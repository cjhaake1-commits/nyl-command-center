from __future__ import annotations

from io import StringIO
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Group / Affinity Benefits", page_icon="🤝", layout="wide")
st.title("Group / Affinity Benefits")
st.caption("Central Florida organization-level prospecting: retirement/investment opportunity + member benefit access + business-owner referral multiplication.")

st.info(
    "Research/planning lane only. Group eligibility, minimum participation, underwriting, product availability, securities/retirement-plan structure, pricing and any major-medical arrangement must be confirmed for the specific organization and product before presentation. Do not promise that group coverage is always cheaper or that every organization qualifies for every product."
)

DATA = '''Organization,Category,Area,Decision Maker,Title,Phone,Email,Investment Potential,Access,Owner Density,Group Fit,Primary Opportunity Lanes,Status
Orlando Regional REALTOR Association,Professional/Trade Association,Orlando,Cliff Long,CEO,407-253-3580,,5,5,5,5,"401(k)/retirement access; mutual funds/IRA/annuity education; group life/disability; owner referrals",Research complete
Central Florida Hotel & Lodging Association,Trade Association,Orlando,Robert Agrusa,President / CEO,407-313-5020,robert.agrusa@cfhla.org,5,5,4,5,"Employer retirement plans; group life/disability; voluntary benefits; executive/key-person introductions",Research complete
Associated Builders and Contractors - Central Florida,Trade Association,Orlando,Michele Daugherty,President & CEO,407-628-2070,mdaugherty@abccentralflorida.org,5,5,5,5,"401(k)/SEP/SIMPLE; group life/disability; voluntary benefits; key-person/buy-sell/succession",Research complete
Greater Orlando Builders Association,Trade Association,Orlando,Chassity Vega,Chief Executive Officer,407-629-9242 ext 6,Chassity@GreaterOrlandoBA.com,5,5,5,5,"Retirement plans; group benefits; key-person; succession; executive benefits",Research complete
Apartment Association of Greater Orlando,Trade Association,Orlando,Monica Ramsey,CEO / Executive Vice President,407-644-0539,,5,5,5,5,"Retirement plans; group life/disability; voluntary benefits; key-person; owner planning",Research complete
West Orange Chamber of Commerce,Chamber,Winter Garden / West Orange,Stephen Lewis,President & CEO,,,5,5,5,5,"Member affinity benefits; retirement-plan access; life/disability; owner planning/referrals",Research complete
Winter Park Chamber of Commerce,Chamber,Winter Park,Annemarie Cooper,President & CEO,407-599-3685,acooper@winterpark.org,5,5,5,5,"Affinity benefits; retirement plans; financial wellness; owner/key-person/succession introductions",Research complete
Seminole County Chamber,Chamber,Seminole County,Rebekah Arthur,President & CEO,407-708-4600,rarthur@seminolebusiness.org,5,5,5,5,"Affinity benefits; retirement access; group life/disability; owner referrals",Research complete
Hispanic Chamber of Metro Orlando,Chamber,Orlando,Pedro Turushina,President & CEO,407-428-5870,info@hispanicchamber.com,5,5,5,5,"Affinity benefits; retirement plans; financial wellness; owner protection/referrals",Research complete
Lakeland Chamber of Commerce,Chamber,Lakeland,Amy Wiggins,President & CEO,863-688-8551 ext 234,,5,4,5,5,"Affinity benefits; retirement plans; owner life/disability; succession referrals",Research complete
Greater Orlando SHRM,Professional Association,Orlando,Dr. Lynn Johnson,President,,president@goshrm.org,5,4,4,5,"Employer retirement plans; group life/disability; voluntary benefits; employer introductions",Research complete
Association for Corporate Growth - Orlando,Professional Association,Orlando,Nimit Kapoor,President,,,5,4,5,4,"401(k)/executive retirement; key-person; succession; buy-sell; executive benefits",Research complete
Greater Orlando Chapter of IFMA,Professional Association,Greater Orlando,Suzanne Larson,Chapter Administrator,407-800-4486,chapteradministrator@ifmaorlando.org,4,4,3,4,"Employer retirement and benefits introductions; financial wellness; business-owner referrals",Research complete
African American Chamber of Commerce of Central Florida,Chamber,Central Florida,President / CEO,Verify current individual,407-420-4870,,5,4,5,5,"Affinity benefits; retirement plans; financial education; owner protection/referrals",Verify leadership
Asian American Chamber of Commerce of Central Florida,Chamber,Central Florida,President / Executive Director,Verify current individual,,,5,4,5,5,"Affinity benefits; retirement plans; owner protection/referrals",Verify leadership
Philippine American Chamber of Commerce - Central Florida,Chamber,Orlando / Central Florida,President / Board Chair,Verify current individual,,,4,4,5,4,"Affinity benefits; retirement plans; life/disability; owner referrals",Verify leadership
NAWBO Orlando,Professional/Owner Association,Orlando,President / Executive Director,Verify current individual,321-285-6450,,5,4,5,4,"SEP/SIMPLE/401(k); mutual funds/IRA/annuity education; life/disability; owner succession",Verify leadership
Executive Exchange of Central Florida,Business Networking Association,Orlando,President / Membership Chair,Verify current individual,,,5,4,5,4,"Owner retirement; key-person; life/disability; referral network",Verify leadership
Orlando Business Network,Business Networking Association,Orlando,Founder / President,Verify current individual,,,5,4,5,4,"Owner retirement; individual investments; key-person; life/disability; referrals",Verify leadership
Rotary District 6980,Civic / Service Clubs,Orange / Seminole / Osceola / Lake / Sumter,Michael Franklin,District Governor 2026-2027,,,4,4,4,4,"Affinity education; retirement/investment seminars; life/disability; owner/professional referrals",Research complete
Florida District of Kiwanis International,Civic / Service Clubs,Central Florida / Statewide,District leadership / Membership,Verify current local decision maker,,,3,3,3,4,"Affinity benefits where eligible; retirement education; individual planning/referrals",Verify leadership
NAAIA Orlando,Professional Association,Orlando,Chapter President / Board,Verify current individual,,,4,4,3,4,"Retirement/investment education; life/disability; referral partnerships",Verify leadership
HAPBWA - Hispanic American Professional & Business Women's Association,Professional/Owner Association,Central Florida,President / Membership Leadership,Verify current individual,,membershapbwa@gmail.com,4,4,5,4,"Owner retirement; SEP/SIMPLE; individual investments; life/disability; referrals",Verify leadership
Boss Babes of Orlando,Owner / Entrepreneur Community,Orlando,Founder / Membership Leadership,Verify current individual,,,4,4,5,3,"Owner retirement; SEP/SIMPLE; individual investments; life/disability; referrals",Verify leadership
Orlando Chamber of Commerce,Chamber,Orlando,President / CEO,Verify current individual,,,5,4,5,5,"Affinity member benefits; retirement-plan access; life/disability; owner referrals",Verify leadership
Four Corners Chamber of Commerce,Chamber,Lake / Orange / Osceola / Polk,President / Executive Director,Verify current individual,,,4,4,5,4,"Affinity benefits; retirement access; life/disability; owner referrals",Verify leadership
'''

