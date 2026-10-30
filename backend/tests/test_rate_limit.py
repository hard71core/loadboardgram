"""Per-client-IP rate limiting (core/rate_limit.py) on the unauthenticated
credential endpoints (/api/auth/register, /login) and on POST
/api/search. Limits are read from env at request time, so these tests
monkeypatch them down to something small instead of firing dozens of
requests; conftest.py's autouse fixture clears limiter state between tests.

The RateLimiter unit tests at the bottom need no DB; the route tests have
the same DB requirement as test_health.py.
"""

import uuid
from unittest.mock import patch

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from app.core.rate_limit import RateLimiter
from app.main import app


def _bad_login(client: TestClient):
    return client.post(
        "/api/auth/login",
        json={"email": f"{uuid.uuid4().hex}@example.com", "password": "wrong-password"},
    )


def test_login_is_rate_limited_per_client_ip(monkeypatch):
    monkeypatch.setenv("AUTH_RATE_LIMIT_PER_MINUTE", "3")
    with TestClient(app) as client:
        statuses = [_bad_login(client).status_code for _ in range(3)]
        blocked = _bad_login(client)

    assert statuses == [401, 401, 401]
    assert blocked.status_code == 429
    assert int(blocked.headers["Retry-After"]) > 0


def test_register_shares_the_auth_budget_with_login(monkeypatch):
    # One "auth" bucket across both credential endpoints — otherwise a
    # brute-forcer just spreads attempts across them to double the budget.
    monkeypatch.setenv("AUTH_RATE_LIMIT_PER_MINUTE", "1")
    with TestClient(app) as client:
        assert _bad_login(client).status_code == 401
        blocked = client.post(
            "/api/auth/register",
            json={
                "email": f"{uuid.uuid4().hex}@example.com",
                "password": "secret123",
                "company_name": "Rate Limited Co",
                "role": "shipper",
            },
        )

    assert blocked.status_code == 429


def test_refresh_is_not_rate_limited(monkeypatch):
    # A refresh token is 256 random bits — nothing to brute-force — while a
    # 429 there would make AuthContext.tsx treat the session as dead and log
    # a legitimate user out (e.g. many users behind one NAT). So /refresh
    # stays outside the auth budget, even once that budget is spent.
    monkeypatch.setenv("AUTH_RATE_LIMIT_PER_MINUTE", "1")
    with TestClient(app) as client:
        assert _bad_login(client).status_code == 401
        statuses = {
            client.post("/api/auth/refresh", json={"refresh_token": "not-a-real-token"}).status_code
            for _ in range(3)
        }

    assert statuses == {401}


def test_auth_limit_is_tracked_separately_per_client_ip(monkeypatch):
    monkeypatch.setenv("AUTH_RATE_LIMIT_PER_MINUTE", "1")
    with TestClient(app, client=("203.0.113.1", 50000)) as first:
        assert _bad_login(first).status_code == 401
        assert _bad_login(first).status_code == 429
    with TestClient(app, client=("203.0.113.2", 50000)) as second:
        assert _bad_login(second).status_code == 401


def test_search_is_rate_limited_independently_of_auth(monkeypatch):
    monkeypatch.setenv("SEARCH_RATE_LIMIT_PER_MINUTE", "2")
    monkeypatch.setenv("AUTH_RATE_LIMIT_PER_MINUTE", "5")
    with patch("app.api.routes.search.parse_search_query", return_value=None):
        with TestClient(app) as client:
            statuses = [
                client.post("/api/search", json={"query": "reefer"}).status_code for _ in range(2)
            ]
            blocked = client.post("/api/search", json={"query": "reefer"})
            # Exhausting the search budget must not lock the caller out of login.
            login_after = _bad_login(client)

    assert statuses == [200, 200]
    assert blocked.status_code == 429
    assert login_after.status_code == 401


def test_bearer_protected_auth_routes_are_not_rate_limited(monkeypatch):
    # /me already requires a valid access token — brute-forcing it means
    # guessing a signed JWT, not a password, so it stays out of the budget.
    monkeypatch.setenv("AUTH_RATE_LIMIT_PER_MINUTE", "1")
    with TestClient(app) as client:
        assert _bad_login(client).status_code == 401
        statuses = {
            client.get("/api/auth/me", headers={"Authorization": "Bearer not-a-jwt"}).status_code
            for _ in range(3)
        }

    assert statuses == {401}


# ── RateLimiter unit tests (no DB) ──────────────────────────────────────


class _FakeClock:
    def __init__(self) -> None:
        self.now = 1000.0

    def __call__(self) -> float:
        return self.now


def test_rate_limiter_allows_again_once_the_window_slides_past():
    clock = _FakeClock()
    limiter = RateLimiter(clock=clock)

    limiter.hit("auth", "1.2.3.4", limit=2, window_seconds=60)
    clock.now += 30
    limiter.hit("auth", "1.2.3.4", limit=2, window_seconds=60)
    with pytest.raises(HTTPException) as exc_info:
        limiter.hit("auth", "1.2.3.4", limit=2, window_seconds=60)
    assert exc_info.value.status_code == 429
    # The oldest hit (t=1000) frees up at t=1060; it's t=1030 now.
    assert exc_info.value.headers["Retry-After"] == "30"

    clock.now += 31  # first hit is now outside the window
    limiter.hit("auth", "1.2.3.4", limit=2, window_seconds=60)


def test_rate_limiter_rejected_hits_do_not_extend_the_block():
    # A blocked client hammering away must not keep pushing its own
    # unblock time further out — only accepted hits count.
    clock = _FakeClock()
    limiter = RateLimiter(clock=clock)
    limiter.hit("auth", "1.2.3.4", limit=1, window_seconds=60)
    for _ in range(5):
        clock.now += 10
        with pytest.raises(HTTPException):
            limiter.hit("auth", "1.2.3.4", limit=1, window_seconds=60)

    clock.now += 11  # t=1061, original hit expired
    limiter.hit("auth", "1.2.3.4", limit=1, window_seconds=60)


def test_rate_limiter_reset_clears_all_state():
    limiter = RateLimiter()
    limiter.hit("auth", "1.2.3.4", limit=1, window_seconds=60)
    limiter.reset()
    limiter.hit("auth", "1.2.3.4", limit=1, window_seconds=60)
