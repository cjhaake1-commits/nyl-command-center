from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Warranty","back":"A statement guaranteed to be true and treated as part of the contract. A warranty is held to a stricter standard than a representation."},
    {"front":"Representation","back":"A statement made by the applicant that is believed true to the best of the applicant's knowledge. In life and health insurance, application statements are generally treated as representations rather than warranties."},
    {"front":"Material misrepresentation","back":"A false statement that would influence the insurer's decision to accept the risk, classify the risk, or determine the premium."},
    {"front":"Warranty vs representation","back":"Warranty = exact/strict truth standard and contractual in nature. Representation = substantially true when made; consequences generally depend on materiality."},
    {"front":"Life/health application statements","back":"Typically representations, not warranties. The insurer focuses on whether any false statement was material to underwriting."},
    {"front":"Materiality memory cue","back":"Material = it matters to the underwriting decision."},
]

QUESTIONS = [
    {"q":"In life and health insurance, statements made by an applicant on the application are generally considered:","choices":["Representations","Warranties","Binders","Riders"],"answer":0,"why":"Life and health applications generally treat applicant statements as representations rather than strict warranties."},
    {"q":"Which statement best describes a warranty?","choices":["A statement guaranteed to be true and treated as part of the contract","A statement that only needs to be approximately true","A producer opinion","A policy dividend"],"answer":0,"why":"A warranty is held to a strict truth standard and is contractual in nature."},
    {"q":"A false application statement would most likely be considered material if it:","choices":["Would influence underwriting, classification, or premium","Contains a spelling error","Has no effect on the risk","Was corrected before submission"],"answer":0,"why":"Materiality depends on whether the information could affect the insurer's underwriting decision."},
    {"q":"Which is the best distinction between a representation and a warranty?","choices":["A representation generally must be substantially true when made; a warranty is subject to a stricter exact-truth standard","Representations are always written by insurers","Warranties apply only to beneficiaries","There is no difference"],"answer":0,"why":"Representations are generally judged by material truthfulness, while warranties are stricter contractual statements."},
    {"q":"An applicant gives inaccurate information that would have caused the insurer to charge a different premium. This is most likely:","choices":["A material misrepresentation","A waiver","An adhesion issue","A unilateral promise"],"answer":0,"why":"If the false statement affects pricing or classification, it is material to underwriting."},
]

LIGHTNING = [
    ("Guaranteed true; strict standard", "Warranty"),
    ("Applicant statement; substantially true when made", "Representation"),
    ("False statement affecting underwriting", "Material misrepresentation"),
    ("Life/health application statement", "Representation"),
]
