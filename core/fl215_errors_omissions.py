from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Errors & Omissions (E&O) insurance","back":"Professional liability coverage that helps protect insurance professionals against liability arising from mistakes, negligence, or failures in professional services."},
    {"front":"What can E&O pay for?","back":"Defense costs and covered damages arising from an insurance professional's negligent acts, errors, or omissions."},
    {"front":"Failure to place requested coverage","back":"A classic E&O exposure: the client requests coverage or a policy change, but the producer fails to put it into effect."},
    {"front":"Misstating coverage","back":"Incorrectly describing policy coverage can create professional liability and may trigger an E&O claim."},
    {"front":"Administrative or processing mistakes","back":"Errors involving applications, e-signatures, authorizations, premium calculations, or policy changes can create E&O exposure."},
    {"front":"Failure to explain policy provisions","back":"A producer may face E&O exposure when inadequate explanation of important policy terms causes client harm."},
    {"front":"Failure to identify client loss exposures","back":"Missing a material exposure or failing to recommend appropriate coverage may lead to professional liability."},
    {"front":"Inaccurate information sent to carrier","back":"Forwarding incomplete or inaccurate client information to an insurer can create E&O exposure."},
    {"front":"Improper claim handling","back":"Professional errors in handling or communicating about a claim may be an E&O exposure, depending on the role and policy."},
    {"front":"Intentional acts and liability insurance","back":"Intentional harm is excluded from liability coverage; intentional criminal, illegal, dishonest, malicious, or deliberate unlawful conduct is not protected as an accidental professional error."},
    {"front":"Simple negligence vs. E&O","back":"Simple negligence is an unintentional failure to act reasonably, such as a missed deadline or filing error; it is the type most commonly associated with E&O coverage."},
    {"front":"Gross negligence vs. E&O","back":"Gross negligence involves reckless or serious disregard for reasonable care. Coverage may be limited or depend on policy terms and facts."},
    {"front":"Willful and wanton conduct vs. E&O","back":"Conscious or intentional disregard of known risk approaches deliberate misconduct and is generally outside E&O protection."},
]

QUESTIONS = [
    {"q":"What type of insurance is designed to protect an insurance producer from liability arising from professional mistakes?","choices":["Errors and omissions insurance","Workers compensation","Commercial auto","Inland marine"],"answer":0,"why":"E&O is professional liability coverage for mistakes, negligence, or failures in professional services."},
    {"q":"A client asks an agent to add a coverage endorsement, but the agent forgets and a covered-type loss later occurs. Which policy is most relevant to the agent's professional liability?","choices":["Errors and omissions insurance","Life insurance","Flood insurance only","Surety bond only"],"answer":0,"why":"Failure to implement a requested coverage change is a common E&O exposure."},
    {"q":"Which expense is commonly associated with E&O coverage?","choices":["Legal defense costs","Routine office rent","Employee vacation pay","Advertising expenses"],"answer":0,"why":"E&O coverage can pay defense costs and covered damages arising from professional negligence."},
    {"q":"An agent miscalculates a client's premium and the error causes financial harm. This is best classified as:","choices":["A potential E&O exposure","A subrogation recovery","A criminal sentence","A valued contract"],"answer":0,"why":"Premium calculation mistakes are professional errors that can create E&O liability."},
    {"q":"An agent incorrectly tells a client that a policy covers a loss that it actually excludes. This can create:","choices":["E&O exposure","Automatic subrogation","A reciprocal insurer","A stock dividend"],"answer":0,"why":"Misstating insurance coverage is a common source of professional liability claims."},
    {"q":"Which situation is LEAST likely to be an E&O exposure?","choices":["The agent's office printer breaks","The agent fails to submit a requested policy change","The agent forwards incomplete client information to the carrier","The agent fails to explain an important exclusion"],"answer":0,"why":"A broken office printer is generally an ordinary business expense, not a professional liability error affecting the client."},
    {"q":"A producer fails to recognize an obvious liability exposure and therefore recommends insufficient coverage. This may create:","choices":["E&O liability","A parole evidence issue only","Subrogation rights for the producer","A criminal conviction automatically"],"answer":0,"why":"Failure to identify client loss exposures or recommend appropriate coverage is a recognized E&O risk."},
    {"q":"The core purpose of E&O coverage is to help a professional manage which type of risk?","choices":["Professional liability risk","Investment market risk","Property depreciation only","Mortality risk"],"answer":0,"why":"E&O is professional liability insurance designed around negligent errors and omissions in professional services."},
    {"q":"Which conduct is most clearly outside the purpose of E&O coverage?","choices":["Deliberate dishonest misconduct","An accidental filing error","A missed deadline","An unintentional processing mistake"],"answer":0,"why":"E&O is designed for professional errors and negligence, not deliberate dishonest or intentional misconduct."},
    {"q":"An agent accidentally misses a filing deadline despite normally following reasonable procedures. This most closely illustrates:","choices":["Simple negligence","Willful misconduct","Intentional fraud","Malicious conduct"],"answer":0,"why":"An unintentional failure to use reasonable care is simple negligence and is commonly associated with E&O exposure."},
    {"q":"Which negligence level involves reckless disregard rather than an ordinary inadvertent mistake?","choices":["Gross negligence","Simple negligence","No negligence","Strict contract performance"],"answer":0,"why":"Gross negligence reflects serious or reckless disregard for reasonable care."},
    {"q":"An agent knowingly commits deliberate misconduct despite understanding the likely harm. For E&O purposes this is closest to:","choices":["Willful and wanton conduct","Simple negligence","An innocent clerical error","Ordinary reasonable care"],"answer":0,"why":"Conscious disregard and deliberate misconduct move beyond ordinary negligence and are generally not protected as accidental E&O losses."},
]

