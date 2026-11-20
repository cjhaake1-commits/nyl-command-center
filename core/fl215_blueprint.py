from __future__ import annotations

FL215_EXAM_FACTS = {
    "total_questions": 165,
    "scored_questions": 150,
    "pretest_questions": 15,
    "time_minutes": 165,
    "passing_score": 0.70,
}

# Current Pearson VUE Florida Agent's Health & Life (including Annuities & Variable Contracts)
# content outline weighting. Percentages apply to the 150 scored questions.
FL215_BLUEPRINT = [
    ("Types of life policies and features", 0.10),
    ("Life policy riders, provisions, options, exclusions", 0.10),
    ("Life application, underwriting, policy delivery", 0.08),
    ("Retirement and other life concepts", 0.05),
    ("Types of health policies", 0.11),
    ("Health policy provisions, clauses, riders", 0.10),
    ("Social insurance: Medicare, Medicaid, Social Security", 0.04),
    ("Other health insurance concepts", 0.04),
    ("Field underwriting procedures", 0.05),
    ("Florida statutes/rules common to all lines", 0.13),
    ("Florida statutes: life, annuity, variable products", 0.10),
    ("Florida statutes: health insurance", 0.10),
]

# Consensus priorities combine official weighting with recurring public candidate/prep discussion themes.
# 'Official' = directly supported by current outline. 'Public signal' = recurring anecdotal emphasis only.
CONSENSUS_PRIORITIES = [
    {"topic": "Florida statutes, rules, licensing, unfair trade practices", "priority": "Very high", "basis": "Official", "why": "33% of scored questions are Florida-specific when the three Florida-law sections are combined."},
    {"topic": "Life policy types and features", "priority": "High", "basis": "Official", "why": "10% official weight; recurring public prep emphasis on term, whole, universal, variable and indexed products."},
    {"topic": "Life provisions, riders, beneficiaries, nonforfeiture", "priority": "High", "basis": "Official + public signal", "why": "10% official weight and repeated candidate reports that provisions can be a weak spot."},
    {"topic": "Health policy types", "priority": "High", "basis": "Official", "why": "11% official weight, the largest non-Florida-law individual content area."},
    {"topic": "Health/disability provisions and clauses", "priority": "High", "basis": "Official + public signal", "why": "10% official weight; candidate reports repeatedly mention disability and less-common provisions."},
    {"topic": "Applications, underwriting, field underwriting, delivery", "priority": "High", "basis": "Official", "why": "13% combined across life application/underwriting and field underwriting."},
    {"topic": "Annuities and variable contracts", "priority": "High", "basis": "Official + public signal", "why": "Embedded in life/annuity statutory coverage and frequently represented in public study sets."},
    {"topic": "Medicare / Medicaid / Social Security", "priority": "Medium", "basis": "Official", "why": "4% official social-insurance weighting; highly memorizable and efficient points."},
    {"topic": "Exact Florida numbers, deadlines, age thresholds, free-look periods", "priority": "Very high", "basis": "Official-source-only", "why": "These are memorization-heavy and can change; use current Florida DFS/Pearson-approved material rather than old crowdsourced cards."},
    {"topic": "Terminology recognition", "priority": "Very high", "basis": "Public signal", "why": "Multiple candidates describe success from terminology mastery and failure from memorizing answer patterns without understanding terms."},
]

MEMORIZATION_BUCKETS = {
    "Definitions": [
        "peril vs hazard", "pure vs speculative risk", "moral vs morale hazard", "indemnity", "insurable interest",
        "aleatory", "unilateral", "adhesion", "conditional", "representation vs warranty",
        "express / implied / apparent authority", "domestic / foreign / alien insurer",
    ],
    "Unfair trade practices": [
        "twisting", "rebating", "misrepresentation", "churning", "sliding", "defamation", "coercion", "unfair discrimination",
    ],
    "Life": [
        "term / whole / universal / variable life", "revocable vs irrevocable beneficiary", "primary vs contingent beneficiary",
        "waiver of premium", "guaranteed insurability", "accelerated benefit", "cash surrender / reduced paid-up / extended term",
        "absolute vs collateral assignment", "reinstatement", "grace period", "incontestability",
    ],
    "Annuities": [
        "immediate vs deferred", "fixed vs variable", "accumulation unit vs annuity unit", "annuitization",
        "life only / period certain / refund / joint-and-survivor", "qualified vs nonqualified",
    ],
    "Health": [
        "deductible / copay / coinsurance", "elimination period / benefit period", "noncancelable / guaranteed renewable / optionally renewable",
        "HMO / PPO / POS", "coordination of benefits", "long-term care benefit triggers",
        "Medicare A / B / C / D", "Medicaid", "Social Security disability",
    ],
    "Florida exact-rule bucket": [
        "free-look periods", "licensing/appointment deadlines", "CE rules", "response deadlines", "penalties", "age thresholds", "dollar limits",
    ],
}

PUBLIC_STUDY_CONSENSUS = [
    "Do many practice exams, but review every miss instead of memorizing the answer letter.",
    "Know terminology well enough to recognize it inside a short scenario.",
    "Write down or flashcard laws with numbers and concepts that repeatedly cause misses.",
    "Aim for repeated mid-80s or better on practice exams before relying on readiness.",
    "Read questions carefully; words like NOT, EXCEPT, BEST and MOST can change the answer.",
    "Use full-length simulations for timing and shorter untimed sets for learning from mistakes.",
]
