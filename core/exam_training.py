from __future__ import annotations

# Original study content aligned to public exam outlines. These are not live exam questions.

SIE_DOMAINS = {
    "Capital Markets": 0.16,
    "Products & Risks": 0.44,
    "Trading, Accounts & Prohibited Activities": 0.31,
    "Regulatory Framework": 0.09,
}

SIE_LESSONS = {
    "Capital Markets": [
        "Primary market = issuer sells newly issued securities; secondary market = investors trade existing securities.",
        "Investment bankers help issuers raise capital through underwriting and distribution.",
        "The Federal Reserve influences money and credit primarily through monetary policy; Congress and the executive branch drive fiscal policy.",
        "Expansion generally favors growth and rising employment; contraction/recession generally brings slowing output and employment.",
        "Interest rates and bond prices generally move in opposite directions.",
        "FINRA is an SRO; the SEC is a federal securities regulator.",
    ],
    "Products & Risks": [
        "Common stock represents ownership and usually voting rights; dividends are not guaranteed.",
        "Preferred stock generally has dividend and liquidation preference over common stock but less growth participation.",
        "Bondholders are creditors. Know par value, coupon, maturity, current yield, YTM, call risk, credit risk and interest-rate risk.",
        "Treasury securities carry U.S. government credit backing; municipal bonds are issued by states and political subdivisions.",
        "Mutual funds transact at NAV calculated after the order; ETFs trade intraday in the secondary market.",
        "Options: call buyers are bullish and put buyers are bearish. Buyers have rights; writers have obligations.",
        "Diversification reduces company-specific risk but cannot eliminate systematic market risk.",
        "Variable annuity and variable life values can fluctuate because separate-account performance is market-linked.",
    ],
    "Trading, Accounts & Prohibited Activities": [
        "Market orders prioritize execution; limit orders prioritize price.",
        "A buy limit is placed below the market; a sell limit is placed above the market.",
        "Customer identification and AML procedures help firms detect and report suspicious activity.",
        "Material nonpublic information must not be used to trade or tipped to others for trading.",
        "Market manipulation, front running, unauthorized trading and falsifying records are prohibited.",
        "Know the purpose of account registrations, powers of attorney, discretionary authority and trusted contact information.",
        "Understand communications categories and why securities communications must be fair, balanced and not misleading.",
    ],
    "Regulatory Framework": [
        "The SIE alone does not authorize a person to engage in securities business; qualification and registration requirements still apply.",
        "Associated persons must keep required registration information current and report specified events.",
        "Form U4 is used for registration information; Form U5 is used when an associated person's registration with a firm terminates.",
        "Continuing education and firm-element training support ongoing regulatory competence.",
        "Know high-level roles of the SEC, FINRA, MSRB and state securities regulators.",
    ],
}

FL_215_LESSONS = {
    "General Insurance & Regulation": [
        "Know risk, peril, hazard, indemnity, insurable interest, utmost good faith, representations and warranties.",
        "Know producer licensing, appointments, fiduciary handling of premiums, unfair trade practices and Florida regulatory authority.",
        "Be able to distinguish twisting, rebating, misrepresentation, defamation and unfair discrimination.",
        "Study Florida replacement, advertising, solicitation, recordkeeping and consumer-protection requirements from the current official outline/materials.",
    ],
    "Life Insurance": [
        "Term insurance provides temporary death protection; permanent insurance combines lifetime protection with cash-value features when maintained.",
        "Whole life generally uses fixed premiums and guarantees; universal life separates mortality, expense and interest elements.",
        "Variable life and variable universal life involve securities risk and require appropriate securities registration in addition to insurance authority.",
        "Know policy provisions, riders, beneficiary designations, settlement options, nonforfeiture options, loans, assignments and reinstatement.",
        "Understand needs analysis, human-life-value concepts, business uses of life insurance and taxation basics.",
    ],
    "Annuities": [
        "An annuity is designed primarily to address longevity risk and accumulation/income needs rather than immediate death protection.",
        "Immediate annuities begin income relatively soon; deferred annuities have an accumulation period before payout.",
        "Fixed annuities place investment risk primarily with the insurer; variable annuities place investment risk primarily with the contract owner.",
        "Know accumulation units versus annuity units, surrender charges, annuitization choices, beneficiaries and tax-deferral basics.",
        "Florida-specific annuity suitability/best-interest requirements should always be checked against the current state guidance before the exam.",
    ],
    "Health Insurance": [
        "Know medical expense, disability income, long-term care, Medicare-related coverage and group versus individual concepts.",
        "Understand deductibles, coinsurance, copayments, out-of-pocket limits, elimination periods and benefit periods.",
        "Know common policy provisions, renewability, exclusions, coordination of benefits and claims concepts.",
        "Study Florida-specific health and long-term-care requirements from the current official exam outline and statutes/rules referenced by the state.",
    ],
}

