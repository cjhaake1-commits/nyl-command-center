from __future__ import annotations

from datetime import date, datetime, timedelta

import pandas as pd
import streamlit as st

from core.orlando_market import (
    NETWORKING_ORGANIZATIONS,
    NYL_REFERENCE_PAGES,
    OPEN_SOURCE_REFERENCE,
    ORLANDO_PRIORITY_AREAS,
    ORLANDO_PUBLIC_SOURCES,
    UPCOMING_NETWORKING_EVENTS,
)

st.set_page_config(page_title="NYL Marketing Command Center", page_icon="📣", layout="wide")

st.title("Marketing Command Center")
st.caption("Greater Orlando top-of-mind campaign planning: direct mail, digital, networking and relationship development.")

st.warning(
    "Compliance gate: all insurance/securities advertising, direct mail, social posts, landing pages and event invitations should remain draft-only until reviewed through NYL-approved compliance workflows. "
    "Do not use sensitive traits, inferred wealth, health information or financial distress to target individuals."
)

st.subheader("Greater Orlando Priority Markets")
areas_df = pd.DataFrame(ORLANDO_PRIORITY_AREAS)
areas_df["median_household_income"] = areas_df["median_household_income"].map(lambda x: f"${x:,.0f}")
st.dataframe(
    areas_df[["rank", "area", "county", "median_household_income", "primary_play", "source"]],
    width="stretch",
    hide_index=True,
)
st.caption("Income figures are area-level Census market-planning data, not estimates of any individual's income or net worth.")

st.subheader("90-Day Top-of-Mind Campaign")
area = st.selectbox("Primary market", [a["area"] for a in ORLANDO_PRIORITY_AREAS])
audience = st.selectbox(
    "Audience",
    [
        "Business owners",
        "Executives / professionals",
        "Centers of influence (CPA / attorney / banker / realtor)",
        "Homeowners / households",
        "Commercial real-estate relationships",
    ],
)
solution = st.selectbox(
    "Primary education theme",
    [
        "Protection / life planning",
        "Business-owner protection & continuity",
        "Retirement-income education",
        "Long-term-care education",
        "Estate / legacy planning",
        "Holistic planning / introductions",
    ],
)
weekly_budget = st.number_input("Illustrative weekly marketing budget ($)", min_value=0, value=250, step=50)

campaign_rows = [
    {
        "Week": "1",
        "Direct mail": "Intro letter / postcard: local planning resource + educational CTA",
        "Digital": "Launch compliant geographic/business-professional awareness campaign",
        "Relationship": "Identify 20 COIs + register for 1 priority networking event",
        "Pipeline action": "Add every response, referral and event contact for human follow-up",
    },
    {
        "Week": "2",
        "Direct mail": "No new drop; call/approved follow-up to responders where permitted",
        "Digital": "Educational short-form content + approved retargeting only where platform/firm rules permit",
        "Relationship": "5 COI introductions / coffees requested",
        "Pipeline action": "Prioritize engaged leads and overdue follow-ups",
    },
    {
        "Week": "3",
        "Direct mail": "Educational piece #2 tied to selected theme",
        "Digital": "Theme-specific awareness creative to same permitted geography/audience",
        "Relationship": "Attend chamber/BNI/ACG/COI event",
        "Pipeline action": "Tag source + event + market; schedule next action within 48 hours",
    },
    {
        "Week": "4",
        "Direct mail": "Thank-you / local resource card to qualified relationship leads",
        "Digital": "Top-of-mind content: FAQ / misconception / planning checklist",
        "Relationship": "Referral conversation with warm relationships",
        "Pipeline action": "Review conversion by source; cut low-yield activities",
    },
    {
        "Week": "5-6",
        "Direct mail": "Second-wave drop to fresh public-source/approved lead list",
        "Digital": "Refresh creative; keep frequency controlled",
        "Relationship": "Join/commit to highest-quality group after visits",
        "Pipeline action": "Build 5-day lead inventory and enforce daily next-action queue",
    },
    {
        "Week": "7-8",
        "Direct mail": "Invitation to educational review / event / checklist",
        "Digital": "Educational video/post series around selected planning theme",
        "Relationship": "Host or co-host educational conversation with approved COI",
        "Pipeline action": "Measure appointments per 100 names by source",
    },
    {
        "Week": "9-10",
        "Direct mail": "Credibility / process piece: what a planning conversation covers",
        "Digital": "Repeat strongest compliant message to winning geography/audience",
        "Relationship": "Deepen top 10 COI relationships",
        "Pipeline action": "Promote high-intent prospects; nurture non-ready contacts",
    },
    {
        "Week": "11-12",
        "Direct mail": "Quarter-end check-in / planning reminder",
        "Digital": "90-day recap / educational reminder",
        "Relationship": "Ask best advocates for introductions",
        "Pipeline action": "90-day source ROI review and next-quarter territory allocation",
    },
]
st.dataframe(pd.DataFrame(campaign_rows), width="stretch", hide_index=True)

