from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Aleatory contract","back":"A contract involving an uncertain future event and potentially unequal exchange of value. In insurance, a relatively small premium can result in a much larger covered benefit."},
    {"front":"Contract of adhesion","back":"A contract drafted by one party, typically the insurer, and offered on a take-it-or-leave-it basis without negotiation of standard terms."},
    {"front":"Ambiguity in an adhesion contract","back":"When policy language is genuinely ambiguous, courts generally construe the ambiguity against the drafter and in favor of the policyholder/insured."},
    {"front":"Doctrine of reasonable expectations","back":"Courts may protect the objectively reasonable expectations of the consumer when policy wording or representations create a reasonable understanding of coverage that conflicts with obscure or misleading language."},
    {"front":"Why adhesion matters","back":"Because the insurer drafts the policy language, it bears responsibility for clarity. This is why ambiguous wording is commonly interpreted against the insurer."},
    {"front":"Aleatory memory cue","back":"Aleatory = unequal exchange depending on a what-if event."},
    {"front":"Adhesion memory cue","back":"Adhesion = insurer writes it; applicant takes it or leaves it."},
    {"front":"Reasonable expectations memory cue","back":"What would a reasonable consumer objectively expect the policy to provide based on the contract and representations?"},
]

QUESTIONS = [
    {"q":"Why is an insurance contract described as aleatory?","choices":["Because the values exchanged can be unequal depending on an uncertain event","Because both parties negotiate every clause","Because the insurer has no obligations","Because premiums are always refunded"],"answer":0,"why":"Aleatory contracts involve uncertain events and potentially unequal exchanges of value."},
    {"q":"An insurance contract drafted by the insurer and offered on a take-it-or-leave-it basis is a contract of:","choices":["Adhesion","Indemnity","Subrogation","Contribution"],"answer":0,"why":"Adhesion means one party drafts the standard contract and the other accepts or rejects it."},
    {"q":"If a policy term is genuinely ambiguous, a court will generally interpret the ambiguity:","choices":["Against the drafter and in favor of the policyholder","Always in favor of the insurer","Against both parties equally","Only according to the producer's commission agreement"],"answer":0,"why":"Because the insurer drafted the adhesion contract, ambiguities are generally construed against the drafter."},
    {"q":"The doctrine of reasonable expectations is most concerned with:","choices":["The objectively reasonable coverage understanding of the consumer","The insurer's investment return","The producer's compensation","The state's premium tax rate"],"answer":0,"why":"The doctrine focuses on what a reasonable consumer would understand or expect from the policy and related representations."},
    {"q":"Which phrase best describes a contract of adhesion?","choices":["Take it or leave it","Equal negotiation","Guaranteed profit","No legal obligations"],"answer":0,"why":"Insurance contracts are standardized and drafted by the insurer rather than jointly negotiated."},
    {"q":"A policyowner pays a modest premium and later receives a large covered death benefit. Which contract characteristic does this illustrate?","choices":["Aleatory","Commutative","Bilateral","Void"],"answer":0,"why":"The unequal exchange caused by an uncertain covered event illustrates the aleatory nature of insurance."},
]

LIGHTNING = [
    ("Unequal exchange; uncertain event", "Aleatory"),
    ("Take it or leave it; insurer drafted", "Adhesion"),
    ("Unclear wording construed against drafter", "Ambiguity rule"),
    ("Objective consumer understanding of promised coverage", "Reasonable expectations"),
]
