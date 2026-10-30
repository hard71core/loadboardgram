"""core/llm.py's NL_SEARCH_ENABLED gate and its fail-closed contract. The
Anthropic SDK itself is mocked here too — these assert whether the client
gets constructed at all, not what it returns; see test_search.py for how a
SearchFilter (or None) drives the route's behavior. No DB needed — these
call parse_search_query() directly rather than going through TestClient."""

from datetime import date
from unittest.mock import MagicMock, patch

from app.core.llm import parse_search_query


def test_parse_search_query_returns_none_when_flag_is_off(monkeypatch):
    monkeypatch.delenv("NL_SEARCH_ENABLED", raising=False)  # unset -> defaults off
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-a-real-looking-key")
    with patch("app.core.llm.anthropic.Anthropic") as mock_client:
        result = parse_search_query("reefer out of Dallas")
    assert result is None
    mock_client.assert_not_called()  # the flag must gate before any API call, not just the key


def test_parse_search_query_returns_none_without_a_key_even_when_enabled(monkeypatch):
    monkeypatch.setenv("NL_SEARCH_ENABLED", "true")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    with patch("app.core.llm.anthropic.Anthropic") as mock_client:
        result = parse_search_query("reefer out of Dallas")
    assert result is None
    mock_client.assert_not_called()


def test_parse_search_query_calls_anthropic_when_enabled_and_configured(monkeypatch):
    monkeypatch.setenv("NL_SEARCH_ENABLED", "true")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-a-real-looking-key")

    mock_response = MagicMock()
    mock_response.parsed_output = "sentinel-filter"
    mock_client_instance = MagicMock()
    mock_client_instance.messages.parse.return_value = mock_response

    with patch(
        "app.core.llm.anthropic.Anthropic", return_value=mock_client_instance
    ) as mock_client:
        result = parse_search_query("reefer out of Dallas")

    mock_client.assert_called_once_with(api_key="sk-ant-a-real-looking-key")
    assert result == "sentinel-filter"


def test_parse_search_query_returns_none_when_the_anthropic_call_raises(monkeypatch):
    """Fail-closed on a live-call failure too, not just a missing key/flag —
    a timeout, a rate limit, an outage, whatever. api/routes/search.py's
    keyword fallback depends on this never propagating an exception."""
    monkeypatch.setenv("NL_SEARCH_ENABLED", "true")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-a-real-looking-key")

    mock_client_instance = MagicMock()
    mock_client_instance.messages.parse.side_effect = RuntimeError("Anthropic is down")

    with patch("app.core.llm.anthropic.Anthropic", return_value=mock_client_instance):
        result = parse_search_query("reefer out of Dallas")

    assert result is None


def _enabled_with_mock_client(monkeypatch) -> MagicMock:
    monkeypatch.setenv("NL_SEARCH_ENABLED", "true")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-a-real-looking-key")
    mock_client_instance = MagicMock()
    mock_client_instance.messages.parse.return_value.parsed_output = "sentinel-filter"
    return mock_client_instance


def test_parse_search_query_stops_calling_anthropic_once_the_daily_cap_is_hit(monkeypatch):
    """A per-period cost cap, not just a per-IP rate limit: once
    NL_SEARCH_DAILY_LIMIT calls have gone out today, further queries fall
    back to keyword search (None) without constructing a client at all —
    no matter how many distinct IPs they come from."""
    mock_client_instance = _enabled_with_mock_client(monkeypatch)
    monkeypatch.setenv("NL_SEARCH_DAILY_LIMIT", "2")

    with patch(
        "app.core.llm.anthropic.Anthropic", return_value=mock_client_instance
    ) as mock_client:
        results = [parse_search_query("reefer out of Dallas") for _ in range(3)]

    assert results == ["sentinel-filter", "sentinel-filter", None]
    assert mock_client.call_count == 2


def test_parse_search_query_daily_cap_resets_on_a_new_utc_day(monkeypatch):
    mock_client_instance = _enabled_with_mock_client(monkeypatch)
    monkeypatch.setenv("NL_SEARCH_DAILY_LIMIT", "1")

    with patch("app.core.llm.anthropic.Anthropic", return_value=mock_client_instance):
        with patch("app.core.llm._today", return_value=date(2026, 10, 30)):
            assert parse_search_query("reefer") == "sentinel-filter"
            assert parse_search_query("reefer") is None
        with patch("app.core.llm._today", return_value=date(2026, 10, 31)):
            assert parse_search_query("reefer") == "sentinel-filter"


def test_parse_search_query_failed_calls_still_count_toward_the_daily_cap(monkeypatch):
    # A call that errors out may still have been billed (e.g. a timeout
    # after the provider did the work) — count attempts, not successes.
    mock_client_instance = _enabled_with_mock_client(monkeypatch)
    mock_client_instance.messages.parse.side_effect = RuntimeError("Anthropic is down")
    monkeypatch.setenv("NL_SEARCH_DAILY_LIMIT", "1")

    with patch(
        "app.core.llm.anthropic.Anthropic", return_value=mock_client_instance
    ) as mock_client:
        parse_search_query("reefer")
        parse_search_query("reefer")

    assert mock_client.call_count == 1


def test_parse_search_query_flag_off_does_not_consume_the_daily_cap(monkeypatch):
    mock_client_instance = _enabled_with_mock_client(monkeypatch)
    monkeypatch.setenv("NL_SEARCH_DAILY_LIMIT", "1")

    monkeypatch.setenv("NL_SEARCH_ENABLED", "false")
    parse_search_query("reefer")
    monkeypatch.setenv("NL_SEARCH_ENABLED", "true")
    with patch("app.core.llm.anthropic.Anthropic", return_value=mock_client_instance):
        assert parse_search_query("reefer") == "sentinel-filter"
