from __future__ import annotations

from data.paul_business_leads import BUSINESS_ROWS
from data.paul_individual_leads import INDIVIDUAL_ROWS

# Paul Beck tenant data. This file is intentionally separate from the Chris Haake
# Central Florida datasets so no Orlando/Florida prospects leak into Paul's app.
# Source rows are public/professional only. No residential/home-address-derived
# outreach data is permitted. All outreach remains HOLD / RESEARCH ONLY /
# COMPLIANCE REVIEW unless separately authorized after licensing/compliance review.

OUTREACH_STATUS = "HOLD"
RESEARCH_STATUS = "RESEARCH ONLY"
COMPLIANCE_STATUS = "COMPLIANCE REVIEW"


def _dedupe(rows: list[dict], key: str) -> list[dict]:
    seen: set[str] = set()
    result: list[dict] = []
    for row in rows:
        value = str(row.get(key, "")).strip().casefold()
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(row)
    return result


PUBLIC_LEADS = _dedupe([
    {
        "Business": name,
        "City": city,
        "Category": category,
        "Professional Phone": phone,
        "Website": website,
        "Verification Source": source,
        "Score": score,
        "Outreach Status": OUTREACH_STATUS,
        "Research Status": RESEARCH_STATUS,
        "Compliance Status": COMPLIANCE_STATUS,
        "Tenant": "Paul Beck",
        "Territory": "Simi Valley 93065 + 20-mile radius",
    }
    for name, city, category, phone, website, source, score in BUSINESS_ROWS
], "Business")

HNW_LEADS = _dedupe([
    {
        "Name": name,
        "Organization": organization,
        "Professional Role": role,
        "City": city,
        "Professional Phone": phone,
        "Verification Source": source,
        "Score": score,
        "Outreach Status": OUTREACH_STATUS,
        "Research Status": RESEARCH_STATUS,
        "Compliance Status": COMPLIANCE_STATUS,
        "Tenant": "Paul Beck",
        "Territory": "Simi Valley 93065 + 20-mile radius",
    }
    for name, organization, role, city, phone, source, score in INDIVIDUAL_ROWS
], "Name")

# Referral-network candidates are included in HNW_LEADS/individual COIs for now so
# the tenant has one deduplicated individual count. Keep this separate list empty
# rather than double-counting the same people in the UI total.
MARKETING_NETWORK_LEADS: list[dict] = []

TARGET_INDIVIDUALS = 100
TARGET_BUSINESSES = 24
INDIVIDUAL_TARGET_MET = len(HNW_LEADS) >= TARGET_INDIVIDUALS
BUSINESS_TARGET_MET = len(PUBLIC_LEADS) >= TARGET_BUSINESSES
