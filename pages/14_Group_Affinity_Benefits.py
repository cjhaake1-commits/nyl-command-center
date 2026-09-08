from __future__ import annotations

from io import StringIO
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Groups & Affinity", page_icon="🤝", layout="wide")
st.title("Groups & Affinity")
st.caption("Central Florida organization-level prospecting built around one goal: earn the in-person meeting, then discover where New York Life may be able to add value.")

st.info(
    "Research / DRAFT-HOLD lane. Initial outreach is networking and discovery only. Do not promise eligibility, pricing, savings, acceptance, guaranteed issue, no-exam underwriting, tax treatment, product availability, or a specific group/association structure before current NYL/carrier rules, Florida requirements, organization structure, member eligibility, state/product availability, and any required SMRU approval are confirmed."
)

DATA = '''Organization,Category,Area,Decision Maker,Title,Phone,Email,Investment Potential,Access,Owner Density,Group Fit,Primary Opportunity Lanes,Status,New Target,Timing Hook,Custom Opening
Orlando Regional REALTOR Association,Professional/Trade Association,Orlando,Cliff Long,CEO,407-253-3580,,5,5,5,5,"401(k)/retirement access; mutual funds/IRA/annuity education; group life/disability; owner referrals",Research complete,No,,"I wanted to introduce myself because ORRA sits at the center of a huge network of independent professionals and business owners in Central Florida."
Central Florida Hotel & Lodging Association,Trade Association,Orlando,Robert Agrusa,President / CEO,407-313-5020,robert.agrusa@cfhla.org,5,5,4,5,"Employer retirement plans; group life/disability; voluntary benefits; executive/key-person introductions",Research complete,No,,"I have been getting to know more of the employer groups around Central Florida, and CFHLA stood out because of the size and diversity of the hospitality community you represent."
Associated Builders and Contractors - Central Florida,Trade Association,Orlando,Michele Daugherty,President & CEO,407-628-2070,mdaugherty@abccentralflorida.org,5,5,5,5,"401(k)/SEP/SIMPLE; group life/disability; voluntary benefits; key-person/buy-sell/succession",Research complete,No,,"I have been looking at organizations with a strong concentration of business owners and employers, and ABC Central Florida was an obvious group I wanted to get to know better."
Greater Orlando Builders Association,Trade Association,Orlando,Chassity Vega,Chief Executive Officer,407-629-9242 ext 6,Chassity@GreaterOrlandoBA.com,5,5,5,5,"Retirement plans; group benefits; key-person; succession; executive benefits",Research complete,No,,"I wanted to learn more about GOBA because your membership is exactly the kind of owner-and-employer community where there may be several different ways to create value."
Apartment Association of Greater Orlando,Trade Association,Orlando,Monica Ramsey,CEO / Executive Vice President,407-644-0539,,5,5,5,5,"Retirement plans; group life/disability; voluntary benefits; key-person; owner planning",Research complete,No,,"I have been getting to know more of the owner and employer organizations around Orlando, and the Apartment Association caught my attention because of the businesses and decision makers in your membership."
West Orange Chamber of Commerce,Chamber,Winter Garden / West Orange,Stephen Lewis,President & CEO,,,5,5,5,5,"Member affinity benefits; retirement-plan access; life/disability; owner planning/referrals",Research complete,No,,"I am based here in Central Florida and wanted to get more connected with the organizations serving business owners close to home, so West Orange was high on my list."
Winter Park Chamber of Commerce,Chamber,Winter Park,Annemarie Cooper,President & CEO,407-599-3685,acooper@winterpark.org,5,5,5,5,"Affinity benefits; retirement plans; financial wellness; owner/key-person/succession introductions",Research complete,No,,"I have been mapping some of the stronger local business communities around Orlando, and Winter Park was one I specifically wanted to learn more about."
Seminole County Chamber,Chamber,Seminole County,Rebekah Arthur,President & CEO,407-708-4600,rarthur@seminolebusiness.org,5,5,5,5,"Affinity benefits; retirement access; group life/disability; owner referrals",Research complete,No,,"I have been getting to know more of the chamber and employer networks around Central Florida, and Seminole County is one I wanted to introduce myself to directly."
Hispanic Chamber of Metro Orlando,Chamber,Orlando,Pedro Turushina,President & CEO,407-428-5870,info@hispanicchamber.com,5,5,5,5,"Affinity benefits; retirement plans; financial wellness; owner protection/referrals",Research complete,No,,"I wanted to introduce myself because the business-owner community you represent is exactly the kind of network I am trying to understand better and support locally."
Lakeland Chamber of Commerce,Chamber,Lakeland,Amy Wiggins,President & CEO,863-688-8551 ext 234,,5,4,5,5,"Affinity benefits; retirement plans; owner life/disability; succession referrals",Research complete,No,,"I have been widening my Central Florida network beyond Orlando and wanted to learn more about the business-owner community the Lakeland Chamber serves."
Greater Orlando SHRM,Professional Association,Orlando,Dr. Lynn Johnson,President,,president@goshrm.org,5,4,4,5,"Employer retirement plans; group life/disability; voluntary benefits; employer introductions",Research complete,No,,"I wanted to introduce myself because your members are directly involved in the benefit and workforce issues employers are trying to solve every day."
Association for Corporate Growth - Orlando,Professional Association,Orlando,Nimit Kapoor,President,,,5,4,5,4,"401(k)/executive retirement; key-person; succession; buy-sell; executive benefits",Research complete,No,,"I have been looking for groups where business owners, executives and advisors naturally intersect, and ACG Orlando immediately stood out."
Greater Orlando Chapter of IFMA,Professional Association,Greater Orlando,Suzanne Larson,Chapter Administrator,407-800-4486,chapteradministrator@ifmaorlando.org,4,4,3,4,"Employer retirement and benefits introductions; financial wellness; business-owner referrals",Research complete,No,,"I wanted to learn more about IFMA Orlando because your members touch so many employers and facilities across the region."
African American Chamber of Commerce of Central Florida,Chamber,Central Florida,President / CEO,Verify current individual,407-420-4870,,5,4,5,5,"Affinity benefits; retirement plans; financial education; owner protection/referrals",Verify leadership,No,,"I have been getting to know more of the organizations supporting business owners throughout Central Florida and wanted to introduce myself to the Chamber."
Asian American Chamber of Commerce of Central Florida,Chamber,Central Florida,President / Executive Director,Verify current individual,,,5,4,5,5,"Affinity benefits; retirement plans; owner protection/referrals",Verify leadership,No,,"I wanted to introduce myself because I am trying to get more connected with the organizations supporting owner-led businesses across Central Florida."
Philippine American Chamber of Commerce - Central Florida,Chamber,Orlando / Central Florida,President / Board Chair,Verify current individual,,,4,4,5,4,"Affinity benefits; retirement plans; life/disability; owner referrals",Verify leadership,No,,"I have been building relationships with business and professional organizations around Central Florida and wanted to learn more about your membership."
NAWBO Orlando,Professional/Owner Association,Orlando,President / Executive Director,Verify current individual,321-285-6450,,5,4,5,4,"SEP/SIMPLE/401(k); mutual funds/IRA/annuity education; life/disability; owner succession",Verify leadership,No,,"I wanted to connect because NAWBO has exactly the kind of owner-heavy membership where financial and protection needs can look very different from a traditional employee group."
Executive Exchange of Central Florida,Business Networking Association,Orlando,President / Membership Chair,Verify current individual,,,5,4,5,4,"Owner retirement; key-person; life/disability; referral network",Verify leadership,No,,"I am getting more involved with owner and executive networks around Orlando and wanted to learn more about how Executive Exchange serves its members."
Orlando Business Network,Business Networking Association,Orlando,Founder / President,Verify current individual,,,5,4,5,4,"Owner retirement; individual investments; key-person; life/disability; referrals",Verify leadership,No,,"I have been getting to know more of the business-owner networks around Orlando and wanted to introduce myself rather than just send over information cold."
Rotary District 6980,Civic / Service Clubs,Orange / Seminole / Osceola / Lake / Sumter,Michael Franklin,District Governor 2026-2027,,,4,4,4,4,"Affinity education; retirement/investment seminars; life/disability; owner/professional referrals",Research complete,No,,"I am trying to get more involved with established civic and professional groups around Central Florida and wanted to learn how Rotary District 6980 supports its clubs and members."
Florida District of Kiwanis International,Civic / Service Clubs,Central Florida / Statewide,District leadership / Membership,Verify current local decision maker,,,3,3,3,4,"Affinity benefits where eligible; retirement education; individual planning/referrals",Verify leadership,No,,"I wanted to introduce myself because I am looking for ways to support established membership organizations in the area beyond a traditional one-on-one client relationship."
NAAIA Orlando,Professional Association,Orlando,Chapter President / Board,Verify current individual,,,4,4,3,4,"Retirement/investment education; life/disability; referral partnerships",Verify leadership,No,,"I have been getting to know more of the professional associations around Orlando and wanted to learn more about what your chapter is focused on this year."
HAPBWA - Hispanic American Professional & Business Women's Association,Professional/Owner Association,Central Florida,President / Membership Leadership,Verify current individual,,membershapbwa@gmail.com,4,4,5,4,"Owner retirement; SEP/SIMPLE; individual investments; life/disability; referrals",Verify leadership,No,,"I wanted to connect because your membership appears to have a strong mix of professionals and business owners, which is exactly the kind of organization I am trying to get to know better."
Boss Babes of Orlando,Owner / Entrepreneur Community,Orlando,Founder / Membership Leadership,Verify current individual,,,4,4,5,3,"Owner retirement; SEP/SIMPLE; individual investments; life/disability; referrals",Verify leadership,No,,"I have been looking for newer and more entrepreneurial owner communities around Orlando, and your group caught my attention."
Orlando Chamber of Commerce,Chamber,Orlando,President / CEO,Verify current individual,,,5,4,5,5,"Affinity member benefits; retirement-plan access; life/disability; owner referrals",Verify leadership,No,,"I am trying to get more connected with the organizations serving Orlando business owners and wanted to introduce myself directly."
Four Corners Chamber of Commerce,Chamber,Lake / Orange / Osceola / Polk,President / Executive Director,Verify current individual,,,4,4,5,4,"Affinity benefits; retirement access; life/disability; owner referrals",Verify leadership,No,,"I wanted to learn more about Four Corners because you sit at the intersection of several fast-growing Central Florida business communities."
Building Empowerment Chamber of Commerce (BECC),Chamber,Central Florida,Tiffany Jeffers,President & Founder,407-490-2253,connect@becchamber.org,5,5,5,4,"Member financial education; business retirement plans; voluntary protection; owner life/disability; key-person; succession/referrals",Research complete,Yes,"New chamber / early relationship window","I saw that you are building something pretty new in Central Florida, which is actually what caught my attention. I would love to learn what you want the Chamber to become for members and see whether we can be useful as you build it."
FLN Orlando / Florida Lawyers Network,Professional/Owner Network,Orlando,Chapter Development Team,Orlando chapter development,954-961-5999,,5,5,5,3,"Law-firm 401(k); owner retirement; partner life/disability; buy-sell; succession; attorney COI referrals",Research complete,Yes,"Orlando chapter forming in 2026","I saw that the Orlando chapter is still being built out, and that is exactly why I wanted to reach out now rather than after everything is already established."
AFCEA Orlando,Professional/Trade Association,Orlando,Courtney R. Powell,President,,,5,5,4,4,"Employer 401(k); executive benefits; group life/disability; voluntary benefits; key-person; succession",Research complete,Yes,"Founded 2024 / young organization","AFCEA Orlando caught my attention because it is still a relatively young chapter with a strong mix of defense, technology, government and business leadership."
Central Florida Vacation Rental Professionals (CFVRP),Trade/Owner Association,Orlando / Central Florida,Executive leadership,Verify current individual,,,5,4,5,4,"SEP/SIMPLE/401(k); employer plans; owner retirement; life/disability; key-person; employee protection; succession",Verify leadership,Yes,"Newly formed / founding members represent large rental portfolios","I saw that CFVRP is newly formed and already represents a meaningful number of professionally managed vacation homes, so I wanted to learn what you are trying to build for members while the organization is still taking shape."
Manufacturers Association of Central Florida (MACF),Trade Association,Central Florida,Candy Cole,Executive Director,407-897-3384,macfhq@macf.biz,5,5,5,5,"401(k); workforce benefits; life/disability; executive retention; key-person; continuity; succession",Research complete,Yes,"New Executive Director appointed Oct 2025","I noticed MACF has relatively new executive leadership, so I thought this might be a good time to introduce myself and learn what priorities you are setting for members."
Visit Orlando,Tourism Trade Association,Orlando,Kristen Darby,SVP Membership & Support Services,,Join@VisitOrlando.com,5,5,5,5,"Member benefit platform; employer 401(k); financial wellness; group life/disability; voluntary benefits; executive/key-person introductions",Research complete,Yes,"1,600+ member companies / major employer network","I wanted to introduce myself because Visit Orlando represents such a broad cross-section of employers and business owners, and I would like to understand what kinds of member resources are most valuable to them today."
BOMA Orlando,Commercial Real Estate Association,Orlando,Amy Ravenelle,2026 President,407-380-3320,bae@bomaorlando.org,5,5,5,5,"Employer 401(k); group benefits; executive benefits; key-person; owner retirement; CRE referrals",Research complete,Yes,"Company-based membership / strong owner-employer density","BOMA stood out because your membership is tied so closely to companies, owners and senior property professionals, which creates a very different set of needs than a typical individual membership group."
IREM Central Florida Chapter,Professional/Real Estate Association,Central Florida,Nancy Lovell,President,407-782-4446,admin@irem-centralfl.org,5,5,4,4,"401(k); executive benefits; life/disability; key-person; owner retirement; referrals",Research complete,Yes,"High-income real estate management network","I wanted to learn more about IREM because your members sit at the intersection of employers, property operations and senior real-estate leadership throughout Central Florida."
Central Florida FAMP - Florida Association of Mortgage Professionals,Professional/Owner Association,Central Florida,Chapter President,Verify current 2026 individual,850-942-6411,CentralFloridaFAMP@gmail.com,5,4,5,4,"SEP/SIMPLE/401(k); owner retirement; disability/life; key-person; real-estate owner referrals",Verify leadership,Yes,"Owner-heavy mortgage network","I wanted to introduce myself because mortgage professionals are often business owners themselves and also sit close to a huge number of other owners and households across Central Florida."
ILEA Orlando - International Live Events Association,Professional/Owner Association,Orlando,Lisa Compton,President,,info@ileaorlando.com,4,4,5,4,"SEP/SIMPLE/401(k); disability; life; key-person; financial wellness; owner referrals",Research complete,Yes,"Small-employer and independent-operator density","I have been looking at owner-heavy professional groups around Orlando, and ILEA stood out because so many event businesses are entrepreneurial or closely held."
NACE Orlando - National Association for Catering and Events,Professional/Owner Association,Orlando,Selina Mullenax,President,,,4,4,5,4,"Employer retirement plans; owner SEP/SIMPLE; life/disability; employee protection; key-person; succession",Research complete,Yes,"Hospitality/event owner and employer network","I wanted to introduce myself because NACE brings together a lot of local employers and owner-operated businesses, and I would like to understand what your members are asking for beyond the usual industry resources."
ISACA Central Florida Chapter,Professional Association,Central Florida,Ray Payano,President,,,5,4,3,4,"Employer 401(k); executive benefits; financial education; life/disability; technology-company introductions",Research complete,Yes,"1,000+ technology / cybersecurity / governance members","ISACA caught my attention because of the size of the chapter and the concentration of senior technology and cybersecurity professionals in the membership."
'''

