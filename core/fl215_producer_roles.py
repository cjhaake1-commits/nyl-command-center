from __future__ import annotations

# Original study drills distilled from user-provided XCEL screenshots.
# No proprietary exam questions are reproduced.

CARDS = [
    {"front":"Agent vs broker — who is represented?","back":"Agent represents the insurer. Broker represents the buyer/applicant/insured."},
    {"front":"Broker — basic role","back":"A broker solicits/accepts applications for a buyer and seeks to place coverage with an insurer."},
    {"front":"Can a broker bind coverage?","back":"Generally no. The broker must work with an authorized agent or insurer representative who can bind the insurer."},
    {"front":"Can an agent bind coverage?","back":"An appointed agent may have authority under the agent contract/appointment to bind the insurer, subject to the scope of that authority."},
    {"front":"Agent vs solicitor","back":"An agent can seek applicants, present insurance solutions, complete applications, and may bind coverage. A solicitor seeks prospects but has no independent authority to bind coverage."},
    {"front":"Solicitor — typical role","back":"Find prospects and arrange appointments with an agent who can sell and bind coverage."},
    {"front":"Fiduciary","back":"A person in a position of financial trust and confidence who must handle entrusted interests or funds with appropriate loyalty and care."},
    {"front":"Agent as fiduciary","back":"Agents act in a fiduciary capacity when handling premiums or giving advice that affects a client's financial security."},
    {"front":"Agent representation memory cue","back":"Agent = insurer/company side."},
    {"front":"Broker representation memory cue","back":"Broker = buyer/client side."},
    {"front":"Solicitor memory cue","back":"Solicitor = seeks prospects, sets appointments, cannot independently bind coverage."},
]

QUESTIONS = [
    {"q":"In an insurance sales transaction, an agent generally represents the:","choices":["Insurer","Applicant","Beneficiary","State regulator"],"answer":0,"why":"An agent acts on behalf of the insurer under an agency relationship."},
    {"q":"In an insurance sales transaction, a broker generally represents the:","choices":["Buyer or applicant","Insurer","State regulator","Reinsurer"],"answer":0,"why":"A broker generally represents the insurance buyer rather than a particular insurer."},
    {"q":"Which producer generally cannot bind an insurer to coverage merely by acting as a broker?","choices":["Broker","Appointed agent with binding authority","Authorized insurer representative","None of these"],"answer":0,"why":"A broker generally must place the coverage through an agent or company representative who has authority to bind the insurer."},
    {"q":"A licensed person seeks prospects and arranges meetings with agents but has no authority to bind coverage. This person is acting as a:","choices":["Solicitor","Broker with binding authority","Insurer","Principal"],"answer":0,"why":"A solicitor's role is prospecting and arranging opportunities for an authorized agent, without independent binding authority."},
    {"q":"Which activity most clearly demonstrates an insurance agent's fiduciary capacity?","choices":["Handling premium money entrusted to the agent","Choosing an office paint color","Scheduling lunch","Buying personal stationery"],"answer":0,"why":"Handling another party's money creates a position of financial trust and confidence."},
    {"q":"Which pairing is correct?","choices":["Agent—insurer; Broker—buyer/applicant","Agent—buyer; Broker—insurer","Agent—regulator; Broker—insurer","Agent—beneficiary; Broker—regulator"],"answer":0,"why":"The core exam distinction is that the agent represents the insurer while the broker represents the buyer/applicant."},
    {"q":"Who would a solicitor normally refer a prospect to when the prospect is ready to purchase coverage?","choices":["An agent authorized to sell and bind coverage","Another prospect","A beneficiary","A reinsurer"],"answer":0,"why":"Solicitors generate prospects and appointments; an authorized agent handles the insurance sale and binding authority."},
    {"q":"Why is an insurance agent considered a fiduciary in important parts of the relationship?","choices":["The agent may handle entrusted money and provide advice affecting financial security","The agent owns the insurer","The agent is always the applicant","The agent regulates insurance law"],"answer":0,"why":"Fiduciary responsibilities arise from financial trust, including handling premiums and advising clients."},
]

SCENARIO_DRILLS = [
    {"scenario":"Jordan represents an insurer under an appointment and has authority within that appointment to bind eligible coverage.","answer":"Agent","why":"An agent represents the insurer and may receive binding authority through the agency contract and appointment."},
    {"scenario":"Taylor represents a buyer, shops among insurers, and must place the selected coverage through someone authorized to bind the insurer.","answer":"Broker","why":"A broker represents the buyer/applicant and generally does not independently bind the insurer."},
    {"scenario":"Casey finds prospects and schedules them to meet with an authorized agent but cannot bind coverage.","answer":"Solicitor","why":"Prospecting without independent binding authority is the key solicitor distinction."},
    {"scenario":"An agent accepts a client's premium payment on behalf of the insurer.","answer":"Fiduciary capacity","why":"The agent is handling entrusted funds and therefore occupies a position of financial trust."},
]

LIGHTNING = [
    ("Represents insurer", "Agent"),
    ("Represents buyer/applicant", "Broker"),
    ("Can have authority to bind insurer", "Agent"),
    ("Generally cannot independently bind insurer", "Broker"),
    ("Finds prospects and sets appointments; no binding authority", "Solicitor"),
    ("Position of financial trust and confidence", "Fiduciary"),
    ("Handling premium funds", "Fiduciary duty"),
]
