"""Per-client-IP rate limiting for endpoints that are cheap to abuse: the
unauthenticated credential endpoints (password brute-force, sign-up spam)
and NL search (each call can be a billed Anthropic request).

Sliding-window log, held in this process's memory — deliberately the
smallest thing that actually closes the gap at demo scale, not the target
design. Its limits are explicit:

- State is per-process. Under several uvicorn workers or replicas each one
  keeps its own counters, so the effective limit is N × the configured one.
  The target (docs/technical-documentation.html section 9) is rate limiting
  at the API gateway, or a shared store like Redis behind this same
  interface.
- The key is the TCP peer address (request.client.host). X-Forwarded-For is
  deliberately ignored: it's client-controlled, and trusting it without a
  known proxy in front would let anyone mint a fresh budget per request.
  Behind a reverse proxy every caller would share the proxy's IP — that's
  the point to add trusted-proxy handling, not before.

Limits are read from env on every request (not at import time) so they can
be tuned without a code change and overridden per test.
"""

import math
import os
import threading
import time
from collections import defaultdict, deque
from collections.abc import Callable

from fastapi import HTTPException, Request

from . import database  # noqa: F401  (import for its load_dotenv() side effect)

WINDOW_SECONDS = 60


class RateLimiter:
    def __init__(self, clock: Callable[[], float] = time.monotonic) -> None:
        self._clock = clock
        self._hits: dict[tuple[str, str], deque[float]] = defaultdict(deque)
        # Sync routes run in FastAPI's threadpool, so concurrent requests
        # really can race on the same deque.
        self._lock = threading.Lock()

    def hit(self, scope: str, key: str, *, limit: int, window_seconds: int) -> None:
        """Records one request for (scope, key), or raises 429 if that would
        exceed `limit` within the trailing `window_seconds`. Rejected
        requests aren't recorded — a blocked client retrying in a loop
        doesn't push its own unblock time further out."""
        now = self._clock()
        with self._lock:
            hits = self._hits[(scope, key)]
            while hits and hits[0] <= now - window_seconds:
                hits.popleft()
            if len(hits) >= limit:
                retry_after = max(1, math.ceil(hits[0] + window_seconds - now))
                raise HTTPException(
                    status_code=429,
                    detail="Too many requests, try again later",
                    headers={"Retry-After": str(retry_after)},
                )
            hits.append(now)

    def reset(self) -> None:
        with self._lock:
            self._hits.clear()


limiter = RateLimiter()


def _limit_from_env(var: str, default: int) -> int:
    return int(os.getenv(var, str(default)))


def _client_key(request: Request) -> str:
    return request.client.host if request.client else "unknown"


def auth_rate_limit(request: Request) -> None:
    """One shared budget across register and login — separate budgets would
    just let a brute-forcer spread attempts across them. /refresh is left
    out on purpose, see its docstring in api/routes/auth.py."""
    limiter.hit(
        "auth",
        _client_key(request),
        limit=_limit_from_env("AUTH_RATE_LIMIT_PER_MINUTE", 10),
        window_seconds=WINDOW_SECONDS,
    )


def search_rate_limit(request: Request) -> None:
    limiter.hit(
        "search",
        _client_key(request),
        limit=_limit_from_env("SEARCH_RATE_LIMIT_PER_MINUTE", 20),
        window_seconds=WINDOW_SECONDS,
    )