df = pd.read_csv(StringIO(DATA)).fillna("")
df["Priority Score"] = (
    df["Investment Potential"] * 0.35
    + df["Access"] * 0.25
    + df["Owner Density"] * 0.25
    + df["Group Fit"] * 0.15
) * 20


def tier(score: float) -> str:
    if score >= 94:
        return "A+"
    if score >= 86:
        return "A"
    if score >= 78:
        return "B+"
    return "B"


df["Tier"] = df["Priority Score"].apply(tier)
df = df.sort_values(["Priority Score", "New Target", "Investment Potential", "Owner Density"], ascending=[False, False, False, False]).reset_index(drop=True)

if "group_affinity_activity" not in st.session_state:
    st.session_state.group_affinity_activity = {}

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Organizations", len(df))
m2.metric("Net-new targets", int((df["New Target"] == "Yes").sum()))
m3.metric("A+ targets", int((df["Tier"] == "A+").sum()))
m4.metric("Verified contacts", int((df["Status"] == "Research complete").sum()))
m5.metric("Owner-heavy", int((df["Owner Density"] >= 5).sum()))

pipeline_tab, call_tab, scripts_tab, meeting_tab, compliance_tab = st.tabs(
    ["📋 Group Pipeline", "📞 Meeting-First Call Queue", "🗣️ Scripts", "🤝 In-Person Meeting", "🛡️ Compliance / Eligibility"]
)

