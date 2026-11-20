from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Subrogation — definition","back":"After paying a covered claim, an insurer may step into the insured's shoes and pursue the party responsible for the loss to recover what it paid."},
    {"front":"Subrogation — memory cue","back":"Insurer pays first, then pursues the at-fault party."},
    {"front":"Who usually seeks recovery in subrogation?","back":"The insurer that paid its insured's covered claim."},
    {"front":"Who is pursued in subrogation?","back":"The person or entity responsible for causing the insured's loss, often through that party's insurer."},
    {"front":"Why subrogation matters","back":"It helps insurers recover claim payments from responsible parties and prevents the wrongdoer from escaping financial responsibility."},
    {"front":"Subrogation phrase to remember","back":"'Step into the insured's shoes.'"},
]

QUESTIONS = [
    {"q":"An insurer pays its policyholder for a covered auto loss caused by another driver and then seeks reimbursement from the at-fault driver's insurer. This is:","choices":["Subrogation","Estoppel","Waiver","Concealment"],"answer":0,"why":"Subrogation allows the paying insurer to pursue the responsible party after compensating its insured."},
    {"q":"The phrase 'stepping into the insured's shoes' most directly describes:","choices":["Subrogation","Indemnity","Apparent authority","Parole evidence"],"answer":0,"why":"That phrase is a classic way to remember subrogation."},
    {"q":"What typically happens first in a subrogation situation?","choices":["The insured's insurer pays the covered claim","The responsible party pays the insurer","The insurer cancels the policy","The agent waives a policy condition"],"answer":0,"why":"Subrogation generally follows payment of the insured's covered claim."},
    {"q":"After paying a covered loss, an insurer seeks recovery from the party that caused the loss. What right is the insurer exercising?","choices":["Subrogation","Rescission","Waiver","Concealment"],"answer":0,"why":"The insurer is asserting the insured's recovery rights against the responsible party."},
    {"q":"Which statement best describes the purpose of subrogation?","choices":["To allow an insurer to recover claim payments from a responsible third party","To make oral promises override written policies","To let a producer bind any insurer","To eliminate the need for premiums"],"answer":0,"why":"Subrogation shifts the ultimate cost of a loss toward the party responsible for causing it."},
]

SCENARIO_DRILLS = [
    {"scenario":"A driver's car is damaged by another motorist. The driver's own insurer pays $5,000 for repairs, then pursues the at-fault driver's insurer for reimbursement.","answer":"Subrogation","why":"The insurer paid its insured and then stepped into the insured's shoes to recover from the responsible party."},
    {"scenario":"An insurer has not yet paid its insured but is evaluating whether a loss is covered.","answer":"Not yet subrogation","why":"Subrogation normally becomes relevant after the insurer has paid a covered claim and then seeks recovery."},
    {"scenario":"An insured receives a covered claim payment, and the insurer later seeks repayment from a negligent third party.","answer":"Subrogation","why":"That is the classic sequence: claim payment first, recovery action second."},
]

LIGHTNING = [
    ("Pays insured, then pursues wrongdoer", "Subrogation"),
    ("Step into insured's shoes", "Subrogation"),
    ("Recovery from at-fault party", "Subrogation"),
    ("Responsible party's insurer may reimburse", "Subrogation"),
]
