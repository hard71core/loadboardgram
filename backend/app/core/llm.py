"""Thin wrapper around the Anthropic SDK for the NL-search feature.

Deliberately the only place in the codebase that talks to an LLM provider —
see docs/technical-documentation.html section 7.8 ("LLM Gateway" as a single
call point) and section 7 ("a model is never a single point of failure").
Every call here fails closed: any problem (feature flag off, no key, network
error, provider outage, a response that doesn't parse) returns None, and the
caller treats that exactly like "the user didn't specify a filter" rather
than an error — see api/routes/search.py's keyword fallback.
"""

import logging
import os
import threading
from datetime import UTC, date, datetime

import anthropic

from ..schemas import SearchFilter

logger = logging.getLogger(__name__)

# Structured extraction, not open-ended reasoning — Haiku is the right size
# for this and an order of magnitude cheaper than Opus for the same job.
MODEL = "claude-haiku-4-5"

_SYSTEM_PROMPT = (
    "Extract search filters for a freight load board from the user's "
    "free-text query. Only set a field if the query actually specifies it "
    "— leave everything else null; do not guess or default. "
    "equipment_type must be exactly 'Dry Van', 'Reefer', or 'Flatbed' when "
    "given, and null otherwise."
)


def _nl_search_enabled() -> bool:
    return os.getenv("NL_SEARCH_ENABLED", "false").strip().lower() in ("1", "true", "yes")


# Process-wide cap on Anthropic calls per UTC day — the cost cap, as opposed
# to core/rate_limit.py's per-IP limit, which many IPs together can still
# multiply. In-memory and per-process, same caveat as rate_limit.py: under
# N workers the real ceiling is N × NL_SEARCH_DAILY_LIMIT, and a restart
# resets it. The target is section 7.8's cost budget + circuit breaker.
_usage_lock = threading.Lock()
_usage_day: date | None = None
_usage_count = 0


def _today() -> date:
    return datetime.now(UTC).date()


def _try_consume_daily_budget() -> bool:
    """Counts one call against today's budget, or returns False if it's
    spent. Counted before the call, not after a success: a call that times
    out may still have been billed."""
    global _usage_day, _usage_count
    limit = int(os.getenv("NL_SEARCH_DAILY_LIMIT", "500"))
    today = _today()
    with _usage_lock:
        if _usage_day != today:
            _usage_day, _usage_count = today, 0
        if _usage_count >= limit:
            return False
        _usage_count += 1
        return True


def reset_daily_usage() -> None:
    global _usage_day, _usage_count
    with _usage_lock:
        _usage_day, _usage_count = None, 0


def parse_search_query(query: str) -> SearchFilter | None:
    """Turns free text like "reefer out of Dallas this week under 900" into
    a SearchFilter. Returns None if NL_SEARCH_ENABLED isn't turned on, the
    key isn't configured, today's NL_SEARCH_DAILY_LIMIT is spent, the API
    call fails, or the response doesn't
    validate — callers must fall back to a plain keyword match in every one
    of those cases, not raise.

    NL_SEARCH_ENABLED defaults to off: the feature works end-to-end (the
    keyword fallback), but nothing here spends Anthropic credits until it's
    deliberately turned on in .env — see .env.example."""
    if not _nl_search_enabled():
        return None

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or api_key.startswith("replace-with-"):
        return None

    if not _try_consume_daily_budget():
        logger.warning(
            "NL search: daily Anthropic call budget spent, falling back to keyword search"
        )
        return None

    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.parse(
            model=MODEL,
            max_tokens=1024,
            system=_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": query}],
            output_format=SearchFilter,
        )
    except Exception:
        logger.exception("NL search: Anthropic call failed, falling back to keyword search")
        return None

    return response.parsed_output