with pipeline_tab:
    st.subheader("Ranked Group / Affinity Pipeline")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        new_only = st.checkbox("Net-new only", False)
    with c2:
        verified_only = st.checkbox("Verified decision maker only", False)
    with c3:
        min_investment = st.slider("Min retirement/investment potential", 1, 5, 4)
    with c4:
        tiers = st.multiselect("Tier", ["A+", "A", "B+", "B"], default=["A+", "A", "B+"])

    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    filtered = df[
        df["Category"].isin(categories)
        & df["Tier"].isin(tiers)
        & (df["Investment Potential"] >= min_investment)
    ].copy()
    if new_only:
        filtered = filtered[filtered["New Target"] == "Yes"]
    if verified_only:
        filtered = filtered[filtered["Status"] == "Research complete"]

    show_cols = [
        "Tier", "Priority Score", "New Target", "Organization", "Category", "Area",
        "Decision Maker", "Title", "Phone", "Email", "Timing Hook",
        "Primary Opportunity Lanes", "Status"
    ]
    st.dataframe(filtered[show_cols], width="stretch", hide_index=True)
    st.download_button(
        "Download filtered group pipeline CSV",
        filtered.to_csv(index=False).encode("utf-8-sig"),
        "nyl_group_affinity_pipeline.csv",
        "text/csv",
        use_container_width=True,
    )

