from __future__ import annotations

# Public-career-history prospecting only.
# A qualifying career transition is a RESEARCH SIGNAL, not evidence that the person
# participated in a retirement plan, has a particular balance, or should roll assets.
# Keep all records DRAFT/HOLD until contact, licensing, firm and communications review.

ROLLOVER_LEADS = []

ROLLOVER_SCREEN = {
    "former_employer_min_headcount": 100,
    "former_employer_min_tenure_years": 3.0,
    "preferred_change_recency_months": 24,
    "geography": "Central Florida / roughly 90 minutes of Orlando",
    "public_sources": ["LinkedIn", "Facebook public professional/business posts", "company bios", "press releases"],
    "exclude": [
        "private/non-public social content",
        "inferred retirement balance",
        "inferred plan participation",
        "protected or sensitive personal traits",
        "people outside approved geography unless separately approved",
    ],
}

ROLLOVER_REVIEW_POINTS = [
    "Leaving assets in a former employer plan can be a valid choice, especially when fees are low or plan investments/features are attractive.",
    "A new employer plan may accept rollovers and can simplify account tracking if its fees, investments and plan features are competitive.",
    "An IRA can provide broader investment choice and account consolidation, but fees, services, protections and investment options must be compared.",
    "Cashing out can trigger current income tax and may trigger an additional early-distribution tax; it also removes assets from retirement savings.",
    "An indirect rollover generally has a 60-day completion window and eligible taxable distributions paid to the participant are generally subject to 20% withholding.",
    "Old accounts can create administrative fragmentation: multiple statements, beneficiaries, allocations, fee schedules and plan communications to monitor.",
    "Plan fees and investment expenses can materially affect long-term results; compare the old plan, new plan and any proposed IRA rather than assuming one is cheaper.",
    "Former-employer plan loans can create special issues after separation; plan terms and IRS rules should be reviewed before any asset movement.",
    "Plan-specific legal protections, withdrawal rules and investment features can differ from an IRA; no recommendation should be made without comparing the actual alternatives.",
]

ROLLOVER_OUTREACH = {
    "phone": (
        "Hi [First Name], this is Christopher Haake with New York Life here in Central Florida. "
        "I came across your recent career move and wanted to introduce myself. When someone changes employers after being with a company for a number of years, "
        "there are usually a few retirement-plan decisions worth reviewing - including whether to leave an old plan where it is, move it to a new employer plan, "
        "or consider an IRA. I am not calling assuming one option is right for you. I would rather spend 20 minutes in person understanding what you have and whether a review would be useful. "
        "Would you be open to a brief meeting next week?"
    ),
    "email": (
        "Subject: A quick retirement-plan review after your career move\n\n"
        "Hi [First Name],\n\n"
        "I saw your recent career move and wanted to introduce myself. I am Christopher Haake with New York Life here in Central Florida.\n\n"
        "When someone leaves an employer after several years, there can be a few choices to review for an old workplace retirement plan - leaving it in place, moving it to a new employer plan if available, or considering an IRA. The right answer depends on the actual plan, fees, investment choices, protections and your broader goals.\n\n"
        "I would be glad to meet for 20 minutes, look at the choices with you, and determine whether anything needs attention. No assumption that a rollover is the right outcome.\n\n"
        "Best,\nChristopher Haake"
    ),
}
