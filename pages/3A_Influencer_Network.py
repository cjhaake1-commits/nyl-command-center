from __future__ import annotations

import pandas as pd
import streamlit as st

from data.marketing_network_leads import MARKETING_NETWORK_LEADS

st.set_page_config(page_title="Influencer & Referral Network", page_icon="📱", layout="wide")

st.title("Influencer & Referral Network")
st.caption(
    "Central Florida social-media, real-estate, home, design, lifestyle and community accounts selected for audience fit, reach and referral-network potential."
)

st.warning(
    "Any paid promotion, testimonial, endorsement, influencer compensation or referral arrangement involving financial services must follow NYL/carrier compliance before execution."
)

df = pd.DataFrame(MARKETING_NETWORK_LEADS)

if df.empty:
    st.info("No influencer or referral-network candidates loaded yet.")
    st.stop()

c1, c2, c3 = st.columns(3)
c1.metric("Accounts / creators", len(df))
c2.metric("Very-high referral potential", int((df["Referral potential"] == "Very High").sum()))
c3.metric("Audience-fit 95+", int((pd.to_numeric(df["Audience fit score"], errors="coerce") >= 95).sum()))

q = st.text_input("Search names, handles, categories or markets")
view = df.copy()
if q.strip():
    mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
    view = view[mask]

view = view.sort_values(["Audience fit score", "Reach score"], ascending=[False, False], kind="stable")

st.subheader("Accounts We Selected")
st.caption("The rationale column explains why each account made the list; Best angle describes the most natural relationship or collaboration path.")

cols = [
    "Name",
    "Brand",
    "Category",
    "Area",
    "Audience size",
    "Audience fit score",
    "Reach score",
    "Referral potential",
    "Why fit",
    "Best angle",
    "Verified date",
    "Source URL",
]
st.dataframe(view[[c for c in cols if c in view.columns]], width="stretch", hide_index=True)

st.subheader("Top Relationship Targets")
for _, row in view.head(10).iterrows():
    with st.expander(f"{row['Name']} — {row['Brand']} | Fit {row['Audience fit score']}/100"):
        st.write(f"**Category:** {row['Category']}")
        st.write(f"**Market:** {row['Area']}")
        st.write(f"**Audience:** {row['Audience size']}")
        st.write(f"**Why we picked them:** {row['Why fit']}")
        st.write(f"**Best relationship angle:** {row['Best angle']}")
        st.write(f"**Referral potential:** {row['Referral potential']}")
        st.write(f"**Verified:** {row['Verified date']}")
        st.link_button("Open research source", row["Source URL"], width="stretch")

st.divider()
st.caption(
    "Follower counts are time-stamped public estimates and should be rechecked before campaign decisions. Selection emphasizes Central Florida audience relevance and referral quality, not follower count alone."
)