with call_tab:
    st.subheader("Phone objective: earn the in-person meeting")
    st.caption("Keep the call light. Introduce yourself, give one relevant reason for the call, mention the broad member-value idea, and ask to stop by. Save discovery for the meeting.")

    queue = df[(df["Tier"].isin(["A+", "A"]))].copy()
    org = st.selectbox("Choose organization", queue["Organization"].tolist(), key="group_call_org")
    row = queue[queue["Organization"] == org].iloc[0]

    q1, q2, q3 = st.columns(3)
    q1.metric("Tier", row["Tier"])
    q2.metric("Priority", f"{row['Priority Score']:.0f}/100")
    q3.metric("Decision maker", row["Decision Maker"] if row["Decision Maker"] else "Verify")

    st.markdown("**Personalized opening hook**")
    st.success(row["Custom Opening"])

    call_script = f"""Hi {row['Decision Maker'] if row['Decision Maker'] and 'Verify' not in str(row['Decision Maker']) else '[Name]'}, this is Christopher Haake. I’m with New York Life here in Central Florida.\n\n{row['Custom Opening']}\n\nI’ve been looking at ways we may be able to bring some additional value to organizations like yours and their members — whether that’s around benefits, retirement and financial education, or some of the needs that come up for business owners and professionals.\n\nI’m really not trying to turn this into a sales call. I’d much rather stop by, learn a little more about what you’re doing and who your members are, and see if there’s anything that would actually make sense.\n\nWould you have 20 or 30 minutes sometime next week for me to come by and introduce myself?"""
    st.text_area("Call script", call_script, height=300)

    st.markdown("**If they ask: ‘What exactly are you looking to do?’**")
    st.write(
        "It could be a few different things depending on the organization. There may be opportunities around member benefits, retirement or financial education, protection for members and employees, or resources specifically for business owners. But I really don’t know enough about your group yet to tell you what would make sense, which is why I’d rather meet first than start throwing products at you over the phone."
    )

    st.markdown("**If they say they already have benefits**")
    st.write(
        "That’s completely fine. I’m not calling assuming you need to replace anything. I’d really just like to understand what you already offer and whether there are areas that are not being addressed. Sometimes there is, sometimes there isn’t. Either way, I’d still enjoy getting to know the organization."
    )

    st.markdown("**If they say ‘send me something’**")
    st.write(
        "Absolutely. I can send a short introduction. Rather than sending a bunch of generic material, though, I’d still like to sit down for a few minutes first so I understand the organization. Then anything I send afterward can actually be relevant to your members. What does your schedule look like next week?"
    )

    st.markdown("**Quick activity tracker**")
    current = st.session_state.group_affinity_activity.get(org, {"status": "Not contacted", "notes": ""})
    a1, a2 = st.columns([1, 2])
    with a1:
        activity_status = st.selectbox(
            "Status",
            ["Not contacted", "Called - no answer", "Voicemail left", "Connected - follow up", "Meeting requested", "Meeting scheduled", "Not now", "Closed / no fit"],
            index=["Not contacted", "Called - no answer", "Voicemail left", "Connected - follow up", "Meeting requested", "Meeting scheduled", "Not now", "Closed / no fit"].index(current["status"]) if current["status"] in ["Not contacted", "Called - no answer", "Voicemail left", "Connected - follow up", "Meeting requested", "Meeting scheduled", "Not now", "Closed / no fit"] else 0,
            key=f"status_{org}",
        )
    with a2:
        activity_notes = st.text_input("Notes", value=current.get("notes", ""), key=f"notes_{org}")
    if st.button("Save call update", use_container_width=True):
        st.session_state.group_affinity_activity[org] = {"status": activity_status, "notes": activity_notes}
        st.success("Call update saved for this session.")

