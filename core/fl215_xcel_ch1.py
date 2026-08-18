from __future__ import annotations

# Original review prompts distilled from user-provided XCEL Chapter 1 screenshots.
# This file does not reproduce proprietary XCEL exam questions.

CH1_CARDS = [
    {"front":"NAIC — what is it?","back":"National Association of Insurance Commissioners: an organization of state insurance regulators that promotes uniformity, supports state regulation, protects consumers, and develops model laws/regulations. It is not itself a legislature or enforcement agency."},
    {"front":"NAIC model acts","back":"Templates for state insurance legislation/regulation. States may adopt or modify them; the NAIC itself does not enact state law."},
    {"front":"NAIC Unfair Trade Practices model","back":"Model framework addressing practices such as misrepresentation, false advertising, coercion/intimidation, unfair discrimination, and unfair claims practices; state insurance authorities enforce their adopted laws."},
    {"front":"NAIC Advertising Code","back":"Model standards aimed at preventing misleading insurance advertising and requiring appropriate disclosure in advertising and direct-mail solicitation."},
    {"front":"NCOIL","back":"National Conference of Insurance Legislators: organization of state legislators focused on insurance policy; develops model laws, educates policymakers, and supports state-based insurance regulation."},
    {"front":"NAIC vs NCOIL","back":"NAIC = state insurance regulators/commissioners and model regulations. NCOIL = state legislators and model laws. Both support state-based insurance regulation."},
    {"front":"NAIFA / NAHU ethics focus","back":"Professional organizations emphasizing ethical life/health insurance sales: sell to needs, recommend suitable products, make full and accurate disclosure, document recommendations/decisions, and provide ongoing client service."},
    {"front":"Selling to needs","back":"Learn the client's actual needs first, then recommend products designed to address those needs rather than selling merely for production."},
    {"front":"Suitability of recommended products","back":"Match the product to the client's needs, objectives, financial capabilities, and relevant circumstances."},
    {"front":"Full and accurate disclosure","back":"Explain relevant product benefits, limitations, costs, conditions, and material facts accurately."},
    {"front":"Documentation","back":"Document meetings, fact-finding, identified needs, recommendations, and client decisions/acknowledgments as required."},
    {"front":"Client service","back":"The relationship continues after the sale; maintain service, assist through delivery and ongoing needs, and act professionally."},
    {"front":"Producer role","back":"A conduit between insurer and insurance-buying public; solicits business, helps clients obtain coverage from application through delivery, guides clients toward appropriate products, and maintains relationships."},
    {"front":"Purpose of insurer rating services","back":"Independent rating organizations publicize/evaluate an insurer's financial strength and ability to meet obligations; examples include A.M. Best, Fitch, S&P, and Moody's."},
    {"front":"Solvency","back":"The insurer's overall financial ability to meet its obligations. Financial strength/solvency is a major concern for policyowners and regulators."},
    {"front":"Insurer reserves","back":"Accounting measurement of future obligations to policyholders. Reserves are carried as liabilities because the insurer expects to settle those obligations in the future."},
    {"front":"Insurer liquidity","back":"Ability to have sufficient available funds/assets to make payouts as obligations arise, including unpredictable policyowner claims or benefits."},
    {"front":"Reserves vs liquidity","back":"Reserves = measured future obligations/liabilities. Liquidity = ability to produce cash/available funds for payments when needed."},
    {"front":"Risk transfer and pooling","back":"Insurance transfers financial risk from individuals to an insurer and pools premiums/loss exposure across many insureds."},
    {"front":"Stock vs mutual insurer","back":"Stock insurer is owned by shareholders/stockholders; mutual insurer is owned by policyholders."},
    {"front":"Underwriting / claims / actuarial","back":"Underwriting evaluates/selects risk; claims evaluates and pays covered losses; actuarial work uses statistics/mortality/morbidity and financial assumptions to help price products and establish reserves."},
    {"front":"Insurance distribution paths","back":"Insurance may reach consumers through career/captive agents, independent agents, and direct-marketing channels; know the basic distinctions."},
]

