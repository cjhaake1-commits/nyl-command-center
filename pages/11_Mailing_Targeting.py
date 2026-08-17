from __future__ import annotations

import pandas as pd
import streamlit as st

st.title("Mailing Lists & Geographic Targeting")
st.caption("Central Florida prospecting planner for compliant direct mail and digital geographic campaigns. Verify all campaigns against carrier, NYL, platform, and applicable legal/compliance requirements before launch.")

zip_rows = [
    {"Priority":1,"ZIP":"34786","Market":"Windermere","Primary angle":"Affluent households / business owners","Opportunities":"Life insurance; estate & legacy conversations; retirement; business-owner planning"},
    {"Priority":2,"ZIP":"32836","Market":"Dr. Phillips / Southwest Orlando","Primary angle":"Affluent households / executives","Opportunities":"Life insurance; retirement; wealth/legacy conversations"},
    {"Priority":3,"ZIP":"32814","Market":"Baldwin Park","Primary angle":"Professionals / established households","Opportunities":"Life insurance; retirement; family protection"},
    {"Priority":4,"ZIP":"32789","Market":"Winter Park","Primary angle":"Affluent households / professionals / owners","Opportunities":"Life insurance; retirement; business-owner and legacy conversations"},
    {"Priority":5,"ZIP":"32804","Market":"College Park","Primary angle":"Professionals / established homeowners","Opportunities":"Life insurance; retirement; family protection"},
    {"Priority":6,"ZIP":"32751","Market":"Maitland","Primary angle":"Executives / professionals / business owners","Opportunities":"Life insurance; retirement; business-owner planning"},
]
zip_df = pd.DataFrame(zip_rows)

business_plan, individual_plan, ip_plan = st.tabs(["Business Mail", "Individual / Household Mail", "Digital & IP Strategy"])

with business_plan:
    st.subheader("Business prospecting lane")
    st.write("Prioritize locally operating firms, newer companies, owner-led companies, professional practices, firms with 10+ employees, and companies showing growth or succession/benefits needs.")
    st.markdown("**Suggested signals:** company age, employee count, hiring/growth, owner tenure, industry, public business contact information, weak benefits messaging, succession exposure, and public expansion events.")
    st.info("Use public business contact information and licensed/authorized data sources. Keep source, date collected, and opt-out/suppression status with each record.")

with individual_plan:
    st.subheader("Greater Orlando geographic priority list")
    st.dataframe(zip_df, use_container_width=True, hide_index=True)
    st.download_button("Export ZIP Target List (CSV)", zip_df.to_csv(index=False).encode("utf-8"), "orlando_mailing_targets.csv", "text/csv")
    st.markdown("**Direct-mail workflow:** ZIP → USPS carrier routes → income/age/household-size filters → campaign segment → approved creative → response tracking.")
    st.info("USPS Every Door Direct Mail can target carrier routes without requiring a named household list. For named/addressed lists, use properly licensed data and maintain suppression/opt-out controls.")

with ip_plan:
    st.subheader("Digital geographic / IP-assisted campaign planner")
    st.warning("Do not build or use a system that identifies a specific person's IP address or links an IP address to sensitive financial/insurance profiling. Use compliant advertising-platform or vendor-provided geographic/household campaign products instead.")
    st.markdown("**Preferred approach:** direct mail creates awareness → compliant geographic/radius digital advertising reinforces the message → landing page/QR/phone response creates a consented lead → lead is scored and routed into the prospecting pipeline.")
    st.markdown("**Campaign fields to track:** geography, audience source, creative, mail drop date, digital flight dates, impressions, landing-page visits, QR scans, calls, appointments, opportunities, placed business, cost, and ROI.")

st.divider()
st.subheader("Campaign Plan")
c1, c2 = st.columns(2)
with c1:
    campaign = st.text_input("Campaign name", "Greater Orlando Affluent Household Pilot")
    offer = st.selectbox("Primary conversation", ["Life Insurance", "Retirement Planning", "Business Owner Planning", "Estate / Legacy Conversation", "Multi-Service Review"])
with c2:
    touches = st.number_input("Planned touches", min_value=1, max_value=12, value=5)
    horizon = st.selectbox("Campaign window", ["30 days", "60 days", "90 days"])

st.markdown(f"**{campaign}** — {offer} — {touches} planned touches over {horizon}.")
st.caption("Recommended sequence: awareness mailer → digital reinforcement → value-oriented second touch → event/appointment invitation → follow-up. Avoid unapproved product claims or individualized financial conclusions before suitability/compliance review.")
