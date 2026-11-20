from __future__ import annotations

# High-yield deck built from recurring public candidate-study themes plus official-topic alignment.
# Public anecdotes are signals, not proof of exact live questions. No recalled/live questions are reproduced.

PUBLIC_SIGNAL_NOTE = (
    "This deck prioritizes concepts repeatedly emphasized in public candidate discussions and common prep resources, "
    "then anchors them to the Florida 2-15 licensing scope. It predicts topic families, not exact exam questions."
)

HIGH_YIELD_CARDS = [
    # Florida law / regulation and pure memorization
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Twisting","back":"Using misleading comparisons or misrepresentations to induce a policyowner to replace or change insurance coverage."},
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Rebating","back":"Offering an unlawful inducement or value not stated in the contract to persuade someone to buy insurance, subject to current Florida law."},
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Misrepresentation","back":"Making false or misleading statements about a policy, its terms, benefits, dividends, insurer, or related facts."},
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Fiduciary responsibility","back":"Premiums and funds received by an agent must be handled and accounted for in a fiduciary capacity."},
    {"category":"Florida Rules & Regulation","priority":4,"kind":"memorize","front":"Domestic / foreign / alien insurer","back":"Domestic = organized under Florida law; foreign = organized under another U.S. state; alien = organized under another country."},
    {"category":"Florida Rules & Regulation","priority":4,"kind":"memorize","front":"Authorized/admitted insurer","back":"An insurer authorized by the state to transact the applicable insurance business."},
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Express / implied / apparent authority","back":"Express = specifically granted; implied = reasonably necessary to carry out express authority; apparent = authority a third party reasonably believes exists because of the principal's conduct."},
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Insurance contract characteristics","back":"Aleatory, unilateral, adhesion, conditional. Know what each word means and recognize it in a short scenario."},
    {"category":"Florida Rules & Regulation","priority":5,"kind":"memorize","front":"Peril vs hazard","back":"Peril = direct cause of loss. Hazard = condition that increases the chance or severity of loss."},
    {"category":"Florida Rules & Regulation","priority":4,"kind":"memorize","front":"Insurable interest","back":"A legitimate financial/economic interest in avoiding the insured loss; know when it must exist for life versus property/casualty concepts."},

    # Life
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Term life","back":"Temporary death protection for a stated period; generally no cash value."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Whole life","back":"Permanent coverage commonly characterized by level premiums, guaranteed death benefit and guaranteed cash value when contractual requirements are met."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Universal life","back":"Flexible-premium permanent life insurance with separately identified mortality, expense and interest elements; policy must remain adequately funded."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Variable life / VUL","back":"Uses separate-account investments; values can fluctuate and the policyowner bears investment risk. Variable products also involve securities regulation."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Revocable vs irrevocable beneficiary","back":"Revocable can generally be changed by the policyowner; irrevocable generally requires the beneficiary's consent for changes affecting their rights."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Primary vs contingent beneficiary","back":"Primary is first in line; contingent receives proceeds if the primary beneficiary cannot or does not receive them."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Reduced paid-up","back":"Nonforfeiture option using cash value to buy a smaller amount of fully paid permanent insurance."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Extended term","back":"Nonforfeiture option using cash value to buy term coverage generally for the original face amount for as long as the value permits."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Cash surrender","back":"Nonforfeiture option in which the policyowner terminates the policy and receives available cash surrender value."},
    {"category":"Life Insurance","priority":5,"kind":"memorize","front":"Waiver of premium rider","back":"Waives required premiums during a qualifying total disability under the rider's terms."},
    {"category":"Life Insurance","priority":4,"kind":"memorize","front":"Guaranteed insurability rider","back":"Allows purchase of additional coverage at stated times/events without new evidence of insurability."},
    {"category":"Life Insurance","priority":4,"kind":"memorize","front":"Absolute vs collateral assignment","back":"Absolute transfers ownership rights; collateral gives a creditor a limited interest as security for a debt."},
    {"category":"Life Insurance","priority":4,"kind":"memorize","front":"Policy loan at death","back":"Outstanding loan balance and interest generally reduce net death proceeds."},
    {"category":"Life Insurance","priority":4,"kind":"memorize","front":"Key-person insurance","back":"Business-owned coverage intended to offset economic loss caused by the death of a key person."},
    {"category":"Life Insurance","priority":4,"kind":"memorize","front":"Buy-sell funding","back":"Life insurance can provide liquidity to purchase a deceased owner's business interest."},

    # Annuities / variable contracts
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Immediate vs deferred annuity","back":"Immediate begins payout relatively soon; deferred has an accumulation period before payout."},
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Fixed vs variable annuity investment risk","back":"Fixed: insurer generally bears investment risk supporting guarantees. Variable: contract owner bears separate-account investment risk."},
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Accumulation units vs annuity units","back":"Accumulation units measure variable-annuity interests before annuitization; annuity units are used during the payout phase."},
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Life-only annuity payout","back":"Generally highest periodic lifetime payment because there is no minimum refund/period-certain guarantee after death."},
    {"category":"Annuities & Variable Contracts","priority":4,"kind":"memorize","front":"Life with period certain","back":"Pays for life but guarantees payments for at least the selected certain period; beneficiary can receive remaining guaranteed payments after early death."},
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Tax-deferred does NOT mean tax-free","back":"Annuity earnings generally grow tax-deferred; taxation is postponed until distribution under applicable tax rules."},
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Nonqualified annuity funding","back":"Generally funded with after-tax dollars; distinguish basis from taxable earnings when studying distributions."},
    {"category":"Annuities & Variable Contracts","priority":5,"kind":"memorize","front":"Variable products: dual nature","back":"Variable life and variable annuities are insurance products with securities exposure, so appropriate insurance and securities requirements apply."},

    # Health / disability / Medicare / LTC
    {"category":"Health Insurance","priority":5,"kind":"memorize","front":"Deductible / copay / coinsurance","back":"Deductible = amount paid before plan sharing begins; copay = stated dollar amount; coinsurance = percentage sharing of covered expenses."},
    {"category":"Health Insurance","priority":5,"kind":"memorize","front":"Elimination period","back":"Time waiting period after a qualifying disability begins before disability income benefits become payable."},
    {"category":"Health Insurance","priority":5,"kind":"memorize","front":"Benefit period","back":"Maximum period during which qualifying disability benefits may be payable under the policy."},
    {"category":"Health Insurance","priority":5,"kind":"memorize","front":"Medicare A / B / C / D","back":"A = hospital; B = medical/outpatient; C = Medicare Advantage; D = prescription drugs."},
    {"category":"Health Insurance","priority":4,"kind":"memorize","front":"Group insurance structure","back":"Typically a master policy is issued to the group and covered members receive certificates/evidence of coverage."},
    {"category":"Health Insurance","priority":4,"kind":"memorize","front":"Coordination of benefits","back":"Determines order/coordination of payment when a person has multiple health coverages and helps prevent improper duplication."},
    {"category":"Health Insurance","priority":4,"kind":"memorize","front":"Guaranteed renewable","back":"Insurer generally must renew to the stated age/point if premiums are paid, while permitted class-wide premium changes may occur."},
    {"category":"Health Insurance","priority":4,"kind":"memorize","front":"Noncancelable","back":"During the guaranteed period, insurer generally cannot cancel coverage or raise the insured's premium if required premiums are paid."},
    {"category":"Health Insurance","priority":5,"kind":"memorize","front":"Long-term care core purpose","back":"Coverage for qualifying extended care such as nursing, assisted-living, home/community care, subject to benefit triggers and policy terms."},
]