with scripts_tab:
    st.subheader("Light, meeting-first scripts")
    st.markdown("**Primary call**")
    st.code(
        "Hi [Name], this is Christopher Haake. I’m with New York Life here in Central Florida.\n\n"
        "I came across [Organization] while I was getting to know some of the stronger business and professional groups in the area, and I wanted to introduce myself.\n\n"
        "I’ve been looking at ways we may be able to bring some additional value to organizations like yours and their members — whether that’s around benefits, retirement and financial education, or some of the needs that come up for business owners and professionals.\n\n"
        "I’m really not trying to turn this into a sales call. I’d much rather stop by, learn a little more about what you’re doing and who your members are, and see if there’s anything that would actually make sense.\n\n"
        "Would you have 20 or 30 minutes sometime next week for me to come by and introduce myself?",
        language=None,
    )

    st.markdown("**Rushed version**")
    st.code(
        "No problem — I’ll keep it very simple. I’d just like to introduce myself and learn a little about the organization. If there’s a way New York Life can eventually be useful to your members, great. If not, I’ve still made a good local connection. Would there be a good day for me to stop by for 20 minutes?",
        language=None,
    )

    st.markdown("**Voicemail**")
    st.code(
        "Hi [Name], this is Christopher Haake with New York Life here in Central Florida. I came across [Organization] recently and wanted to introduce myself. I’m looking at ways we may be able to provide some additional value to local organizations and their members, and I’d really just like to learn more about what you’re doing. I’m not looking to pitch you over the phone. I’d love to stop by for 20 minutes, introduce myself and learn a little more about the organization. You can reach me at [number]. Again, Christopher Haake with New York Life. I look forward to speaking with you.",
        language=None,
    )

    st.markdown("**Short follow-up email after voicemail / connection**")
    st.code(
        "Hi [Name],\n\nI wanted to follow up on my call and introduce myself. I’m with New York Life here in Central Florida, and I’ve been getting to know more of the business and professional organizations in the area. [Organization] caught my attention because [one specific reason].\n\nI’m not looking to send you a generic benefits pitch. I’d rather stop by, learn a little more about your membership and what you are focused on, and see whether there is any way we could be useful to the organization or its members.\n\nWould you have 20 or 30 minutes next week for me to come by?\n\nBest,\nChristopher Haake",
        language=None,
    )

