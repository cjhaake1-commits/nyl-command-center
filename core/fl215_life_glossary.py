from __future__ import annotations

# Original study drills distilled from user-provided XCEL glossary screenshots.
# Definitions are paraphrased for active recall; no proprietary exam questions are reproduced.

CARDS = [
    {"front":"Accidental Death Benefit (ADB)","back":"Coverage that pays for qualifying accidental death and may cover specified accidental losses such as sight, speech, hearing, use of limbs/paralysis, or loss of members, subject to policy terms."},
    {"front":"Adjustable Life Insurance","back":"Permanent life insurance allowing changes to premium and death-benefit structure within policy limits. Course distinction: its cash-value mechanics differ from universal life and may use a guaranteed fixed basis."},
    {"front":"Attained Age","back":"The insured's current age as of a specified date. Depending on insurer practice, insurance age may be based on nearest birthday or last birthday."},
    {"front":"Cash Surrender Value","back":"Cash amount available to the policyowner when surrendering a cash-value life policy, subject to contract terms, loans, charges, and other adjustments."},
    {"front":"Convertible Term Life Insurance","back":"Term insurance that allows conversion to an eligible permanent policy during the conversion period without new evidence of insurability."},
    {"front":"Decreasing Term Insurance","back":"Temporary insurance with a death benefit/face amount that declines over time; commonly associated with a declining debt or loan obligation."},
    {"front":"Endowment Contract","back":"A contract designed to pay the face amount at the end of a stated period or age if the insured survives, or to pay the death benefit if the insured dies earlier."},
    {"front":"Extended Term Insurance","back":"A nonforfeiture option that uses available cash value to continue term insurance, generally for the original face amount, for as long as the value will purchase."},
    {"front":"Family Income Policy","back":"A life-insurance design combining permanent/whole-life protection with decreasing-term protection to provide a death benefit plus an income stream during a stated family-income period."},
    {"front":"Joint Life Insurance","back":"One policy covering two or more lives that typically pays at the first insured death and then terminates. Contrast with survivorship/second-to-die coverage."},
    {"front":"Universal Life Insurance","back":"Flexible-premium permanent life insurance with an adjustable death benefit and an interest-sensitive accumulation/cash-value component. A guaranteed minimum rate may apply while the insurer may credit a higher current rate."},
]

QUESTIONS = [
    {"q":"A term policy can be changed to an eligible permanent policy during a stated period without new evidence of insurability. What feature is this?","choices":["Convertibility","Decreasing term","Extended term","ADB"],"answer":0,"why":"Convertible term permits conversion to permanent coverage without proving insurability again, subject to contract rules."},
    {"q":"Which term insurance is commonly matched to a debt whose balance declines over time?","choices":["Decreasing term","Level term","Joint life","Endowment"],"answer":0,"why":"Decreasing term has a declining face amount and is commonly associated with declining obligations."},
    {"q":"A whole-life policyowner stops premiums but wants the original face amount to continue for as long as the cash value can purchase term coverage. Which nonforfeiture option fits?","choices":["Extended term","Reduced paid-up","Cash surrender","Policy loan"],"answer":0,"why":"Extended term generally keeps the original face amount as term insurance for a limited period."},
    {"q":"Which term means the insured's current age as of a particular date?","choices":["Attained age","Issue age only","Maturity age","Benefit age"],"answer":0,"why":"Attained age means current age as of the specified date."},
    {"q":"Which permanent policy is especially associated with flexible premiums, adjustable death benefits, and interest-sensitive cash accumulation?","choices":["Universal life","Decreasing term","Joint life","Accidental death only"],"answer":0,"why":"Universal life is designed around premium/death-benefit flexibility and an interest-sensitive accumulation account."},
    {"q":"A single policy covers two spouses and pays when the first spouse dies, after which the policy ends. What is it?","choices":["Joint life","Survivorship life","Family income only","Convertible term"],"answer":0,"why":"Joint life is first-to-die coverage; survivorship life pays after the second insured dies."},
    {"q":"What is cash surrender value?","choices":["The cash amount available when a cash-value policy is surrendered, after applicable adjustments","The policy's gross death benefit in every case","The amount of every premium ever paid","A guaranteed accidental-death payment"],"answer":0,"why":"Cash surrender value is the amount available to the owner upon surrender, subject to contract adjustments."},
    {"q":"Which contract is designed to pay its face amount if the insured survives to a stated date or age, while also paying upon earlier death?","choices":["Endowment contract","Decreasing term","ADB only","Extended term"],"answer":0,"why":"An endowment combines a maturity benefit at a stated date/age with a death benefit before that date."},
]

LIGHTNING = [
    ("Accident + death/dismemberment-type loss", "ADB"),
    ("Current age", "Attained age"),
    ("Cash available on surrender", "Cash surrender value"),
    ("Term -> permanent without new insurability", "Convertible term"),
    ("Face amount declines", "Decreasing term"),
    ("Pays at stated maturity or earlier death", "Endowment"),
    ("Same face amount continues temporarily after surrender/nonforfeiture election", "Extended term"),
    ("Whole life + decreasing term income design", "Family income policy"),
    ("Pays at first death of multiple insureds", "Joint life"),
    ("Flexible premium + adjustable death benefit + interest-sensitive accumulation", "Universal life"),
]
