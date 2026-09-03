from __future__ import annotations

import pandas as pd
import streamlit as st

from core.rep_profile import REP_NAME, TERRITORY_LABEL, TERRITORY_RADIUS_MILES, TERRITORY_ZIP

st.set_page_config(page_title=f"Mailing & Targeting | {REP_NAME}", page_icon="📬", layout="wide")
st.title("Mailing Lists & Geographic Targeting")
st.caption(f"{REP_NAME} • {TERRITORY_LABEL}")
st.warning("Campaigns remain draft-only until applicable NYL/carrier, legal, privacy, suppression and communications requirements are satisfied.")

business_plan, individual_plan, digital_plan = st.tabs(["Business Mail", "Individual / Household Mail", "Digital Geographic Strategy"])

with business_plan:
    st.subheader("Business prospecting lane")
    st.write("Prioritize verified businesses and professional practices operating inside the configured territory, especially owner-led firms, newer companies, growing teams and businesses with public continuity/succession signals.")
    st.info("Use public business contact information and approved data sources. Keep source, collection date and suppression/opt-out status with each record.")

with individual_plan:
    st.subheader("Configured territory")
    st.dataframe(pd.DataFrame([{
        "Center ZIP": TERRITORY_ZIP,
        "Market": "Simi Valley, CA",
        "Radius": f"{TERRITORY_RADIUS_MILES} miles",
        "Status": "Primary research territory",
    }]), width="stretch", hide_index=True)
    st.caption("Additional ZIP-level targeting should be added only after the local market list is verified rather than copied from the Central Florida tenant.")

with digital_plan:
    st.subheader("Geographic campaign planner")
    st.warning("Do not identify a specific person's IP address or link IP data to sensitive financial/insurance profiling. Use compliant platform/vendor geographic products instead.")
    st.write("Preferred sequence: compliant geographic awareness → consented response → verified lead → Salesforce-ready record → human review.")

st.divider()
st.subheader("Campaign Plan")
c1, c2 = st.columns(2)
with c1:
    campaign = st.text_input("Campaign name", "Simi Valley Territory Pilot")
    audience = st.selectbox("Audience", ["Business owners", "Executives / professionals", "Centers of influence", "Households", "Other"])
with c2:
    touches = st.number_input("Planned touches", min_value=1, max_value=12, value=5)
    horizon = st.selectbox("Campaign window", ["30 days", "60 days", "90 days"])
st.markdown(f"**{campaign}** — {audience} — {touches} planned touches over {horizon}.")
