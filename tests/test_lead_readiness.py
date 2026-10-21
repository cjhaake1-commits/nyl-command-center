from datetime import date

from core.lead_readiness import evaluate_lead_readiness


def good_record():
    return {
        "Trigger": "Public announcement of a new office opened this month",
        "Source URL": "https://example.com/news",
        "Verified date": "2026-10-15",
        "Business email": "owner@example.com",
        "Warm path": "Chamber introduction",
        "Next action": "Request introduction at the chamber event",
    }


def test_prime_requires_current_public_evidence_contact_action_and_unique_record():
    result = evaluate_lead_readiness(good_record(), today=date(2026, 10, 21))
    assert result["status"] == "PRIME — ready for human review"
    assert result["score"] == 100


def test_stale_source_never_qualifies_as_prime():
    result = evaluate_lead_readiness(good_record(), today=date(2026, 10, 21))
    assert result["status"].startswith("PRIME")
    result = evaluate_lead_readiness(
        {**good_record(), "Verified date": "2026-08-17"},
        today=date(2026, 10, 21),
    )
    assert result["status"] == "REVERIFY — source date is stale or missing"
    assert "Source verified within 30 days" in result["missing_gates"]


def test_missing_contact_and_duplicate_hold_record():
    result = evaluate_lead_readiness(
        good_record(),
        today=date(2026, 10, 21),
        duplicate_in_catalog=True,
    )
    assert result["status"] == "HOLD — research gap"
    assert "No duplicate in research catalog" in result["missing_gates"]
    no_contact = {key: value for key, value in good_record().items() if key != "Business email"}
    result = evaluate_lead_readiness(no_contact, today=date(2026, 10, 21))
    assert "Current public contact route" in result["missing_gates"]