CH1_QUESTIONS = [
    {"q":"Which organization is composed primarily of state insurance regulators and develops model insurance laws and regulations?","choices":["NAIC","NCOIL","FINRA","SIPC"],"answer":0,"why":"The NAIC is made up of state insurance regulators and develops model acts/regulations."},
    {"q":"Which statement about the NAIC is most accurate?","choices":["It directly enacts state insurance statutes","It is a federal enforcement agency","It develops model acts and promotes regulatory uniformity","It licenses every insurance producer in the United States"],"answer":2,"why":"The NAIC develops models and promotes consistency; states enact and enforce their own laws."},
    {"q":"The National Conference of Insurance Legislators is primarily made up of:","choices":["State legislators","Insurance company actuaries","Federal judges","Registered representatives"],"answer":0,"why":"NCOIL is a legislative organization of state lawmakers focused on insurance policy."},
    {"q":"A useful distinction between NAIC and NCOIL is:","choices":["NAIC is regulators; NCOIL is legislators","NAIC is federal; NCOIL is international","NAIC regulates securities; NCOIL regulates banks","There is no meaningful distinction"],"answer":0,"why":"NAIC centers on state insurance regulators; NCOIL centers on state legislators."},
    {"q":"Which activity best reflects an ethical needs-based sales practice?","choices":["Recommend the highest-commission product first","Identify client needs before recommending a product","Avoid discussing product limitations","Skip documentation if the client agrees verbally"],"answer":1,"why":"Needs-based selling starts with fact-finding and matching the recommendation to the client's needs."},
    {"q":"An ethical producer should disclose:","choices":["Only benefits","Only premium","Relevant benefits and limitations","Nothing beyond the application"],"answer":2,"why":"Full and accurate disclosure includes material benefits, limitations, and relevant product facts."},
    {"q":"Which is most consistent with good producer documentation?","choices":["Record identified needs and recommendations","Rely entirely on memory","Destroy notes immediately","Document only declined products"],"answer":0,"why":"Good documentation records needs, recommendations, decisions, and relevant client interactions."},
    {"q":"Under NAIC unfair-trade-practice concepts, which is most likely considered unfair?","choices":["Accurate disclosure","False advertising","Fact-finding","Policy delivery"],"answer":1,"why":"False or misleading advertising is a classic unfair trade practice."},
    {"q":"The NAIC Advertising Code is designed primarily to reduce:","choices":["Misleading insurance advertising","Medical underwriting","Premium collection","Actuarial reserving"],"answer":0,"why":"Its focus is truthful, properly disclosed insurance advertising and solicitation."},
    {"q":"Which organization is most closely associated with writing model laws for consideration by state legislatures?","choices":["NCOIL","SIPC","FDIC","Federal Reserve"],"answer":0,"why":"NCOIL develops model insurance laws for state legislative consideration."},
    {"q":"A rating service such as A.M. Best is primarily useful for evaluating an insurer's:","choices":["Producer commission schedule","Financial strength","Advertising slogan","Policyowner age"],"answer":1,"why":"Rating services focus primarily on insurer financial strength and ability to meet obligations."},
    {"q":"An insurer's reserves are best described as:","choices":["Future obligations measured as liabilities","Producer bonuses","Guaranteed profits","Advertising expenses"],"answer":0,"why":"Reserves represent measured future obligations to policyholders and are accounted for as liabilities."},
    {"q":"Which term most directly describes an insurer's ability to make payments when funds are needed?","choices":["Liquidity","Rebating","Adhesion","Indemnity"],"answer":0,"why":"Liquidity concerns the availability of funds/assets to make payments as obligations arise."},
    {"q":"Who owns a mutual insurance company?","choices":["Policyholders","Stockholders","State regulators","Producers"],"answer":0,"why":"Mutual insurers are owned by their policyholders."},
    {"q":"Which department is primarily responsible for evaluating applicants and selecting risk?","choices":["Underwriting","Claims","Marketing","Accounting"],"answer":0,"why":"Underwriting evaluates and classifies risks presented to the insurer."},
    {"q":"Which insurance-company function relies heavily on statistical assumptions to help price products and establish reserves?","choices":["Actuarial","Claims intake","Agency recruiting","Policy delivery"],"answer":0,"why":"Actuaries use statistical and financial assumptions in pricing and reserve calculations."},
]

LIGHTNING = [
    ("State insurance regulators; model acts/regulations", "NAIC"),
    ("State legislators; model insurance laws", "NCOIL"),
    ("Misrepresentation, false advertising, coercion, unfair discrimination", "Unfair trade practices"),
    ("Truthful insurance advertising and disclosures", "NAIC Advertising Code"),
    ("Match recommendation to client needs and capabilities", "Suitability"),
    ("Explain benefits and limitations accurately", "Full and accurate disclosure"),
    ("Record needs, recommendations, and decisions", "Documentation"),
    ("Relationship continues after the sale", "Client service"),
    ("Future obligations shown as liabilities", "Reserves"),
    ("Ability to make payments when needed", "Liquidity"),
    ("A.M. Best / Fitch / S&P / Moody's", "Rating services"),
    ("Owned by shareholders", "Stock insurer"),
    ("Owned by policyholders", "Mutual insurer"),
    ("Evaluates and selects risk", "Underwriting"),
    ("Evaluates covered losses and benefits", "Claims"),
    ("Statistics, pricing, mortality/morbidity, reserves", "Actuarial"),
]
