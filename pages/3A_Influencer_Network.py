from __future__ import annotations

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from data.marketing_network_leads import MARKETING_NETWORK_LEADS

st.set_page_config(page_title="Influencer Network | Chris Haake", page_icon="📱", layout="wide")

brand_hero(
    "Influencer & Referral Network",
    "Build relationships with Central Florida creators and community connectors whose audiences naturally overlap homeowners, movers, affluent families, investors and business owners.",
    "Chris Haake • Marketing & Network",
)

st.warning("Compliance gate: paid promotion, testimonials, endorsements, influencer compensation or referral arrangements involving financial services require NYL/carrier approval before execution.")

df = pd.DataFrame(MARKETING_NETWORK_LEADS)
if df.empty:
    st.info("No influencer or referral-network candidates loaded yet.")
    st.stop()

fit = pd.to_numeric(df["Audience fit score"], errors="coerce")
reach = pd.to_numeric(df["Reach score"], errors="coerce")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Network Candidates", len(df))
c2.metric("Fit 95+", int((fit >= 95).sum()))
c3.metric("Reach 90+", int((reach >= 90).sum()))
c4.metric("Very High Referral", int((df["Referral potential"] == "Very High").sum()))

st.subheader("Relationship Shortlist")
q1, q2, q3 = st.columns([1.3, 1, 1])
q = q1.text_input("Search", placeholder="Name, handle, category, market...")
min_fit = q2.slider("Minimum audience fit", 0, 100, 80)
referral_levels = sorted(df["Referral potential"].dropna().astype(str).unique())
selected_referral = q3.multiselect("Referral potential", referral_levels, default=referral_levels)

view = df.copy()
view = view[pd.to_numeric(view["Audience fit score"], errors="coerce") >= min_fit]
if selected_referral:
    view = view[view["Referral potential"].astype(str).isin(selected_referral)]
if q.strip():
    mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
    view = view[mask]
view = view.sort_values(["Audience fit score", "Reach score"], ascending=[False, False], kind="stable")

st.markdown("### Top Relationship Targets")
for _, row in view.head(8).iterrows():
    title = f"{row['Name']} • {row['Brand']}  |  Fit {row['Audience fit score']}/100"
    with st.expander(title):
        a, b, c = st.columns([1, 1, 1])
        a.metric("Audience Fit", f"{row['Audience fit score']}/100")
        b.metric("Reach", f"{row['Reach score']}/100")
        c.metric("Referral Potential", str(row["Referral potential"]))
        st.markdown(f"**Audience / account:** {row['Audience size']}  ")
        st.markdown(f"**Category:** {row['Category']} • **Market:** {row['Area']}")
        st.markdown(f"**Why we picked them:** {row['Why fit']}")
        st.markdown(f"**Best relationship angle:** {row['Best angle']}")
        st.caption(f"Verified {row['Verified date']}")
        if row.get("Source URL"):
            st.link_button("Open research source", row["Source URL"], width="stretch")

st.subheader("Full Network Intelligence")
cols = ["Name", "Brand", "Category", "Area", "Audience size", "Audience fit score", "Reach score", "Referral potential", "Why fit", "Best angle", "Verified date"]
st.dataframe(view[[c for c in cols if c in view.columns]], width="stretch", hide_index=True)

st.subheader("How to Use This Network")
a, b, c = st.columns(3)
with a:
    st.markdown("**Relationship First**")
    st.write("Meet through local events, shared businesses, community circles and genuine value exchange before proposing campaigns.")
with b:
    st.markdown("**Audience Before Followers**")
    st.write("A smaller luxury Realtor or designer with homeowner intent can outrank a mass lifestyle account with weak local conversion potential.")
with c:
    st.markdown("**Collaborate Carefully**")
    st.write("Favor educational events, community visibility and reciprocal introductions; route compensated or promotional activity through compliance.")

st.divider()
st.caption("Follower counts are time-stamped public estimates. Reverify audience size, geography and engagement before making campaign decisions.")
