from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Aleatory contract","back":"Depends on an uncertain future event and may involve an unequal exchange: a small premium can produce a much larger covered benefit."},
    {"front":"Contract of adhesion","back":"The insurer drafts the standard contract; the applicant generally accepts or rejects it rather than negotiating its wording."},
    {"front":"Unilateral contract","back":"Only the insurer makes a legally enforceable promise to perform. The policyowner is not forced to keep paying premiums, but coverage can lapse or terminate if required premiums are not paid."},
    {"front":"Personal contract","back":"Property and casualty insurance generally insures the person or entity's interest in property rather than the property itself, so the policy normally cannot simply be transferred to a new owner without insurer consent."},
    {"front":"Life insurance transfer exception","back":"Life insurance ownership rights can generally be transferred through assignment, subject to policy terms and applicable law."},
    {"front":"Conditional contract","back":"The insurer's duty to perform depends on the insured satisfying policy conditions, such as timely premium payment, notice/proof of loss, and other required acts."},
    {"front":"Ambiguity in an adhesion contract","back":"Genuinely ambiguous policy language is generally construed against the drafter and in favor of the policyholder/insured."},
    {"front":"Doctrine of reasonable expectations","back":"Focuses on the objectively reasonable coverage understanding of the consumer when wording or representations create a reasonable expectation of coverage."},
    {"front":"Valued contract","back":"Pays a predetermined stated amount for a covered event rather than measuring the exact economic loss at claim time. Life insurance and many AD&D benefits are examples."},
    {"front":"Indemnity contract","back":"Seeks to restore the insured financially to approximately the position held before the covered loss, subject to policy limits, deductibles, coinsurance, and other terms."},
    {"front":"Reimbursement policy","back":"A form of indemnity coverage that pays covered expenses actually incurred, subject to the policy's cost-sharing and limits."},
    {"front":"Valued vs. indemnity","back":"Valued = stated benefit. Indemnity = measured covered economic loss/expense."},
]

QUESTIONS = [
    {"q":"Why is an insurance contract described as aleatory?","choices":["The values exchanged can be unequal depending on an uncertain event","Both parties negotiate every clause","The insurer has no obligations","Premiums are always refunded"],"answer":0,"why":"Aleatory contracts involve uncertain events and potentially unequal exchanges of value."},
    {"q":"An insurer drafts a standard policy and the applicant accepts it without negotiating its wording. This illustrates:","choices":["Adhesion","Indemnity","Subrogation","Contribution"],"answer":0,"why":"A contract of adhesion is drafted by one party and offered on standardized terms."},
    {"q":"Which characteristic means only the insurer makes the enforceable promise to pay if policy conditions are satisfied?","choices":["Unilateral","Aleatory","Personal","Commutative"],"answer":0,"why":"Insurance is unilateral because the insurer promises performance; the policyowner is not legally compelled to continue premiums."},
    {"q":"A policy requires timely notice and proof of a covered loss before benefits are payable. Which characteristic is illustrated?","choices":["Conditional","Personal","Aleatory","Valued"],"answer":0,"why":"The insurer's obligation depends on specified policy conditions being met."},
    {"q":"A homeowner sells a house. Why does the buyer not automatically receive the seller's homeowners policy?","choices":["Property insurance is generally a personal contract tied to the insured's interest and underwriting","All insurance is nontransferable by law","The policy is aleatory","The policy is a valued contract"],"answer":0,"why":"Property insurance generally protects the insured person's interest and cannot simply follow the property to a new owner."},
    {"q":"Which statement best distinguishes valued and indemnity contracts?","choices":["Valued pays a stated benefit; indemnity measures covered economic loss","Valued policies have no premium; indemnity policies do","Only indemnity policies are legal","Valued contracts always reimburse receipts"],"answer":0,"why":"Valued contracts use a predetermined benefit, while indemnity contracts compensate measured covered loss or expense."},
    {"q":"A life policy has a $500,000 death benefit. The insured dies and the covered claim is payable. The benefit is not recalculated from the family's exact financial loss at death. This is primarily an example of:","choices":["A valued contract","An indemnity contract","A reimbursement contract","A void contract"],"answer":0,"why":"Life insurance generally pays the stated contractual death benefit rather than calculating the exact loss at death."},
    {"q":"A covered medical expense is $25,000 and a reimbursement policy pays covered expenses actually incurred, subject to its terms. This is an example of:","choices":["Indemnity/reimbursement","Valued life insurance","Aleatory-only coverage","A contract of adhesion only"],"answer":0,"why":"Reimbursement coverage is a form of indemnity because payment is based on covered expenses actually incurred."},
    {"q":"If a policy term is genuinely ambiguous, a court will generally interpret the ambiguity:","choices":["Against the drafter and in favor of the policyholder","Always in favor of the insurer","Against both parties equally","According to the producer's commission agreement"],"answer":0,"why":"Because the insurer drafted the adhesion contract, ambiguities are generally construed against the drafter."},
    {"q":"The doctrine of reasonable expectations is most concerned with:","choices":["The objectively reasonable coverage understanding of the consumer","The insurer's investment return","The producer's compensation","The state's premium tax rate"],"answer":0,"why":"The doctrine focuses on the consumer's objectively reasonable understanding of coverage."},
]

LIGHTNING = [
    ("Unequal exchange + uncertain event", "Aleatory"),
    ("Insurer writes it; take it or leave it", "Adhesion"),
    ("Only insurer makes enforceable promise", "Unilateral"),
    ("Policy tied to insured person's interest", "Personal"),
    ("Duties depend on required acts/conditions", "Conditional"),
    ("Predetermined benefit", "Valued"),
    ("Restore measured covered loss", "Indemnity"),
    ("Pays covered expenses actually incurred", "Reimbursement"),
    ("Unclear wording construed against drafter", "Ambiguity rule"),
    ("Objective consumer understanding", "Reasonable expectations"),
]