st.markdown("#### Direct-Mail Draft Framework")
st.write(
    "Use mail primarily as a credibility and familiarity layer—not as a hard-close piece. A compliant draft should normally contain: "
    "local relevance, one clear educational problem, a short explanation of the planning conversation, an approved CTA, required disclosures/identity language, and no unapproved performance or product claims."
)

mail_theme = {
    "Business-owner protection & continuity": "If a key owner or employee were suddenly unavailable, would the business have enough time and liquidity to protect employees, customers and the owners' families?",
    "Protection / life planning": "A protection plan should evolve as your family, career, property and responsibilities change.",
    "Retirement-income education": "Retirement planning is not only about accumulating assets; it also involves turning resources into a durable income strategy.",
    "Long-term-care education": "A long-term-care plan is about preserving choices for care and reducing the financial burden on the people around you.",
    "Estate / legacy planning": "A coordinated legacy plan can help families and business owners clarify who receives what, when and how—alongside their legal and tax professionals.",
    "Holistic planning / introductions": "A useful planning relationship connects protection, accumulation, retirement and legacy decisions rather than treating them as isolated products.",
}[solution]

st.code(
    f"DRAFT — FOR NYL COMPLIANCE REVIEW\n\n"
    f"Greater Orlando / {area}\n"
    f"Audience: {audience}\n\n"
    f"Opening idea: {mail_theme}\n\n"
    "CTA: Offer a brief educational planning conversation or approved checklist/review.\n"
    "Do not mail until the final copy, disclosures, branding, list source and solicitation process are approved.",
    language="text",
)

st.markdown("#### Targeted Digital — Top-of-Mind Layer")
digital_rows = [
    {
        "Channel": "LinkedIn",
        "Use": "Professional/business visibility, company/job-function audiences where permitted, thought-leadership and COI content",
        "Avoid": "Sensitive-data targeting, inferred financial condition, unapproved testimonials/claims",
    },
    {
        "Channel": "Meta / Facebook / Instagram",
        "Use": "Geographic awareness and educational content under applicable financial-services ad-category rules",
        "Avoid": "Individual wealth inference, sensitive attributes, aggressive microtargeting or unapproved lead forms",
    },
    {
        "Channel": "Google Search",
        "Use": "Capture explicit planning intent around approved educational topics and local searches",
        "Avoid": "Personalized targeting based on financial hardship or other restricted consumer-finance signals",
    },
    {
        "Channel": "Organic social",
        "Use": "Consistent educational posts, event participation, local-business/community visibility, approved FAQs",
        "Avoid": "Product recommendations in public comments, confidential client stories or unapproved claims",
    },
]
st.dataframe(pd.DataFrame(digital_rows), width="stretch", hide_index=True)

suggested_split = {
    "Direct mail / print": round(weekly_budget * 0.40),
    "Digital awareness/search": round(weekly_budget * 0.35),
    "Networking/events": round(weekly_budget * 0.20),
    "Testing / reserve": round(weekly_budget * 0.05),
}
st.write("Illustrative weekly allocation (adjust once real conversion data exists):")
st.dataframe(pd.DataFrame([{"Bucket": k, "Budget": f"${v:,.0f}"} for k, v in suggested_split.items()]), width="stretch", hide_index=True)

st.divider()
st.subheader("Networking Organizations — Recommended Join Order")
org_df = pd.DataFrame(NETWORKING_ORGANIZATIONS)
st.dataframe(
    org_df[["rank", "organization", "score", "join_timing", "why", "caution"]],
    width="stretch",
    hide_index=True,
)