df = pd.read_csv(StringIO(DATA)).fillna("")
df["Priority Score"] = (
    df["Investment Potential"] * 0.35
    + df["Access"] * 0.25
    + df["Owner Density"] * 0.25
    + df["Group Fit"] * 0.15
) * 20

def tier(score: float) -> str:
    if score >= 94: return "A+"
    if score >= 86: return "A"
    if score >= 78: return "B+"
    return "B"

df["Tier"] = df["Priority Score"].apply(tier)
df = df.sort_values(["Priority Score", "Investment Potential", "Owner Density"], ascending=False).reset_index(drop=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Organizations", len(df))
m2.metric("A+ targets", int((df["Tier"] == "A+").sum()))
m3.metric("Verified decision makers", int((df["Status"] == "Research complete").sum()))
m4.metric("Owner-heavy targets", int((df["Owner Density"] >= 5).sum()))

with st.sidebar:
    st.header("Filters")
    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    tiers = st.multiselect("Tier", ["A+", "A", "B+", "B"], default=["A+", "A", "B+"])
    min_investment = st.slider("Minimum investment/retirement potential", 1, 5, 4)
    verified_only = st.checkbox("Verified decision maker only", False)

filtered = df[df["Category"].isin(categories) & df["Tier"].isin(tiers) & (df["Investment Potential"] >= min_investment)].copy()
if verified_only:
    filtered = filtered[filtered["Status"] == "Research complete"]

st.subheader("Ranked Organization Pipeline")
st.dataframe(filtered, width="stretch", hide_index=True)

st.subheader("Managing Partner Discussion Framework")
st.markdown(
    """
**1. Lead with member value, not a product.** Ask whether the organization would consider an exclusive financial-benefits platform that could improve member retention and provide access to protection, retirement planning and financial education.

**2. Run two economics tracks.** Investment/retirement opportunities get the highest lifetime-revenue weighting; group life/disability/voluntary benefits get a high speed-to-access weighting because they can open many owner and employee relationships quickly.

**3. Treat every member business as a second-stage opportunity.** After organization-level approval and compliant engagement, discovery can uncover 401(k), SEP/SIMPLE, mutual-fund/IRA, annuity, key-person, disability, executive-benefit, buy-sell and succession needs.

**4. Confirm structure before promises.** Association eligibility, participation minimums, pricing, underwriting, securities suitability, retirement-plan fiduciary/recordkeeping structure and any major-medical component must be validated for the actual case before being represented to an organization.
"""
)

st.download_button(
    "Download current pipeline CSV",
    filtered.to_csv(index=False).encode("utf-8-sig"),
    "nyl_group_affinity_pipeline.csv",
    "text/csv",
    use_container_width=True,
)