with meeting_tab:
    st.subheader("In-person discovery framework")
    st.caption("This is where the deeper questions belong — after the phone call has earned the meeting.")
    st.markdown(
        """
**Open conversationally**

- How did the organization get started, and what are you most focused on growing or improving right now?
- Who makes up the membership today — mostly owners, employers, professionals, employees, or a mix?
- What do members tend to ask the organization for that is hard to provide today?

**Understand the current benefit landscape**

- What kinds of member benefits, educational resources or financial programs do you already offer?
- Are those handled at the organization level, through individual member companies, or mainly left to members themselves?
- Are there areas where members consistently seem underserved?

**Explore without pitching**

- Would financial education or retirement resources be useful to the membership?
- Do many member businesses ask about employee retention, benefits, succession, or protecting key people?
- Is there interest in giving members access to resources they could choose to use individually without the organization taking on a major administrative burden?

**Decision process**

- If we eventually found something worthwhile, who else would normally need to be involved?
- Are there board meetings, renewal cycles, annual planning periods or membership events we should work around?

**Close the meeting**

"That gives me enough to do some homework. I don’t want to force a fit or bring you a generic presentation. Let me take what you’ve told me, make sure anything I come back with is actually appropriate and available, and then we can decide whether there is anything worth pursuing."
"""
    )

