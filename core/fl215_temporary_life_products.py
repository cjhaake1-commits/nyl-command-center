from __future__ import annotations

# Original study drills distilled from user-provided XCEL life-insurance screenshots.
# Content is paraphrased for active recall and exam practice.

CARDS = [
    {"front":"Term life — basic definition","back":"Pure, temporary life-insurance protection for a limited period. It pays a death benefit only if the insured dies while coverage is in force."},
    {"front":"Why term life is usually low cost","back":"Term insurance focuses on mortality protection only and generally does not build cash value, so it can provide a large death benefit for a relatively low initial premium."},
    {"front":"How a term can be defined","back":"A term may be stated as a number of years, such as 10 or 20 years, or it may run until a specified age, such as age 65 or 70."},
    {"front":"If the insured outlives the term","back":"The policy expires and no death benefit is payable unless some separate feature or renewal/conversion option applies."},
    {"front":"If term coverage lapses or is cancelled before death","back":"If the insured dies after coverage has lapsed or been cancelled, the term policy does not pay a death benefit."},
    {"front":"Level term premium concept","back":"Many term policies use a fixed premium during the stated level period because the mortality cost is averaged across the term."},
    {"front":"Main economic advantage of term life","back":"For the same face amount, term insurance typically has a lower initial premium than permanent life insurance."},
    {"front":"Main economic limitation of term life","back":"Term life generally does not accumulate cash value and can expire without paying a benefit if the insured survives the term."},
    {"front":"Term life — death benefit per premium dollar","back":"Term life usually provides the greatest amount of death benefit per dollar of initial premium outlay."},
    {"front":"Three basic term-policy patterns","back":"Level term, decreasing term, and increasing term; they are primarily distinguished by how the face amount changes over time."},
    {"front":"Decreasing term life","back":"A term policy whose death benefit gradually declines during the coverage period while the premium typically remains level."},
    {"front":"Common use for decreasing term","back":"Designed to match a declining financial obligation, such as a mortgage or other loan balance."},
    {"front":"Decreasing term example","back":"A 20-year policy may start with a $50,000 death benefit that declines over the term toward zero, while the premium remains unchanged."},
    {"front":"Mortgage redemption insurance","back":"A form of decreasing term life insurance intended to pay off the remaining mortgage balance if the insured dies before the mortgage is fully repaid."},
    {"front":"Why mortgage redemption face amount declines","back":"The policy face amount is designed to track the shrinking mortgage balance over time."},
    {"front":"Credit life insurance","back":"A limited-benefit term policy covering a debtor so that the outstanding loan balance can be paid if the debtor dies before repayment."},
    {"front":"Credit life beneficiary","back":"Usually the lender or creditor, because the purpose is to satisfy the remaining debt."},
    {"front":"Credit life benefit pattern","back":"Usually decreasing term, with coverage matching the declining outstanding loan balance and a term matched to the loan period."},
    {"front":"Who usually pays for credit life","back":"The borrower typically pays the entire cost, including when group credit life is arranged through a lending institution."},
    {"front":"Maximum credit life benefit","back":"The benefit cannot exceed the amount of the indebtedness; the creditor's insurable interest is limited to the debt owed."},
    {"front":"Credit insurance coercion rule","back":"A lender may require suitable insurance as a loan condition in some settings, but cannot force the borrower to buy it from that lender or a particular insurer. Doing so is coercion."},
]