# Scenario families train recognition rather than lengthy analysis.
SCENARIO_PATTERNS = [
    ("An agent uses a misleading comparison to get a client to replace an existing policy.", "Twisting"),
    ("An agent offers an unauthorized gift/value to induce a sale.", "Rebating"),
    ("A policyowner wants the original face amount maintained temporarily after stopping premiums.", "Extended term"),
    ("A policyowner wants a smaller permanent policy with no more premiums.", "Reduced paid-up"),
    ("A disabled insured must wait 60 days before income benefits begin.", "Elimination period"),
    ("A retiree wants the largest lifetime annuity payment and accepts that payments stop at death.", "Life only"),
    ("An annuity owner's account rises and falls with separate-account investments.", "Variable annuity"),
    ("A beneficiary designation cannot be changed without that beneficiary's consent.", "Irrevocable beneficiary"),
    ("A business insures an employee whose death would cause major financial loss.", "Key-person insurance"),
    ("A creditor receives limited policy rights as security for a loan.", "Collateral assignment"),
]

# Numbers/rules should come from current official Florida material, not crowdsourced recollection.
OFFICIAL_ONLY_BUCKETS = [
    "Florida licensing/appointment deadlines and administrative time periods",
    "Florida replacement notice and record-retention requirements",
    "Florida free-look, grace-period, reinstatement and claims-related statutory numbers",
    "Florida annuity suitability/best-interest requirements and required documentation",
    "Florida long-term-care and Medicare supplement state-specific requirements",
    "Any dollar limit, age threshold, day count, hour requirement, fine or penalty",
]