QUESTIONS = [
    {"track":"SIE","domain":"Capital Markets","q":"An issuer sells newly issued common stock to investors. This transaction takes place in which market?","choices":["Primary market","Secondary market","Third market","Fourth market"],"answer":0,"why":"New securities are sold by the issuer in the primary market."},
    {"track":"SIE","domain":"Capital Markets","q":"If market interest rates rise sharply, the price of an existing fixed-rate bond will generally:","choices":["Rise","Fall","Remain unchanged","Move to par immediately"],"answer":1,"why":"Existing fixed coupons become less attractive when new bonds offer higher rates, so prices generally fall."},
    {"track":"SIE","domain":"Capital Markets","q":"Which organization is a self-regulatory organization for broker-dealers?","choices":["Federal Reserve","FINRA","Treasury Department","IRS"],"answer":1,"why":"FINRA is an SRO overseeing member broker-dealers and associated persons."},
    {"track":"SIE","domain":"Products & Risks","q":"Which security most directly represents an ownership interest in a corporation?","choices":["Corporate bond","Common stock","Treasury note","Municipal revenue bond"],"answer":1,"why":"Common stock is an equity ownership interest."},
    {"track":"SIE","domain":"Products & Risks","q":"A customer buys a call option. The customer generally expects the underlying security to:","choices":["Rise","Fall","Remain exactly flat","Default"],"answer":0,"why":"A call gives the buyer the right to buy at the strike price and is generally a bullish position."},
    {"track":"SIE","domain":"Products & Risks","q":"Which risk cannot be eliminated merely by holding a well-diversified portfolio of stocks?","choices":["Business risk","Company-specific risk","Systematic market risk","Management risk"],"answer":2,"why":"Diversification can reduce nonsystematic risk, but broad market/systematic risk remains."},
    {"track":"SIE","domain":"Products & Risks","q":"Mutual fund shares are normally purchased or redeemed at:","choices":["The previous day's NAV","The next calculated NAV after the order","A negotiated intraday price","Par value"],"answer":1,"why":"Open-end investment company shares use forward pricing at the next computed NAV."},
    {"track":"SIE","domain":"Products & Risks","q":"In a variable annuity, investment performance is primarily reflected in the:","choices":["General account only","Separate account","FDIC reserve","SIPC cash account"],"answer":1,"why":"Variable contract values are tied to investments held in separate accounts."},
    {"track":"SIE","domain":"Trading, Accounts & Prohibited Activities","q":"Which order prioritizes execution over price?","choices":["Limit order","Market order","Stop-limit order","GTC limit order"],"answer":1,"why":"A market order seeks prompt execution at the best available price."},
    {"track":"SIE","domain":"Trading, Accounts & Prohibited Activities","q":"Trading while in possession of material nonpublic information is generally:","choices":["Permitted for small trades","Permitted after telling a coworker","Prohibited","Required to create liquidity"],"answer":2,"why":"Trading on material nonpublic information can violate insider-trading laws and rules."},
    {"track":"SIE","domain":"Trading, Accounts & Prohibited Activities","q":"A suspicious pattern of transactions designed to conceal the source of illicit funds is primarily a concern under:","choices":["AML requirements","Proxy rules","Margin maintenance only","Blue-sky registration only"],"answer":0,"why":"AML programs are designed to detect and address suspicious money-laundering activity."},
    {"track":"SIE","domain":"Regulatory Framework","q":"Which form is generally filed when an associated person's registration with a firm terminates?","choices":["Form U4","Form U5","Form 10-K","Form 8-K"],"answer":1,"why":"Form U5 is the Uniform Termination Notice for Securities Industry Registration."},
    {"track":"SIE","domain":"Regulatory Framework","q":"Passing the SIE by itself allows an individual to immediately transact securities business for customers:","choices":["True","False"],"answer":1,"why":"The SIE is a foundational exam; appropriate representative-level qualification, association and registration requirements still apply."},
    {"track":"Florida 2-15","domain":"General Insurance & Regulation","q":"An applicant intentionally provides false material information on an insurance application. This most directly violates the principle of:","choices":["Utmost good faith","Subrogation","Contribution","Reinsurance"],"answer":0,"why":"Insurance contracts depend on truthful disclosure of material facts by the parties."},
    {"track":"Florida 2-15","domain":"General Insurance & Regulation","q":"Inducing a policyowner to replace coverage through misleading comparisons is commonly associated with:","choices":["Twisting","Coinsurance","Subrogation","Indemnity"],"answer":0,"why":"Twisting involves misrepresentation used to induce replacement or change of insurance coverage."},
    {"track":"Florida 2-15","domain":"Life Insurance","q":"Which life policy is designed to provide coverage for a specified period without building traditional cash value?","choices":["Term life","Whole life","Variable whole life","Universal life"],"answer":0,"why":"Term life provides temporary protection and generally does not build cash value."},
    {"track":"Florida 2-15","domain":"Life Insurance","q":"Which party normally has the right to change a revocable beneficiary?","choices":["Insurer","Policyowner","Beneficiary","Producer"],"answer":1,"why":"The policyowner controls contractual rights, including changing a revocable beneficiary."},
    {"track":"Florida 2-15","domain":"Annuities","q":"The primary risk an annuity is designed to help address during retirement is:","choices":["Longevity risk","Property risk","Workers compensation risk","Title risk"],"answer":0,"why":"Annuities can provide income designed to continue for life, helping address the risk of outliving assets."},
    {"track":"Florida 2-15","domain":"Annuities","q":"Who generally bears investment risk in a variable annuity separate account?","choices":["Contract owner","State guaranty association","Federal Reserve","Producer"],"answer":0,"why":"The contract owner's value varies with separate-account investment performance."},
    {"track":"Florida 2-15","domain":"Health Insurance","q":"A health policy requires the insured to pay 20% of covered expenses after the deductible. This is called:","choices":["Coinsurance","Elimination period","Grace period","Waiver"],"answer":0,"why":"Coinsurance is the percentage sharing of covered expenses between insured and insurer."},
    {"track":"Florida 2-15","domain":"Health Insurance","q":"In disability income insurance, the period that must pass after disability begins before benefits are payable is the:","choices":["Elimination period","Probationary license","Contestable period","Conversion period"],"answer":0,"why":"The elimination period functions like a time deductible before disability benefits begin."},
]

SOURCES = [
    ("FINRA — Securities Industry Essentials (SIE) Exam", "https://www.finra.org/registration-exams-ce/qualification-exams/securities-industry-essentials-exam"),
    ("FINRA — SIE Content Outline", "https://www.finra.org/sites/default/files/2025-10/SIE_Content_Outline.pdf"),
    ("Florida DFS — Agent and Adjuster Licensing", "https://www.myfloridacfo.com/division/agents/licensing"),
    ("Pearson VUE — Florida Insurance", "https://www.pearsonvue.com/us/en/fl/insurance.html"),
]
