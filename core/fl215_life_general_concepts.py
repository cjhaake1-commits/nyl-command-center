from __future__ import annotations

# Original study drills distilled from user-provided XCEL life-insurance screenshots.
# Content is paraphrased for active recall and exam practice.

CARDS = [
    {"front":"Life insurance — core purpose","back":"Transfers the financial risk of premature death from the insured/policyowner side to the insurer in exchange for premium."},
    {"front":"Immediate estate","back":"Life insurance can instantly create a pool of money for a named beneficiary at the insured's death, so it is often described as creating an immediate estate."},
    {"front":"Are life policies standardized?","back":"Unlike many property/casualty forms, life insurance policies are not one single standardized form; products vary by duration, funding method, benefit design, ownership, and market."},
    {"front":"Broad life-insurance classifications","back":"Common classifications include temporary vs permanent, individual vs group, fixed vs variable, and specialized forms such as industrial/burial/debt-related coverage."},
    {"front":"Mortality and premium relationship","back":"The probability of death generally rises with age, so the pure cost of life insurance increases as an insured gets older."},
    {"front":"Term life insurance","back":"Temporary protection for a stated period. It primarily covers the mortality risk during that term and generally has no cash value."},
    {"front":"Levelized term premium concept","back":"For multi-year level-premium term, the premium can be averaged across the term: it may be higher than pure mortality cost in early years and lower than pure mortality cost in later years."},
    {"front":"Age at issue — why it matters","back":"A level-term policy priced at issue reflects the insured's age when the policy starts; locking in a younger issue age can make later-year cost lower than buying fresh one-year coverage at an older age."},
    {"front":"Permanent life insurance","back":"Designed to provide lifelong protection rather than coverage for a limited term, assuming required premiums/funding and policy conditions are maintained."},
    {"front":"Permanent life — advance funding idea","back":"Because mortality cost becomes very high at advanced ages, permanent policies generally collect more than the current mortality cost in earlier years and build value/reserves to help fund later-year protection."},
]

QUESTIONS = [
    {"q":"Why is life insurance often said to create an immediate estate?","choices":["It can create a death-benefit fund for the beneficiary immediately upon the insured's death","It always creates real estate ownership","It eliminates all estate taxes","It converts term insurance into property insurance"],"answer":0,"why":"The death benefit can create an immediate pool of money for beneficiaries at death."},
    {"q":"Which statement best describes term life insurance?","choices":["Temporary protection for a stated period","Permanent coverage with guaranteed lifelong cash value in every case","Property indemnity coverage","Coverage that always pays at maturity"],"answer":0,"why":"Term insurance is temporary life insurance for a defined period."},
    {"q":"Why do life-insurance costs generally increase with age?","choices":["Mortality risk generally increases with age","Older applicants always request larger death benefits","State law doubles every premium annually","Beneficiaries become older"],"answer":0,"why":"The insurer's expected mortality cost generally rises as the insured gets older."},
    {"q":"A 10-year level-term premium may exceed pure mortality cost in early years but be below pure mortality cost in later years. What principle explains this?","choices":["Levelized/average premium pricing across the term","Subrogation","Insurable interest","Adhesion"],"answer":0,"why":"The premium is averaged over the policy term rather than repriced to pure annual mortality each year."},
    {"q":"Which statement best describes permanent life insurance?","choices":["It is designed to continue for the insured's lifetime if properly maintained","It can never build value","It always expires after one year","It is identical to decreasing term"],"answer":0,"why":"Permanent life is designed for lifelong rather than temporary protection."},
    {"q":"Why does permanent insurance typically collect more than current mortality cost in earlier years?","choices":["To help fund much higher mortality costs in later years","To pay property losses","To eliminate underwriting","To create a broker commission reserve"],"answer":0,"why":"Permanent insurance uses advance funding/reserves to support later-year coverage when mortality costs are much higher."},
]

LIGHTNING = [
    ("Life insurance transfers what risk?", "Risk of death / mortality risk"),
    ("Creates money for beneficiary at death", "Immediate estate"),
    ("Temporary life coverage", "Term life"),
    ("Lifelong design", "Permanent life"),
    ("Death risk generally rises with", "Age"),
    ("Multi-year term premium averaged over time", "Levelized/average premium"),
    ("Younger issue age can help lock in", "Lower level pricing for the selected term"),
    ("Permanent insurance early-year overfunding helps pay", "Higher later-year mortality costs"),
]
