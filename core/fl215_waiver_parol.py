from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Waiver","back":"The voluntary and intentional surrender of a known legal right. If an insurer knowingly gives up enforcement of a policy provision, it may be unable to rely on that provision later in the same matter."},
    {"front":"Parol evidence rule","back":"The final written insurance contract generally controls over prior oral statements or promises that contradict the written terms, subject to recognized legal exceptions."},
    {"front":"Policy changes","back":"Changes to policy terms generally must be made in writing through the proper policy amendment, rider, or endorsement process rather than by an informal oral promise."},
    {"front":"Waiver memory cue","back":"Waiver = knowingly give up a right."},
    {"front":"Parol memory cue","back":"Parol = prior spoken words generally cannot rewrite the final written contract."},
]

QUESTIONS = [
    {"q":"An insurer knowingly chooses not to enforce a policy provision and gives up that right. This is:","choices":["Waiver","Adhesion","Indemnity","Reinsurance"],"answer":0,"why":"Waiver is the voluntary surrender of a known right."},
    {"q":"A producer makes an oral promise before policy delivery that directly conflicts with the final written policy. Which doctrine generally gives priority to the final written contract?","choices":["Parol evidence rule","Aleatory doctrine","Subrogation","Risk retention"],"answer":0,"why":"The parol evidence rule generally prevents prior oral statements from altering an integrated written contract."},
    {"q":"Which is the best way to make a valid change to policy terms?","choices":["Use the insurer's proper written amendment, rider, or endorsement process","Rely on a verbal promise from a friend","Change the applicant's copy by hand without insurer approval","Ignore the written contract"],"answer":0,"why":"Policy changes generally require the insurer's authorized written process."},
    {"q":"Which phrase best describes waiver?","choices":["Voluntary surrender of a known right","Transfer of risk to another insurer","Uncertain unequal exchange","Failure to disclose a material fact"],"answer":0,"why":"Waiver means knowingly and voluntarily relinquishing a right."},
    {"q":"The parol evidence rule is most directly concerned with:","choices":["Prior oral statements that conflict with a final written contract","Insurer reserves","Policy dividends","Risk classification"],"answer":0,"why":"Its core purpose is to protect the integrity of the final written agreement."},
]

LIGHTNING = [
    ("Knowingly give up a right", "Waiver"),
    ("Prior oral promise cannot rewrite final policy", "Parol evidence rule"),
    ("Formal written policy change", "Rider/endorsement/amendment"),
]
