from __future__ import annotations

# Heuristic business-development model, not a published New York Life statistic.
# Scores reflect how strongly a typical business structure maps to public NYL
# business-owner services: key-person/owner protection, succession, retirement,
# executive benefits, employee benefits, and multi-issue planning potential.
INDUSTRY_PROPENSITY = [
    {
        "industry": "Medical / dental / veterinary practices",
        "direct_need_score": 96,
        "coi_value": 76,
        "why": "Owner/partner dependence, disability exposure, buy-sell/succession, retirement planning, key employees and benefits for staff.",
        "best_entry": "Owner/partner continuity + retirement/benefits review",
    },
    {
        "industry": "Law / CPA / architecture / engineering / consulting firms",
        "direct_need_score": 94,
        "coi_value": 94,
        "why": "Partner ownership, key professional dependence, succession, executive retention and strong professional-referral networks.",
        "best_entry": "Partner/key-person continuity + executive/retirement planning",
    },
    {
        "industry": "Construction / electrical / HVAC / plumbing / specialty trades",
        "direct_need_score": 92,
        "coi_value": 78,
        "why": "Often owner-led, dependent on a few estimators/project leaders, growing workforces, succession needs and employee-retention pressure.",
        "best_entry": "Owner/key-person continuity + workforce benefits",
    },
    {
        "industry": "Manufacturing / industrial / distribution",
        "direct_need_score": 91,
        "coi_value": 76,
        "why": "Key management/technical dependence, multi-owner continuity, executive retention, retirement plans and employee-benefit needs.",
        "best_entry": "Key-person + succession + employee/executive benefits",
    },
    {
        "industry": "Technology / software / engineering growth companies",
        "direct_need_score": 90,
        "coi_value": 84,
        "why": "Founder/key-executive concentration, competition for talent, retention needs and rapid organizational change.",
        "best_entry": "Founder/key-person + executive retention",
    },
    {
        "industry": "Commercial real estate / development / property management",
        "direct_need_score": 89,
        "coi_value": 96,
        "why": "Partner/ownership structures, concentrated decision-makers, succession and very strong access to owners, lenders, attorneys and investors.",
        "best_entry": "Partner/owner continuity + COI relationship",
    },
    {
        "industry": "Hospitality / hotels / multi-unit restaurants",
        "direct_need_score": 87,
        "coi_value": 82,
        "why": "Owner/operator dependence, multi-location management, retention pressure and sizeable employee populations.",
        "best_entry": "Owner continuity + key management + workforce benefits",
    },
    {
        "industry": "Logistics / transportation / warehousing",
        "direct_need_score": 86,
        "coi_value": 72,
        "why": "Key operations leaders, succession, employee scale and retention/benefit needs.",
        "best_entry": "Key-person + employee benefits + succession",
    },
    {
        "industry": "Automotive dealers / luxury retail / jewelry / specialty retail",
        "direct_need_score": 85,
        "coi_value": 90,
        "why": "Often owner/family-led, dependent on top producers/managers, succession and strong established-client/referral ecosystems.",
        "best_entry": "Owner/key-person planning + high-trust referral relationships",
    },
    {
        "industry": "Financial-services adjacent firms / benefits / P&C agencies",
        "direct_need_score": 84,
        "coi_value": 98,
        "why": "Professional-owner structures and unusually high referral value into business-owner planning relationships.",
        "best_entry": "COI partnership first; direct firm needs second",
    },
    {
        "industry": "Real estate brokerage / title / mortgage",
        "direct_need_score": 82,
        "coi_value": 97,
        "why": "Owner/broker dependence and exceptional access to households, investors, business owners and transaction-driven introductions.",
        "best_entry": "COI relationship + owner continuity",
    },
    {
        "industry": "Wholesale / food service / business services",
        "direct_need_score": 80,
        "coi_value": 70,
        "why": "Owner/key-manager dependency, employee population and retirement/benefit opportunities, but typically less specialized planning complexity.",
        "best_entry": "Key-person + benefits + retirement",
    },
    {
        "industry": "General retail / consumer services",
        "direct_need_score": 74,
        "coi_value": 66,
        "why": "Owner protection and employee benefits can fit, but strategic complexity and economics vary widely by company.",
        "best_entry": "Owner protection + workforce benefits",
    },
    {
        "industry": "Nonprofit / association / education organizations",
        "direct_need_score": 64,
        "coi_value": 72,
        "why": "Employee/executive benefit and retirement needs may exist, but there is no owner succession/buy-sell need.",
        "best_entry": "Executive/employee benefits and retirement",
    },
]


def normalize_industry(industry: str) -> str:
    return (industry or "").strip().lower()


def industry_profile(industry: str) -> dict:
    text = normalize_industry(industry)
    aliases = [
        (("medical", "dental", "veterinary", "physician", "practice"), 0),
        (("law", "legal", "cpa", "accounting", "architecture", "architect", "engineering", "consulting"), 1),
        (("construction", "electrical", "hvac", "plumbing", "contractor", "roofing", "trade"), 2),
        (("manufacturing", "industrial", "distribution", "fabrication"), 3),
        (("technology", "software", "saas", "tech", "engineering growth"), 4),
        (("commercial real estate", "development", "developer", "property management"), 5),
        (("hospitality", "hotel", "restaurant", "food service", "lodging"), 6),
        (("logistics", "transportation", "trucking", "warehouse", "warehousing"), 7),
        (("automotive", "dealer", "luxury retail", "jewelry", "jeweller", "specialty retail"), 8),
        (("financial services", "insurance agency", "benefits", "p&c", "wealth"), 9),
        (("real estate brokerage", "realtor", "title", "mortgage", "brokerage"), 10),
        (("wholesale", "business services"), 11),
        (("retail", "consumer services"), 12),
        (("nonprofit", "association", "education", "school"), 13),
    ]
    for keywords, idx in aliases:
        if any(keyword in text for keyword in keywords):
            return dict(INDUSTRY_PROPENSITY[idx])
    return {
        "industry": industry or "Other / unclassified",
        "direct_need_score": 70,
        "coi_value": 65,
        "why": "Use the company-specific owner, key-person, workforce, succession and retirement facts to refine the score.",
        "best_entry": "Human review required",
    }


def company_need_score(
    industry: str,
    employee_count: int | None = None,
    owner_led: bool = False,
    multiple_owners: bool = False,
    growth_trigger: bool = False,
    known_key_person: bool = False,
) -> int:
    profile = industry_profile(industry)
    score = int(profile["direct_need_score"])
    if employee_count is not None:
        if employee_count >= 50:
            score += 4
        elif employee_count >= 10:
            score += 2
    if owner_led:
        score += 3
    if multiple_owners:
        score += 2
    if growth_trigger:
        score += 2
    if known_key_person:
        score += 2
    return max(0, min(100, score))
