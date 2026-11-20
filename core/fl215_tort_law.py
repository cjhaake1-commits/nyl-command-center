from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Tort — definition","back":"A tort is a private or civil wrong, independent of contract, in which one party's conduct causes harm to another."},
    {"front":"Contract law vs tort law","back":"Contract law governs agreements; tort law governs civil wrongs and resulting harm that are independent of contracts."},
    {"front":"Civil vs criminal","back":"Torts are generally handled in civil courts; crimes are offenses against society handled in criminal courts."},
    {"front":"Purpose of tort law","back":"To provide a remedy, often money damages, to a person harmed by another's wrongful conduct."},
    {"front":"Simple negligence","back":"Failure to act, or failure to refrain from acting, as a reasonable and prudent person would."},
    {"front":"Gross negligence","back":"Reckless disregard for the need to act reasonably, with substantial indifference to possible harm."},
    {"front":"Willful and wanton negligence","back":"Reckless disregard of reasonable care while aware that bodily injury or property damage will probably occur; it approaches intentional misconduct."},
    {"front":"Insurance professional tort exposure","back":"Insurance professionals may face tort claims when they fail to meet professional obligations and cause harm."},
]

QUESTIONS = [
    {"q":"A private wrong that is independent of a contract is called a:","choices":["Tort","Warranty","Binder","Waiver"],"answer":0,"why":"Tort law addresses civil wrongs independent of contractual obligations."},
    {"q":"Which branch of law generally governs disputes over the terms of an insurance policy itself?","choices":["Contract law","Tort law","Criminal law","Administrative law only"],"answer":0,"why":"The insurance agreement and its enforceable terms are governed by contract law."},
    {"q":"Which court system generally handles tort claims?","choices":["Civil courts","Criminal courts only","Bankruptcy courts only","Tax courts"],"answer":0,"why":"Torts are civil wrongs and are ordinarily resolved in civil court."},
    {"q":"An agent simply forgets to submit a client's application. This most closely illustrates:","choices":["Simple negligence","Gross negligence","Willful and wanton negligence","Subrogation"],"answer":0,"why":"A one-time failure to use reasonable care is classic simple negligence."},
    {"q":"An agent repeatedly and recklessly fails to maintain required client records. This most closely illustrates:","choices":["Gross negligence","Simple negligence","Parole evidence","Waiver"],"answer":0,"why":"Gross negligence involves reckless disregard for reasonable care."},
    {"q":"An agent knowingly processes a fraudulent claim despite understanding that serious harm is likely. This most closely illustrates:","choices":["Willful and wanton negligence","Simple negligence","Implied authority","Subrogation"],"answer":0,"why":"Willful and wanton negligence involves conscious or reckless disregard of a high probability of harm."},
    {"q":"What is a primary purpose of tort law?","choices":["To compensate persons harmed by another's wrongful conduct","To rewrite all insurance contracts","To create agent appointments","To regulate stock exchanges"],"answer":0,"why":"Tort law is designed to remedy civil wrongs, often through monetary damages."},
    {"q":"Which statement best distinguishes tort law from criminal law?","choices":["Tort law addresses private civil wrongs; criminal law addresses offenses against society","Tort law applies only to insurers; criminal law applies only to agents","Tort law has no remedies; criminal law always pays damages","They are the same body of law"],"answer":0,"why":"The key distinction is private civil wrong versus offense against society."},
]

SCENARIO_DRILLS = [
    {"scenario":"A producer accidentally fails to forward an application on time, causing the client to lose a coverage opportunity.","answer":"Simple negligence","why":"The conduct reflects a failure to use reasonable care rather than reckless or intentional misconduct."},
    {"scenario":"A producer repeatedly ignores required recordkeeping procedures despite prior warnings and creates foreseeable client harm.","answer":"Gross negligence","why":"Repeated reckless disregard for a known duty points to gross negligence."},
    {"scenario":"A producer knowingly participates in processing a fraudulent claim while aware that serious financial harm will probably result.","answer":"Willful and wanton negligence","why":"The conduct reflects conscious disregard of a likely harmful result and borders on intentional wrongdoing."},
    {"scenario":"Two parties dispute whether a written policy exclusion applies to a claim.","answer":"Primarily contract law","why":"A dispute over the meaning and enforceability of policy terms arises from the insurance contract."},
]

LIGHTNING = [
    ("Private civil wrong", "Tort"),
    ("Governs insurance agreement terms", "Contract law"),
    ("Handled in civil court", "Tort"),
    ("Failure to use reasonable care", "Simple negligence"),
    ("Reckless disregard for reasonable care", "Gross negligence"),
    ("Aware serious harm will probably occur", "Willful and wanton negligence"),
    ("Money remedy for civil harm", "Tort law"),
]
