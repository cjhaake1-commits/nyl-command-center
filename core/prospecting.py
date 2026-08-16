from __future__ import annotations

from datetime import date, datetime
from typing import Iterable, Mapping
from urllib.parse import quote_plus

STAGE_WEIGHT = {
    "New": 4,
    "Attempting contact": 6,
    "Connected": 10,
    "Needs identified": 15,
    "Appointment set": 18,
    "Follow-up": 12,
    "Won": -100,
    "Lost": -100,
}

PUBLIC_SOURCE_PLAYBOOKS = [
    {
        "source": "Referral / introduction",
        "best_for": "Individuals and business owners",
        "signals": "Warm introduction, professional relationship, community connection",
        "where_to_look": "Existing network, client-approved referrals, professional associations, alumni and community groups",
    },
    {
        "source": "Business directories & company websites",
        "best_for": "Corporations, owners, executives and professionals",
        "signals": "New company, leadership change, hiring/growth, new location, expansion, succession need",
        "where_to_look": "Company websites, chambers of commerce, trade associations, public business directories and local economic-development sites",
    },
    {
        "source": "Public business registrations",
        "best_for": "New businesses and owners",
        "signals": "New entity filing, new DBA, new registered business, ownership/management information where publicly provided",
        "where_to_look": "Secretary of State / state corporation registries and local licensing portals",
    },
    {
        "source": "Real-estate & property signals",
        "best_for": "Homeowners, investors and business owners",
        "signals": "Recent purchase, new property, commercial acquisition, building permit or new construction",
        "where_to_look": "County assessor/recorder, municipal permit portals and publicly accessible real-estate records",
    },
    {
        "source": "Professional social media",
        "best_for": "Professionals, executives and business owners",
        "signals": "Promotion, new role, business launch, award, expansion, public event participation",
        "where_to_look": "Public LinkedIn/company pages and other public professional profiles; review manually and respect platform terms",
    },
    {
        "source": "Public social & community signals",
        "best_for": "Individuals and local businesses",
        "signals": "Publicly announced business opening, community event, public milestone or professional accomplishment",
        "where_to_look": "Public business pages, public event pages, local organizations and community calendars; do not infer private/sensitive facts",
    },
    {
        "source": "Local news & press releases",
        "best_for": "Businesses, executives and professionals",
        "signals": "Funding, expansion, promotion, award, acquisition, opening, hiring or other public business trigger",
        "where_to_look": "Local news, company newsrooms, press-release sites and economic-development announcements",
    },
    {
        "source": "Territory demographics (aggregate only)",
        "best_for": "Territory planning, not individual scoring",
        "signals": "Population, household count, homeownership, housing turnover, business density and other area-level market characteristics",
        "where_to_look": "U.S. Census/ACS and other government statistical sources at ZIP/ZCTA, tract, county, city or metro level",
    },
    {
        "source": "Networking & events",
        "best_for": "Individuals and businesses",
        "signals": "Upcoming local event, chamber meeting, trade group, professional conference or community gathering",
        "where_to_look": "Public event calendars, chambers, trade associations, Meetup/event platforms and civic organizations",
    },
]


def _date_value(value: object) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date):
        return value
    text = str(value)[:10]
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        return None


