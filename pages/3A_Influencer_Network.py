from __future__ import annotations

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from core.rep_profile import REP_NAME, TERRITORY_LABEL
from data.paul_market import MARKETING_NETWORK_LEADS
from data.paul_events import EVENTS

st.set_page_config(page_title=f"Influencer Network | {REP_NAME}", page_icon="📱", layout="wide")
brand_hero(
    "Influencer, Referral & Events Network",
    f"Build relationships with local creators, community connectors and live networking opportunities relevant to {TERRITORY_LABEL}.",
    f"{REP_NAME} • Marketing & Network",
)
st.warning("Paid promotion, testimonials, endorsements, influencer compensation or referral arrangements involving financial services require applicable approval before execution. Event attendance is relationship/research activity; solicitation remains subject to authorization and compliance review.")

network_tab, events_tab = st.tabs(["Referral Network", "Networking & Events"])

with network_tab:
    df = pd.DataFrame(MARKETING_NETWORK_LEADS)
    if df.empty:
        st.info("No separate Paul-specific referral-network candidates are loaded yet. Individual COIs are currently maintained in Prospect Discovery and Lead Lists to avoid double-counting. Chris Haake's Central Florida network is not used in this tenant.")
    else:
        st.dataframe(df, width="stretch", hide_index=True)

    st.subheader("How to Use This Network")
    a, b, c = st.columns(3)
    with a:
        st.markdown("**Relationship First**")
        st.write("Meet through legitimate local events, mutual business relationships and community circles before proposing campaigns.")
    with b:
        st.markdown("**Audience Before Followers**")
        st.write("Prioritize local relevance and relationship potential over raw follower count.")
    with c:
        st.markdown("**Collaborate Carefully**")
        st.write("Keep compensated or promotional activity inside approved compliance processes.")

with events_tab:
    st.subheader("Upcoming Simi Valley Networking & Community Events")
    st.caption("Dates, descriptions and source links are shown directly in the app. Verify details with the organizer before attending because schedules can change.")

    events_df = pd.DataFrame(EVENTS)
    if events_df.empty:
        st.info("No verified upcoming events are loaded.")
    else:
        event_types = ["All"] + sorted(events_df["Type"].dropna().unique().tolist())
        selected_type = st.selectbox("Filter by event type", event_types)
        shown = events_df if selected_type == "All" else events_df[events_df["Type"] == selected_type]

        for _, event in shown.iterrows():
            with st.container(border=True):
                st.markdown(f"### {event['Event']}")
                c1, c2, c3 = st.columns([1, 1, 2])
                c1.markdown(f"**Date**  \n{event['Date']}")
                c2.markdown(f"**Time**  \n{event['Time']}")
                c3.markdown(f"**Location**  \n{event['Location']}")
                st.markdown(f"**Organizer:** {event['Organizer']}")
                st.write(event["Description"])
                st.markdown(f"**Why it matters for Paul's practice:** {event['Why It Matters']}")
                st.link_button("Open official event/source page", event["Source"])

        st.download_button(
            "Download Upcoming Events (.csv)",
            events_df.to_csv(index=False).encode("utf-8-sig"),
            "Paul_Beck_Simi_Valley_Upcoming_Events.csv",
            "text/csv",
            use_container_width=True,
        )