SCENARIO_DRILLS = [
    {"scenario":"A homeowner asks the producer to add an endorsement. The producer confirms the request but never processes it, and a loss later occurs that the endorsement would have addressed.","answer":"Potential E&O claim","why":"The producer failed to put requested coverage into effect, a classic omission."},
    {"scenario":"A producer enters the wrong premium amount during processing, causing the client financial harm.","answer":"Potential E&O claim","why":"A premium calculation or administrative error can create professional liability."},
    {"scenario":"A producer tells a client that an exclusion does not apply when the written policy clearly says it does, and the client suffers a loss after relying on that advice.","answer":"Potential E&O claim","why":"Misstating coverage or failing to explain policy provisions can create professional liability."},
    {"scenario":"A producer notices a major client exposure but never discusses it or recommends any suitable coverage, and the uncovered loss later occurs.","answer":"Potential E&O claim","why":"Failure to identify an exposure or recommend coverage can be an omission in professional services."},
    {"scenario":"A producer makes an accidental filing mistake while attempting to process a client's request correctly.","answer":"Simple negligence / potential E&O exposure","why":"The conduct is unintentional and fits the ordinary negligence category E&O is intended to address."},
    {"scenario":"A producer repeatedly ignores required recordkeeping despite warnings and creates a serious client loss.","answer":"Possible gross negligence","why":"Repeated reckless disregard is more serious than a single inadvertent mistake; coverage can depend on policy language and facts."},
    {"scenario":"A producer knowingly falsifies information to obtain a result and understands that the conduct violates the rules.","answer":"Intentional misconduct — generally not E&O-covered","why":"Deliberate dishonest or unlawful conduct is not the accidental professional negligence E&O is designed to insure."},
]

LIGHTNING = [
    ("Professional liability for agents", "E&O insurance"),
    ("Defense costs for negligence claim", "E&O"),
    ("Fail to add requested coverage", "Omission / E&O exposure"),
    ("Wrong premium calculation", "Error / E&O exposure"),
    ("Misstate policy coverage", "E&O exposure"),
    ("Fail to explain provisions", "E&O exposure"),
    ("Forward incomplete client info", "E&O exposure"),
    ("Fail to recommend coverage", "E&O exposure"),
    ("Accidental missed deadline", "Simple negligence — usually E&O territory"),
    ("Reckless disregard", "Gross negligence"),
    ("Conscious deliberate misconduct", "Willful/wanton — generally excluded"),
    ("Criminal/dishonest/malicious intentional act", "Liability/E&O exclusion"),
]