def priority_score(prospect: Mapping[str, object], today: date | None = None) -> float:
    """Rank sales follow-up using non-sensitive business and workflow signals only."""
    today = today or date.today()
    if bool(prospect.get("do_not_contact")):
        return -999.0

    stage = str(prospect.get("stage") or "New")
    if stage in {"Won", "Lost"}:
        return -999.0

    fit = max(1, min(5, int(prospect.get("fit_score") or 3)))
    warmth = max(1, min(5, int(prospect.get("warmth_score") or 3)))
    urgency = max(1, min(5, int(prospect.get("urgency_score") or 3)))
    source_quality = max(1, min(5, int(prospect.get("source_quality") or 3)))

    score = (
        fit * 5.0
        + warmth * 5.0
        + urgency * 4.0
        + source_quality * 3.0
        + STAGE_WEIGHT.get(stage, 4)
    )

    next_action_date = _date_value(prospect.get("next_action_date"))
    if next_action_date:
        days = (next_action_date - today).days
        if days < 0:
            score += min(25.0, 12.0 + abs(days) * 2.0)
        elif days == 0:
            score += 20.0
        elif days <= 2:
            score += 10.0

    last_contact = _date_value(prospect.get("last_contact_date"))
    if last_contact:
        days_since = (today - last_contact).days
        if days_since >= 14:
            score += 8.0
        elif days_since >= 7:
            score += 4.0
    else:
        score += 5.0

    consent = str(prospect.get("consent_status") or "Unknown")
    if consent == "Do not contact":
        return -999.0
    if consent == "Permission / opt-in":
        score += 5.0

    return round(score, 1)


def rank_prospects(prospects: Iterable[Mapping[str, object]], today: date | None = None) -> list[dict]:
    ranked: list[dict] = []
    for prospect in prospects:
        item = dict(prospect)
        item["priority_score"] = priority_score(item, today=today)
        if item["priority_score"] > -900:
            ranked.append(item)
    return sorted(ranked, key=lambda item: item["priority_score"], reverse=True)


def lead_inventory_target(daily_outreach: int, new_name_share: float = 0.35, coverage_days: int = 5) -> dict:
    daily_outreach = max(0, int(daily_outreach))
    share = min(1.0, max(0.0, float(new_name_share)))
    days = max(1, int(coverage_days))
    daily_new_names = int((daily_outreach * share) + 0.999999)
    return {
        "daily_new_names": daily_new_names,
        "coverage_days": days,
        "pipeline_target": daily_new_names * days,
    }


def lead_gap(active_prospects: int, daily_outreach: int, new_name_share: float = 0.35, coverage_days: int = 5) -> dict:
    target = lead_inventory_target(daily_outreach, new_name_share, coverage_days)
    target["active_prospects"] = max(0, int(active_prospects))
    target["gap"] = max(0, target["pipeline_target"] - target["active_prospects"])
    return target


def public_search_queries(territory: str, segment: str) -> list[dict]:
    """Generate public-web research queries; does not scrape sites or infer sensitive traits."""
    territory = territory.strip() or "your territory"
    segment = segment.strip() or "business owners professionals"
    raw = [
        ("New businesses", f'"{territory}" new business opening owner'),
        ("Chamber / business directory", f'"{territory}" chamber of commerce members {segment}'),
        ("Business registrations", f'"{territory}" new business registrations {segment}'),
        ("Promotions / job changes", f'"{territory}" promoted appointed president owner executive {segment}'),
        ("Company growth", f'"{territory}" expansion hiring new location {segment}'),
        ("Real-estate activity", f'"{territory}" recent property sales public records'),
        ("Commercial property", f'"{territory}" commercial property sale acquisition owner'),
        ("Building permits", f'"{territory}" building permits new construction public records'),
        ("Networking events", f'"{territory}" business networking events chamber professional association'),
        ("Public professional profiles", f'site:linkedin.com/in "{territory}" {segment}'),
        ("Company pages", f'site:linkedin.com/company "{territory}" {segment}'),
        ("Local news", f'"{territory}" {segment} award expansion promotion business news'),
    ]
    return [
        {
            "label": label,
            "query": query,
            "search_url": f"https://www.google.com/search?q={quote_plus(query)}",
        }
        for label, query in raw
    ]


def allowed_signal_note() -> str:
    return (
        "Use public, non-sensitive business/professional/property signals and aggregate territory statistics. "
        "Do not infer or score an individual using race/ethnicity, religion, health/disability, sexual orientation, "
        "citizenship/immigration status, genetic information, or financial distress. Honor do-not-contact and firm compliance rules."
    )
