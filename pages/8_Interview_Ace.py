from __future__ import annotations

import pandas as pd
import streamlit as st

st.set_page_config(page_title="NYL Interview Ace", page_icon="🃏", layout="wide")

st.title("Final Interview Ace")
st.caption("A concise, compliance-minded operating plan to show you are ready to execute from day one.")

st.info(
    "Use this as a conversation aid, not a presentation you force into the interview. Lead with questions, listen to how the office actually operates, "
    "and use the system to demonstrate preparation when the moment is right."
)

st.subheader("30-Second Positioning")
st.write(
    "I have spent years in high-trust, high-consideration sales and business leadership. My plan is to bring that same discipline here: "
    "a narrow Greater Orlando target market, a clean Salesforce-driven pipeline, source-backed reasons to contact people, disciplined next actions, "
    "strong centers of influence, and a daily scorecard that lets me improve conversion instead of just adding random activity. "
    "I have built a planning sandbox for the process, but I would move live prospect/client workflows into whatever New York Life approves."
)

st.subheader("What I Want to Prove in Month One")
month_one = [
    {"Objective": "Get the environment approved", "Evidence": "Know the Salesforce workflow, approved channels, data sources, marketing process, AI rules and specialist resources"},
    {"Objective": "Build first 100 qualified accounts", "Evidence": "Owner-led growth companies, professional practices, COIs, real-estate/hospitality/construction operators, executives"},
    {"Objective": "Create weekly activity rhythm", "Evidence": "50-60 personalized touches, 10-12 meaningful conversations, 3-4 first meetings, 1-2 diagnostics"},
    {"Objective": "Keep pipeline clean", "Evidence": "100% of active records have a dated next action; replies and overdue tasks surface first"},
    {"Objective": "Use specialists early", "Evidence": "Bring field/advanced-planning resources into cases when complexity justifies it"},
    {"Objective": "Earn first implementations appropriately", "Evidence": "Facts first, recommendation second; no product-first pressure"},
    {"Objective": "Start compounding", "Evidence": "Service calendar, review cadence, COI follow-up and introductions only after value"},
]
st.dataframe(pd.DataFrame(month_one), width="stretch", hide_index=True)

st.subheader("Questions That Make the Plan Real")
questions = [
    "Which Salesforce-based environment will I actually use, and what fields/tasks/reports are required from day one?",
    "What email, phone, texting, social-media and scheduling tools are approved and archived for agents in this office?",
    "Which public-data, Sales Navigator, enrichment or prospecting tools are approved, and what information may be imported into Salesforce?",
    "What does the best first-30-day producer in this office do differently from the average new agent?",
    "What first-month production records or activity benchmarks has this office actually seen, and how were they achieved?",
    "How quickly can I get access to Marketing Central, approved campaign materials and local-event support?",
    "Which field consultants, advanced-planning specialists or product specialists should I learn to engage early?",
    "How do you want new agents to balance existing-house opportunities, referrals, public prospecting, seminars/events and personal-market activity?",
    "Which activities are managers willing to review weekly with me: calls, conversations, meetings, diagnostics, cases, persistency, or something else?",
    "What would you need to see from me in the first 30, 60 and 90 days to conclude that I am on a top-producer trajectory?",
    "What licenses/registrations should I prioritize after the initial insurance requirements if my goal is to grow into a broader planning relationship?",
    "Are there expenses, memberships, software or marketing costs I should not incur until the office confirms approval and reimbursement responsibility?",
]
for q in questions:
    st.write(f"• {q}")

st.subheader("What to Show If They Ask 'How Will You Prospect?' ")
prospecting = [
    {"Lane": "Owner-led businesses", "Method": "Public trigger + one relevant owner question + 20-minute diagnostic ask", "Proof of discipline": "Tier A/B/C score and dated next action"},
    {"Lane": "Professional practice owners", "Method": "CPA/attorney/banker/practice-network introductions plus public business research", "Proof of discipline": "Partner/key-person/retirement hypothesis is verified, not assumed"},
    {"Lane": "Centers of influence", "Method": "Professional-to-professional conversation; no referral ask on first contact", "Proof of discipline": "Small test: education session, relevant introduction or joint meeting"},
    {"Lane": "Events", "Method": "Preselect targets before attending; specific 24-hour follow-up", "Proof of discipline": "Stop attending groups that do not create qualified second meetings"},
    {"Lane": "Existing policyholders (after Salesforce access)", "Method": "Review-due and engaged relationships first", "Proof of discipline": "Holistic review and documented needs, not automatic upsell"},
]
st.dataframe(pd.DataFrame(prospecting), width="stretch", hide_index=True)

st.subheader("What the Command Center Automates")
automation = [
    "Reverse-engineers commission goal into sales, meetings, conversations and outreach",
    "Builds today's priority queue from due dates, replies, stages and pipeline hygiene",
    "Flags active records with no next date or overdue next steps",
    "Recommends the next owner/COI/event sequence step without auto-sending it",
    "Tracks first-100 account coverage and lead inventory gaps",
    "Logs touches/replies and refreshes recency",
    "Tracks weekly conversion and weakest-link performance",
    "Maintains Greater Orlando public-source, networking and marketing research",
    "Is structured for Salesforce activity de-duplication and internal-task refresh after authorized integration",
]
for item in automation:
    st.write(f"• {item}")

st.subheader("What It Deliberately Does NOT Automate")
st.write(
    "Cold-message blasting, recommendations, suitability decisions, underwriting judgments, unapproved marketing, or the close. "
    "The design principle is to automate queue management and preparation while keeping trust and regulated decisions human-led."
)

st.subheader("30 / 60 / 90-Day Commitments")
plan = [
    {"Window": "Days 1-30", "Focus": "Approved systems, first 100, weekly rhythm, first diagnostics/implementations", "Management question": "Which target and opening are converting?"},
    {"Window": "Days 31-60", "Focus": "Double down on top 1-2 acquisition lanes, run first owner workshop, deepen 3 productive COIs", "Management question": "Which niche beats baseline?"},
    {"Window": "Days 61-90", "Focus": "Service/review loop, introductions, repeat winning event/workshop, measure segment economics", "Management question": "Where should 60% of next-quarter capacity go?"},
]
st.dataframe(pd.DataFrame(plan), width="stretch", hide_index=True)

st.subheader("Interview Closing")
st.write(
    "I know a system does not create trust or sales by itself. What I want is a disciplined operating environment where every week teaches me something. "
    "If I earn the opportunity, I want to be coachable on your process, use the firm's systems correctly, and put enough focused activity behind it to find out how high I can set the bar in month one."
)

st.caption("Do not claim a record, income outcome, or product capability as guaranteed. Ask the office to validate its actual benchmarks, tools, approvals and compensation rules.")