QUESTIONS = [
    {"q":"Which statement best describes term life insurance?","choices":["Temporary pure death protection for a stated period","Permanent coverage that always builds cash value","An annuity that pays monthly income","Property insurance for a limited term"],"answer":0,"why":"Term life is temporary death protection for a defined period."},
    {"q":"What happens if an insured survives a basic term policy through the end of its coverage period?","choices":["The policy expires with no death benefit payable","The face amount is automatically paid","The policy becomes whole life automatically","Cash value equal to premiums is refunded"],"answer":0,"why":"Basic term coverage expires if the insured outlives the term."},
    {"q":"Why can term life usually provide more death benefit per premium dollar than permanent life?","choices":["It generally provides pure death protection without building cash value","It has no underwriting","It pays every policyholder at maturity","It is subsidized by property insurers"],"answer":0,"why":"Term focuses on mortality protection rather than combining protection with cash-value accumulation."},
    {"q":"A policy provides coverage from age 45 until age 65. How is its term defined?","choices":["By a specified age","By a cash-value target","By an annuity period","By a premium mode"],"answer":0,"why":"Some term policies remain in force until the insured reaches a stated age."},
    {"q":"What is the primary financial advantage of term life compared with permanent life of the same face amount?","choices":["Lower initial premium","Guaranteed cash-value growth","Guaranteed dividends","Lifetime coverage regardless of premium payment"],"answer":0,"why":"Term insurance generally costs substantially less initially for the same face amount."},
    {"q":"Which of the following is NOT a basic type of term insurance based on face-amount pattern?","choices":["Whole life","Level term","Decreasing term","Increasing term"],"answer":0,"why":"Whole life is permanent insurance; the basic term patterns are level, decreasing, and increasing."},
    {"q":"Why can a level-term policy charge a constant premium for several years even though mortality risk rises with age?","choices":["Premium cost is averaged over the level term","Mortality risk does not rise with age","The insurer waives later-year mortality cost","The policy builds enough dividends to cover all increases"],"answer":0,"why":"The premium can be levelized by averaging expected cost over the stated term."},
    {"q":"Steve owns a 20-year level term policy. He dies in year 12 while the policy is in force. What happens?","choices":["The beneficiary receives the stated death benefit","No benefit is payable because the term was not completed","Only accumulated cash value is paid","Premiums are refunded instead of a death benefit"],"answer":0,"why":"Death during the in-force term triggers the policy's death benefit."},
    {"q":"Which combination is characteristic of decreasing term life insurance?","choices":["Declining death benefit and usually level premium","Increasing death benefit and increasing cash value","Level death benefit and declining premium","Lifetime death benefit with flexible premium"],"answer":0,"why":"Decreasing term reduces the face amount over time while premiums generally remain level."},
    {"q":"What is a common purpose of decreasing term life insurance?","choices":["Covering a debt that declines over time","Building retirement cash value","Funding an annuity","Providing a level lifelong death benefit"],"answer":0,"why":"Decreasing term is well suited to obligations such as mortgages and loans that shrink over time."},
    {"q":"Mortgage redemption insurance is best described as which type of policy?","choices":["Decreasing term life","Whole life","Increasing term life","Variable life"],"answer":0,"why":"Mortgage redemption is a classic decreasing term design matched to a mortgage balance."},
    {"q":"Why does the face amount of mortgage redemption insurance decrease over time?","choices":["It is intended to track the declining mortgage balance","The insured's age decreases","The premium is refunded annually","State law requires all mortgage policies to become zero-value"],"answer":0,"why":"The insurance amount shrinks as the mortgage indebtedness shrinks."},
    {"q":"Who is usually the beneficiary of a credit life insurance policy?","choices":["The lender or creditor","The debtor's employer","The state insurance department","Any random third party"],"answer":0,"why":"Credit life is designed to pay off the debt, so the creditor is typically the beneficiary."},
    {"q":"What is the maximum allowable benefit under credit life insurance?","choices":["The amount of the outstanding indebtedness","Twice the loan balance","Any amount chosen by the lender","The debtor's annual income"],"answer":0,"why":"The creditor's insurable interest is limited to the value of the debt."},
    {"q":"A bank tells a borrower that loan approval requires buying credit life insurance specifically from the bank's chosen insurer. What practice is this?","choices":["Coercion","Subrogation","Waiver","Estoppel"],"answer":0,"why":"A lender cannot force a borrower to purchase required insurance from a specific organization or insurer."},
    {"q":"Who typically pays the cost of group credit life insurance?","choices":["The borrower","The lender","The state guaranty association","The beneficiary's estate"],"answer":0,"why":"The borrower typically bears the full cost of credit life coverage."},
]

LIGHTNING = [
    ("Pure temporary life protection", "Term life"),
    ("Term insured survives coverage period", "Policy expires; no death benefit"),
    ("Term may be stated by", "Years or a specified age"),
    ("Term cash value", "Generally none"),
    ("Main term advantage", "Large death benefit for low initial premium"),
    ("Main term limitation", "Temporary; may expire with no payout"),
    ("Fixed premium during a term", "Levelized/averaged premium"),
    ("Three basic face-amount patterns", "Level, decreasing, increasing term"),
    ("Death benefit declines, premium level", "Decreasing term"),
    ("Classic decreasing-term use", "Mortgage or loan payoff"),
    ("Mortgage protection tied to shrinking balance", "Mortgage redemption insurance"),
    ("Debtor life coverage for loan payoff", "Credit life insurance"),
    ("Typical credit life beneficiary", "Lender / creditor"),
    ("Maximum credit life benefit", "Amount of indebtedness"),
    ("Force borrower to buy from specific insurer", "Illegal coercion"),
]
