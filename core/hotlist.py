from __future__ import annotations

# Public-business research candidates only. Rankings use public role, business relevance,
# local-network accessibility and relationship-development fit. They do not use inferred
# personal wealth, health, protected traits, or private financial information.
ORLANDO_PUBLIC_HOTLIST = [
    {
        "rank": 1,
        "organization": "Massey Services",
        "contact": "Tony Massey",
        "role": "President & CEO",
        "area": "Orlando",
        "segment": "Business owner / executive",
        "hot_score": 96,
        "public_signal": "Orlando-headquartered, second-generation leadership, privately held/family-company profile, broad operating footprint and strong Central Florida civic involvement.",
        "relationship_angle": "Business-owner planning, continuity/key-person education, executive relationships and COI introductions after compliant discovery.",
        "source_url": "https://www.masseyservices.com/leaders/tony-massey/",
    },
    {
        "rank": 2,
        "organization": "Baker Barrios Architects",
        "contact": "Timothy Baker",
        "role": "Partner + Chief Executive Officer",
        "area": "Orlando",
        "segment": "Founder / professional-services executive",
        "hot_score": 94,
        "public_signal": "Founder-led Orlando-headquartered architecture/design firm with multi-market growth and visible civic/business leadership.",
        "relationship_angle": "Founder/partner continuity, executive planning and professional-services COI network after compliant discovery.",
        "source_url": "https://www.bakerbarrios.com/leadership/timothy-baker/",
    },
    {
        "rank": 3,
        "organization": "McCraney Property Company",
        "contact": "Steven E. McCraney",
        "role": "President & CEO",
        "area": "Orlando / Central Florida",
        "segment": "Founder / commercial real estate",
        "hot_score": 93,
        "public_signal": "Founder-led private commercial real-estate investment/development firm with an Orlando office and substantial Southeast development activity.",
        "relationship_angle": "Owner/executive relationships, succession/continuity education and commercial-real-estate COI introductions after compliant discovery.",
        "source_url": "https://mccraneyproperty.com/about/meet-the-team/steven-mccraney-4/",
    },
    {
        "rank": 4,
        "organization": "4R Restaurant Group / 4 Rivers Smokehouse",
        "contact": "John Rivers",
        "role": "Founder / CEO",
        "area": "Winter Park",
        "segment": "Founder / hospitality",
        "hot_score": 91,
        "public_signal": "Founder-led Central Florida restaurant group with a strong Winter Park identity and community visibility.",
        "relationship_angle": "Founder/business-owner planning and community-network introductions after compliant discovery.",
        "source_url": "https://www.4rsmokehouse.com/about/",
    },
    {
        "rank": 5,
        "organization": "Palmer Electric Company",
        "contact": "Tom Beard",
        "role": "Chairman & CEO",
        "area": "Winter Park / Orlando",
        "segment": "Established private business",
        "hot_score": 89,
        "public_signal": "Long-established Central Florida electrical contractor with public executive leadership and deep local operating history.",
        "relationship_angle": "Executive/business continuity, key-person and workforce/owner planning conversations after compliant discovery.",
        "source_url": "https://www.palmer-electric.com/about/our-team/",
    },
    {
        "rank": 6,
        "organization": "BOS Orlando",
        "contact": "Jessica Platt",
        "role": "Market President",
        "area": "Lake Mary",
        "segment": "Executive / employee-owned business",
        "hot_score": 86,
        "public_signal": "Lake Mary-based Orlando operation of an employee-owned workplace company with a visible local leadership and business-development team.",
        "relationship_angle": "Executive relationships and business/professional introductions; especially useful as a Lake Mary COI network.",
        "source_url": "https://www.bos.com/orlando/bos-orlando-team/",
    },
    {
        "rank": 7,
        "organization": "Avison Young - Orlando",
        "contact": "Greg Morrison",
        "role": "Principal, Managing Director - Orlando",
        "area": "Orlando",
        "segment": "Center of influence / commercial real estate",
        "hot_score": 84,
        "public_signal": "Publicly listed Orlando managing director in a major commercial real-estate advisory network.",
        "relationship_angle": "High-value COI relationship for introductions to owners, executives, developers and commercial-property decision makers.",
        "source_url": "https://orlando.org/companies/",
    },
    {
        "rank": 8,
        "organization": "Fannie Hillman + Associates",
        "contact": "Kevin McClanahan",
        "role": "Sales Manager / REALTOR",
        "area": "Winter Park",
        "segment": "Center of influence / residential real estate",
        "hot_score": 82,
        "public_signal": "Long-established locally owned Winter Park real-estate brokerage with a public sales manager active in local business/community leadership.",
        "relationship_angle": "COI relationship for compliant introductions tied to life transitions and business/professional networks; do not use client/property value to infer financial need.",
        "source_url": "https://fanniehillman.com/agent/kevin-mcclanahan/",
    },
]


def salesforce_relationship_priority(
    *,
    is_existing_policyholder: bool,
    review_due: bool,
    inbound_engagement: bool,
    documented_planning_gap: bool,
    days_since_contact: int | None = None,
) -> int:
    """Future Salesforce-ready relationship priority using approved relationship/workflow signals.

    Intentionally excludes inferred wealth, health, claims, protected traits and private
    financial-condition scoring. A documented planning gap must come from an approved
    needs-analysis/review process, not an inference from public data.
    """
    score = 0
    if is_existing_policyholder:
        score += 50
    if review_due:
        score += 20
    if inbound_engagement:
        score += 15
    if documented_planning_gap:
        score += 15
    if days_since_contact is not None and days_since_contact >= 365:
        score += 5
    return score
