from __future__ import annotations

from datetime import date, datetime
from typing import Any, Mapping
from urllib.parse import urlparse

MAX_SOURCE_AGE_DAYS = 30


def _value(row: Mapping[str, Any], *keys: str) -> str:
    for key in keys:
        value = row.get(key)
        if value is not None:
            text = str(value).strip()
            if text and text.lower() not in {"nan", "none", "n/a", "null"}:
                return text
    return ""


def _valid_contact(row: Mapping[str, Any]) -> bool:
    email = _value(row, "Business email", "Email", "email", "Public email")
    if email and "@" in email and "." in email.rsplit("@", 1)[-1]:
        return True
    phone = _value(row, "Business phone", "Phone", "phone", "Public phone")
    if phone and sum(ch.isdigit() for ch in phone) >= 10:
        return True
    contact = _value(row, "Public Contact", "Contact", "Contact URL", "LinkedIn URL")
    if contact:
        parsed = urlparse(contact)
        if parsed.scheme in {"http", "https"} and parsed.netloc:
            return True
        if len(contact) >= 12 and any(word in contact.lower() for word in ("call ", "email ", "contact ", "office ", "linkedin")):
            return True
    return False


def _source_date(row: Mapping[str, Any]) -> date | None:
    raw = _value(row, "Verified date", "Verified Date", "Verification date", "Source date")
    try:
        return date.fromisoformat(raw[:10])
    except (TypeError, ValueError):
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00")).date()
        except (TypeError, ValueError):
            return None


def evaluate_lead_readiness(
    row: Mapping[str, Any],
    *,
    today: date | None = None,
    duplicate_in_catalog: bool = False,
) -> dict[str, Any]:
    """Assess public research completeness, never suitability or product need."""
    today = today or date.today()
    cause = _value(row, "Trigger", "Signal", "Public cause", "Business event")
    source_urls = _value(row, "Source URL", "Source Url", "Source", "Public source")
    parsed_urls = [part.strip() for part in source_urls.split("|") if part.strip()]
    has_source = any(urlparse(url).scheme in {"http", "https"} and urlparse(url).netloc for url in parsed_urls)
    source_date = _source_date(row)
    age_days = (today - source_date).days if source_date else None
    fresh = age_days is not None and 0 <= age_days <= MAX_SOURCE_AGE_DAYS
    contact = _valid_contact(row)
    next_action = _value(row, "Next action", "Next Action", "Next step", "Action")
    action = len(next_action) >= 12 and next_action.lower() not in {"research", "follow up", "contact prospect"}
    unique = not duplicate_in_catalog

    gates = {
        "Specific public cause": bool(cause),
        "Dated source link": has_source,
        "Source verified within 30 days": fresh,
        "Current public contact route": contact,
        "Actionable next step": action,
        "No duplicate in research catalog": unique,
    }
    passed = sum(gates.values())
    missing = [name for name, ok in gates.items() if not ok]
    if passed == len(gates):
        status = "PRIME — ready for human review"
    elif not fresh and all(ok for name, ok in gates.items() if name != "Source verified within 30 days"):
        status = "REVERIFY — source date is stale or missing"
    else:
        status = "HOLD — research gap"
    return {
        "status": status,
        "score": round(100 * passed / len(gates)),
        "missing_gates": "; ".join(missing),
        "source_age_days": age_days,
        "gates": gates,
    }
