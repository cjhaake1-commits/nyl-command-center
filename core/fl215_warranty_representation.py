from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Warranty","back":"A statement guaranteed to be true and treated as part of the contract. A warranty is held to a stricter standard than a representation."},
    {"front":"Representation","back":"A statement made by the applicant that is believed true to the best of the applicant's knowledge. In life and health insurance, application statements are generally treated as representations rather than warranties."},
    {"front":"Material misrepresentation","back":"A false statement that would influence the insurer's decision to accept the risk, classify the risk, or determine the premium."},
    {"front":"Concealment","back":"Failure or neglect by an applicant to disclose a known material fact when applying for insurance."},
    {"front":"Misrepresentation vs concealment","back":"Misrepresentation = applicant says something materially false. Concealment = applicant omits or fails to disclose a known material fact."},
    {"front":"Materiality","back":"A fact is material if knowing it would have changed the insurer's decision to issue the policy, classify the risk, price the policy, or issue it on the same terms."},
    {"front":"Rescission","back":"Cancellation of the contract back to its beginning so it is treated as null and void, subject to applicable law and policy provisions."},
    {"front":"Contestable period concept","back":"Insurers generally have a limited period after policy issue to challenge certain application misrepresentations or concealment; exact Florida rules and exceptions should be learned from current official material."},
    {"front":"Warranty vs representation","back":"Warranty = exact/strict truth standard and contractual in nature. Representation = substantially true when made; consequences generally depend on materiality."},
    {"front":"Life/health application statements","back":"Typically representations, not warranties. The insurer focuses on whether any false statement or omission was material to underwriting."},
    {"front":"Materiality memory cue","back":"Material = it matters to the underwriting decision."},
]

QUESTIONS = [
    {"q":"In life and health insurance, statements made by an applicant on the application are generally considered:","choices":["Representations","Warranties","Binders","Riders"],"answer":0,"why":"Life and health applications generally treat applicant statements as representations rather than strict warranties."},
    {"q":"Which statement best describes a warranty?","choices":["A statement guaranteed to be true and treated as part of the contract","A statement that only needs to be approximately true","A producer opinion","A policy dividend"],"answer":0,"why":"A warranty is held to a strict truth standard and is contractual in nature."},
    {"q":"A false application statement would most likely be considered material if it:","choices":["Would influence underwriting, classification, or premium","Contains a spelling error","Has no effect on the risk","Was corrected before submission"],"answer":0,"why":"Materiality depends on whether the information could affect the insurer's underwriting decision."},
    {"q":"Which is the best distinction between a representation and a warranty?","choices":["A representation generally must be substantially true when made; a warranty is subject to a stricter exact-truth standard","Representations are always written by insurers","Warranties apply only to beneficiaries","There is no difference"],"answer":0,"why":"Representations are generally judged by material truthfulness, while warranties are stricter contractual statements."},
    {"q":"An applicant gives inaccurate information that would have caused the insurer to charge a different premium. This is most likely:","choices":["A material misrepresentation","A waiver","An adhesion issue","A unilateral promise"],"answer":0,"why":"If the false statement affects pricing or classification, it is material to underwriting."},
    {"q":"An applicant knows about a recent serious medical diagnosis but omits it when specifically asked about medical history. This is most directly an example of:","choices":["Concealment","Waiver","Adhesion","Reinsurance"],"answer":0,"why":"Concealment is the failure to disclose a known material fact."},
    {"q":"Which choice best distinguishes concealment from misrepresentation?","choices":["Concealment is an omission; misrepresentation is a false statement","Concealment is always accidental; misrepresentation is always intentional","Concealment applies only to insurers","There is no difference"],"answer":0,"why":"The key distinction is omission versus a materially false statement."},
    {"q":"A fact is material when:","choices":["It would affect whether or how the insurer issues or prices the coverage","It appears anywhere on the application","It is interesting to the producer","It has no effect on underwriting"],"answer":0,"why":"Materiality is tied to the insurer's underwriting decision and policy terms."},
    {"q":"Rescission means:","choices":["Treating the contract as null and void from the beginning, subject to law","Adding a rider","Changing a beneficiary","Reinstating a lapsed policy"],"answer":0,"why":"Rescission unwinds the contract and treats it as though it had not been in force, subject to applicable rules."},
]

LIGHTNING = [
    ("Guaranteed true; strict standard", "Warranty"),
    ("Applicant statement; substantially true when made", "Representation"),
    ("False statement affecting underwriting", "Material misrepresentation"),
    ("Known material fact omitted", "Concealment"),
    ("Omission", "Concealment"),
    ("False statement", "Misrepresentation"),
    ("Would change issue/classification/price", "Materiality"),
    ("Contract unwound/null from start", "Rescission"),
    ("Life/health application statement", "Representation"),
]
