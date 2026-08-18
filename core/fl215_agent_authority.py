from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Agent authority — three types","back":"Express, implied, and apparent authority."},
    {"front":"Express authority","back":"Authority deliberately granted by the principal to the agent, usually stated in the agency/appointment contract. Think: specifically written or directly stated authority."},
    {"front":"Implied authority","back":"Authority not expressly written but reasonably necessary or incidental to carry out the agent's express authority and transact the principal's business."},
    {"front":"Apparent authority","back":"Authority a third party reasonably believes the agent has because of the principal's words, conduct, materials, tools, or representations, even if the authority was not actually granted in the agency contract."},
    {"front":"Principal in insurance agency law","back":"The insurer is the principal; the agent acts on the insurer's behalf within the scope of authority granted."},
    {"front":"Express vs implied","back":"Express = directly granted/stated. Implied = unwritten but reasonably necessary to perform express duties."},
    {"front":"Apparent authority — source","back":"Apparent authority comes from the principal's actions or representations to the public, not merely from the agent's own claim of authority."},
    {"front":"Apparent authority memory cue","back":"Apparent = what the customer reasonably thinks the agent can do because of the insurer's conduct."},
    {"front":"Express authority memory cue","back":"Express = specifically written or directly granted."},
    {"front":"Implied authority memory cue","back":"Implied = necessary to do the job."},
    {"front":"Authority and insurer liability","back":"When an agent acts within actual or apparent authority, the insurer may be bound by the agent's acts, subject to applicable law and facts."},
    {"front":"All three can coexist","back":"A single agent can simultaneously have express authority for stated duties, implied authority for necessary incidental acts, and apparent authority created by the insurer's public-facing conduct."},
]

QUESTIONS = [
    {"q":"An agent's written appointment specifically authorizes the agent to solicit applications. This is:","choices":["Express authority","Implied authority","Apparent authority","No authority"],"answer":0,"why":"Express authority is deliberately and specifically granted by the principal, often in writing."},
    {"q":"An agent is authorized to solicit applications and uses ordinary administrative steps reasonably necessary to complete that task, even though those steps are not listed in the contract. This is:","choices":["Implied authority","Express authority","Apparent authority","Estoppel"],"answer":0,"why":"Implied authority covers acts reasonably necessary or incidental to carrying out express authority."},
    {"q":"A customer reasonably believes an agent has authority because the insurer presented the person as its representative. Which authority is most relevant?","choices":["Apparent authority","Express authority","Implied authority","No authority"],"answer":0,"why":"Apparent authority arises from the principal's manifestations to third parties."},
    {"q":"Which statement best distinguishes express and implied authority?","choices":["Express is specifically granted; implied is reasonably necessary to carry out express duties","Express is created only by customers; implied is always written","Express is never written; implied is always written","There is no difference"],"answer":0,"why":"Express authority is directly granted, while implied authority flows from what is reasonably necessary to perform granted duties."},
    {"q":"In insurance agency law, the principal is generally the:","choices":["Insurer","Applicant","Beneficiary","Broker's client"],"answer":0,"why":"The insurer is the principal when an agent is acting on the insurer's behalf."},
    {"q":"Which authority depends most heavily on what a reasonable third party believes based on the insurer's conduct?","choices":["Apparent authority","Express authority","Implied authority","Aleatory authority"],"answer":0,"why":"Apparent authority is based on the principal's outward manifestations to third parties."},
    {"q":"An insurer gives a person an official company email address, access to quoting tools, and branded business cards. A customer reasonably concludes that person is authorized to act for the insurer. This best illustrates:","choices":["Apparent authority","Implied authority","Express authority","Concealment"],"answer":0,"why":"The insurer's conduct created the appearance of authority to a reasonable customer."},
    {"q":"An agent independently claims to have authority, but the insurer did nothing to create that impression. Which statement is most accurate?","choices":["The agent's claim alone generally does not create apparent authority","Apparent authority automatically exists","The agent has express authority","The insurer is always bound"],"answer":0,"why":"Apparent authority generally must be traceable to the principal's manifestations, not just the agent's unsupported assertion."},
    {"q":"A contract says an agent may sell policies. The agent orders ordinary office supplies needed to conduct that authorized business, although the contract does not mention supplies. This is most likely:","choices":["Implied authority","Apparent authority","Express authority","No authority"],"answer":0,"why":"Ordering ordinary supplies can be incidental to carrying out an expressly authorized business role."},
    {"q":"Which exam shortcut is correct?","choices":["Express = written/specified; implied = necessary to do the job; apparent = reasonable public appearance created by the insurer","Express = public appearance; implied = written; apparent = necessary","All three mean exactly the same thing","Apparent authority is always written"],"answer":0,"why":"That is the key licensing-exam distinction among the three authority types."},
    {"q":"Can one agent have express, implied, and apparent authority at the same time?","choices":["Yes","No, only one type can exist at once","Only express and implied can coexist","Only apparent authority can exist"],"answer":0,"why":"Different acts and circumstances can support different authority types simultaneously."},
]

SCENARIO_DRILLS = [
    {"scenario":"The agency contract explicitly says Maria may sell life insurance policies.","answer":"Express authority","why":"The authority is specifically granted in the contract."},
    {"scenario":"Maria uses routine office systems and supplies needed to perform her authorized sales duties, though those details are not written in her contract.","answer":"Implied authority","why":"These are incidental acts reasonably necessary to do the authorized job."},
    {"scenario":"The insurer gives Maria a company email address, branded business cards, and access to customer-facing quoting tools, leading customers to reasonably believe she can act for the company.","answer":"Apparent authority","why":"The appearance of authority comes from the insurer's conduct."},
]

LIGHTNING = [
    ("Specifically granted in agency contract", "Express authority"),
    ("Unwritten but necessary to perform granted duties", "Implied authority"),
    ("Customer reasonably believes authority exists because of insurer conduct", "Apparent authority"),
    ("Company-created appearance", "Apparent authority"),
    ("Necessary to do the job", "Implied authority"),
    ("Specifically written", "Express authority"),
    ("Insurance company in agency relationship", "Principal"),
]