st.success(
    "Recommended first memberships/visits: West Orange Chamber first; Winter Park Chamber as the second geographic anchor; visit multiple BNI chapters before taking a category seat. "
    "Then add ACG Orlando for high-quality business/COI relationships. Estate Planning Council becomes especially valuable once your credentials make you eligible."
)

for org in NETWORKING_ORGANIZATIONS:
    st.link_button(f"Open {org['organization']}", org["url"], width="stretch")

st.subheader("Upcoming Networking Calendar")
st.caption("Rolling 60-day event view, using dated organizer listings. Research refreshed October 12, 2026. The calendar filters out past events automatically; it does not claim live verification of ticket availability.")
from pages_event_catalog import VERIFIED_NETWORKING_EVENTS
today = date.today()
horizon = today + timedelta(days=60)
events = []
for event in VERIFIED_NETWORKING_EVENTS:
    event_date = datetime.strptime(event["date"], "%Y-%m-%d").date()
    if today <= event_date <= horizon:
        item = dict(event)
        item["days_away"] = (event_date - today).days
        events.append(item)
events.sort(key=lambda x: (x["date"], -x["importance"]))
st.metric("Upcoming researched events (next 60 days)", len(events))
st.caption("Focus: introductions and referral partners · 401(k)/retirement planning · business-owner benefits. Source links are organizer listings; verify registration and attendance requirements.")
if events:
    st.dataframe(
        pd.DataFrame(events)[["date", "time", "event", "organization", "objective", "importance", "fit", "days_away", "url"]],
        width="stretch",
        hide_index=True,
        column_config={"url": st.column_config.LinkColumn("Organizer / RSVP")},
    )
    top_event = max(events, key=lambda x: x["importance"])
    st.info(f"Highest-priority event: {top_event['event']} on {top_event['date']} ({top_event['importance']}/100).")
    with st.expander("Event action plan — before, during, after", expanded=True):
        st.markdown("**Before:** Confirm details and register. Identify three potential referral-partner roles and two planning questions. **During:** Target five substantive conversations, two permission-based introductions and one potential discovery appointment. **Within 48 hours:** Follow up individually through NYL-approved channels, document the next action in the approved system, and review conversion. Do not enter confidential client details in this calendar.")
    st.page_link("pages/15_Event_Prospecting.py", label="Open Event Prospecting tracker", icon="🤝")
else:
    st.warning("No dated events in the next 60 days. The researched source list needs another refresh; this is not evidence that no local events exist.")
    st.page_link("pages/15_Event_Prospecting.py", label="Open Event Prospecting research tracker", icon="🤝")
st.caption("Freshness policy: event dates roll forward automatically. New discoveries require a verified source update; a weekly research check is scheduled separately. Never assume an event is still open for registration.")

st.divider()
st.subheader("Lead & Market Research Sources")
for source in ORLANDO_PUBLIC_SOURCES:
    st.markdown(f"**{source['name']} — {source['category']}**  \n{source['use']}")
    st.link_button(f"Open {source['name']}", source["url"], width="stretch")

st.subheader("NYL Public Positioning Research")
st.caption("Use these to understand NYL's public product/service language and local positioning. Do not copy another agent's wording or claims verbatim.")
for ref in NYL_REFERENCE_PAGES:
    st.markdown(f"**{ref['category']}: {ref['name']}** — {ref['takeaway']}")
    st.link_button(f"Open {ref['name']}", ref["url"], width="stretch")

st.subheader("Open-Source Industry Reference")
for ref in OPEN_SOURCE_REFERENCE:
    st.markdown(f"**{ref['name']}** — {ref['patterns']}  \nUse: {ref['use']}")
    st.link_button(f"Open GitHub — {ref['name']}", ref["url"], width="stretch")

st.divider()
st.caption(
    "Operating rule: public data can help identify markets, businesses and public professional signals, but public availability does not itself establish consent to every communication channel. "
    "Honor applicable do-not-call/opt-out rules, platform terms, privacy law, NYL advertising/communications review, and Salesforce/NYL system-of-record requirements."
)
