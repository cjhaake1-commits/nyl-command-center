from __future__ import annotations

# Original study drills distilled from user-provided XCEL life-insurance screenshots.
# Content is paraphrased for active recall and exam practice.

CARDS = [
    {"front":"Term life — basic definition","back":"Pure, temporary life-insurance protection for a limited period. It pays a death benefit only if the insured dies while coverage is in force."},
    {"front":"Why term life is usually low cost","back":"Term insurance focuses on mortality protection only and generally does not build cash value, so it can provide a large death benefit for a relatively low initial premium."},
    {"front":"How a term can be defined","back":"A term may be stated as a number of years, such as 10 or 20 years, or it may run until a specified age, such as age 65 or 70."},
    {"front":"If the insured outlives the term","back":"The policy expires and no death benefit is payable unless some separate feature or renewal/conversion option applies."},
    {"front":"If term coverage lapses or is cancelled before death","back":"If the insured dies after coverage has lapsed or been cancelled, the term policy does not pay a death benefit."},
    {"front":"Level term premium concept","back":"Many term policies use a fixed premium during the stated level period because the mortality cost is averaged across the term."},
    {"front":"Main economic advantage of term life","back":"For the same face amount, term insurance typically has a lower initial premium than permanent life insurance."},
    {"front":"Main economic limitation of term life","back":"Term life generally does not accumulate cash value and can expire without paying a benefit if the insured survives the term."},
    {"front":"Term life — death benefit per premium dollar","back":"Term life usually provides the greatest amount of death benefit per dollar of initial premium outlay."},
    {"front":"Three basic term-policy patterns","back":"Level term, decreasing term, and increasing term; they are primarily distinguished by how the face amount changes over time."},
]

QUESTIONS = [
    {"q":"Which statement best describes term life insurance?","choices":["Temporary pure death protection for a stated period","Permanent coverage that always builds cash value","An annuity that pays monthly income","Property insurance for a limited term"],"answer":0,"why":"Term life is temporary death protection for a defined period."},
    {"q":"What happens if an insured survives a basic term policy through the end of its coverage period?","choices":["The policy expires with no death benefit payable","The face amount is automatically paid","The policy becomes whole life automatically","Cash value equal to premiums is refunded"],"answer":0,"why":"Basic term coverage expires if the insured outlives the term."},
    {"q":"Why can term life usually provide more death benefit per premium dollar than permanent life?","choices":["It generally provides pure death protection without building cash value","It has no underwriting","It pays every policyholder at maturity","It is subsidized by property insurers"],"answer":0,"why":"Term focuses on mortality protection rather than combining protection with cash-value accumulation."},
    {"q":"A policy provides coverage from age 45 until age 65. How is its term defined?","choices":["By a specified age","By a cash-value target","By an annuity period","By a premium mode"],"answer":0,"why":"Some term policies remain in force until the insured reaches a stated age."},
    {"q":"What is the primary financial advantage of term life compared with permanent life of the same face amount?","choices":["Lower initial premium","Guaranteed cash-value growth","Guaranteed dividends","Lifetime coverage regardless of premium payment"],"answer":0,"why":"Term insurance generally costs substantially less initially for the same face amount."},
    {"q":"Which of the following is NOT a basic type of term insurance based on face-amount pattern?","choices":["Whole life","Level term","Decreasing term","Increasing term"],"answer":0,"why":"Whole life is permanent insurance; the basic term patterns are level, decreasing, and increasing."},
    {"q":"Why can a level-term policy charge a constant premium for several years even though mortality risk rises with age?","choices":["Premium cost is averaged over the level term","Mortality risk does not rise with age","The insurer waives later-year mortality cost","The policy builds enough dividends to cover all increases"],"answer":0,"why":"The premium can be levelized by averaging expected cost over the stated term."},
    {"q":"Steve owns a 20-year level term policy. He dies in year 12 while the policy is in force. What happens?","choices":["The beneficiary receives the stated death benefit","No benefit is payable because the term was not completed","Only accumulated cash value is paid","Premiums are refunded instead of a death benefit"],"answer":0,"why":"Death during the in-force term triggers the policy's death benefit."},
]

LIGHTNING = [
    ("Pure temporary life protection", "Term life"),
    ("Term insured survives coverage period", "Policy expires; no death benefit"),
    ("Term may be stated by", "Years or a specified age"),
    ("Term cash value", "Generally none"),
    ("Main term advantage", "Large death benefit for low initial premium"),
    ("Main term limitation", "Temporary; may expire with no payout"),
    ("Fixed premium during a term", "Levelized/averaged premium"),
    ("Three basic face-amount patterns", "Level, decreasing, increasing term"),
]