with compliance_tab:
    st.subheader("Compliance and eligibility guardrails")
    st.warning(
        "New organizations may be excellent relationship targets while not yet qualifying for every association insurance pathway. Relationship value and immediate product eligibility must be scored separately."
    )
    st.markdown(
        """
- Treat QuickDecision as a process, not a product.
- Do not make blanket **no medical exam** claims unless explicitly permitted for the specific product/case and required disclosures are used.
- Custom marketing descriptions remain **DRAFT/HOLD** until required SMRU review/approval is documented.
- Verify product, state and case availability before discussing faster-decision, underwriting or benefit claims.
- Do not promise that group coverage is cheaper, that an organization qualifies, or that a particular member count automatically establishes eligibility.
- Verify the legal organization, formation date, bylaws, membership classes, policyholder/sponsor authority and current benefit/vendor relationships before proposing an association-level structure.
- Where local chapters belong to national organizations, determine whether the local chapter or parent entity has authority to sponsor any program.
- Keep initial outreach focused on networking, member value, education and discovery. Product-specific presentations come only after the case is validated.

**Florida pathway note:** different statutory and product pathways can use different membership, organizational-purpose and existence requirements. Do not reduce eligibility to a single universal “10-member,” “15-member,” “2-year,” or “5-year” rule. Confirm the actual structure for the proposed case before representation.
"""
    )
