from __future__ import annotations

from datetime import date, datetime, timedelta
from math import ceil
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

from core.orlando_market import NETWORKING_ORGANIZATIONS, ORLANDO_PRIORITY_AREAS

st.set_page_config(page_title="First-Year $1M Growth Plan", page_icon="🏆", layout="wide")

today = datetime.now(ZoneInfo("America/New_York")).date()
anticipated_start = today + timedelta(days=10)
goal = 1_000_000

st.title("First-Year $1M Growth Plan")
st.caption(
    "A stretch operating plan for the first 12 months after your NYL contract trigger. "
    "This is a production target and planning model, not a forecast, promise, or NYL compensation illustration."
)

with st.sidebar:
    st.header("Planning assumptions")
    start_date = st.date_input(
        "Anticipated contract trigger",
        value=anticipated_start,
        help="Expected by October 31, 2026. Replace this with the actual trigger date once confirmed.",
    )
    production_weeks = st.number_input(
        "Active production weeks in year one",
        min_value=1,
        max_value=52,
        value=50,
        step=1,
        help="Planning assumption that leaves time for onboarding, holidays, and non-selling work.",
    )
    avg_case_commission = st.number_input(
        "Illustrative credited commission per placed case ($)",
        min_value=100.0,
        max_value=100000.0,
        value=5000.0,
        step=500.0,
        help="Replace with a defensible blended figure from your official NYL compensation materials. This is not a NYL rate.",
    )
    contact_rate = st.slider("Outreach attempt → conversation", 1, 100, 30) / 100
    booking_rate = st.slider("Conversation → appointment booked", 1, 100, 25) / 100
    show_rate = st.slider("Booked → held appointment", 1, 100, 75) / 100
    close_rate = st.slider("Held appointment → placed case", 1, 100, 30) / 100

try:
    first_year_end = date(start_date.year + 1, start_date.month, start_date.day)
except ValueError:
    first_year_end = date(start_date.year + 1, 3, 1)

weekly_goal = goal / production_weeks
monthly_equivalent = goal / 12
selling_days_per_week = 5
daily_goal = weekly_goal / selling_days_per_week
cases_year = ceil(goal / avg_case_commission)
cases_week = cases_year / production_weeks
held_week = ceil(cases_week / close_rate)
booked_week = ceil(held_week / show_rate)
conversations_week = ceil(booked_week / booking_rate)
outreach_week = ceil(conversations_week / contact_rate)

st.success(
    f"North star: $1,000,000 in credited first-year commission • "
    f"planning window {start_date:%b %d, %Y} to {first_year_end:%b %d, %Y}"
)
st.caption(
    f"At {production_weeks} active production weeks, the straight-line pace is "
    f"${weekly_goal:,.0f}/week, ${monthly_equivalent:,.0f}/month, and "
    f"${daily_goal:,.0f}/selling day over a five-day week."
)

st.subheader("Commission math — replace assumptions with your actual contract economics")
m1, m2, m3, m4 = st.columns(4)
m1.metric("First-year target", f"${goal:,.0f}", "credited commission")
m2.metric("Weekly pace", f"${weekly_goal:,.0f}", f"{production_weeks} active weeks")
m3.metric("Illustrative paid cases", f"{cases_year:,}", f"at ${avg_case_commission:,.0f} each")
m4.metric("Illustrative cases / week", f"{cases_week:.1f}", "case-size assumption")

scenario_rows = []
for case_commission in (2500, 5000, 10000):
    cases = ceil(goal / case_commission)
    scenario_rows.append(
        {
            "Average credited commission per placed case (illustrative)": f"${case_commission:,.0f}",
            "Placed cases needed in year": cases,
            "Cases per active week": f"{cases / production_weeks:.1f}",
        }
    )
st.dataframe(pd.DataFrame(scenario_rows), width="stretch", hide_index=True)
st.caption(
    "These scenarios are arithmetic only. Premium, assets transferred, sales count, or a product label does not equal "
    "commission credited. Confirm commission basis, timing, chargebacks, persistency rules, and case credit with your "
    "official contract and field leadership. Measure paid/credited results against the official report."
)

st.subheader("Weekly funnel model")
st.caption(
    "Starting assumptions only. Replace each conversion rate with your own observed results; volume never overrides fit, "
    "permission, suitability, or lead quality."
)
f1, f2, f3, f4, f5 = st.columns(5)
f1.metric("Permission-based outreach attempts", f"{outreach_week:,}", "per week")
f2.metric("Conversations", f"{conversations_week:,}", "per week")
f3.metric("Appointments booked", f"{booked_week:,}", "per week")
f4.metric("Appointments held", f"{held_week:,}", "per week")
f5.metric("Placed cases", f"{cases_week:.1f}", "per week, illustrative")
st.info(
    "The math shows how demanding the goal is under the selected assumptions. It does not establish that the goal is "
    "attainable. Validate average credited commission and conversion rates with the office before treating this pace as a forecast."
)

st.subheader("Product and business lanes to focus")
st.caption(
    "Based on your prior work on whole-life conversations, retirement/401(k) rollover analysis, annuity fee comparisons, "
    "and fund allocation. Prioritize documented client needs and sustainable relationships—not payout."
)
product_lanes = [
    {
        "Lane": "Individual protection",
        "NYL capabilities": "Term and permanent life insurance, including whole life and universal-life options; individual disability and long-term-care coverage.",
        "Best-fit discovery": "Families, business owners, and professionals with a documented protection, income-continuity, or care-planning question.",
        "Access gate": "Appropriate Florida insurance license, NYL appointment, product training, underwriting, and approved fact-finding.",
        "Role in plan": "Core relationship and protection lane; do not lead with a product or infer need from wealth/property.",
    },
    {
        "Lane": "Retirement income and annuities",
        "NYL capabilities": "Fixed and variable annuity options, subject to product availability and suitability.",
        "Best-fit discovery": "People who raise a documented retirement-income, longevity, or rollover question and want alternatives compared.",
        "Access gate": "Insurance license/appointment for insurance contracts; variable contracts also require active securities registration and firm/product approval.",
        "Role in plan": "A focused lane because you have worked through rollover and annuity comparisons; never assume an annuity is the default destination.",
    },
    {
        "Lane": "Investment-company securities",
        "NYL capabilities": "Series 6 limited products include mutual funds, variable annuities, variable life, UITs, and municipal fund securities such as 529 plans.",
        "Best-fit discovery": "Investment or education-funding conversations only within the approved NYLIFE Securities platform and documented customer profile.",
        "Access gate": "Active NYLIFE Securities association/registration in the state, firm approval, product authorization, supervision, and applicable disclosures.",
        "Role in plan": "Use your new Series 6/63 within its actual scope. Series 63 is state-law qualification; it does not expand the Series 6 product menu.",
    },
    {
        "Lane": "Business-owner and executive planning",
        "NYL capabilities": "Protection, continuity, disability, retirement, and benefits discussions coordinated with qualified NYL specialists.",
        "Best-fit discovery": "Owner-led firms and professional practices with a public business event or a need the owner confirms in conversation.",
        "Access gate": "Coordinate with the office's advanced-planning, retirement, and benefits resources; confirm who owns the case and how credit is assigned.",
        "Role in plan": "Strong relationship lane for your business-operations background; build multi-person relationships instead of one-product pitches.",
    },
    {
        "Lane": "Group and employer benefits",
        "NYL capabilities": "NYL Group Benefit Solutions offers employer and employee benefits, including group life/AD&D, disability, leave, and voluntary benefits.",
        "Best-fit discovery": "Employers, associations, and professional groups with a verified benefits decision cycle.",
        "Access gate": "Route to the appointed NYL GBS/broker or institutional team. Do not imply your individual contract lets you quote or place group coverage.",
        "Role in plan": "Strategic referral and introduction lane; agree internally on handoff, licensing, and commission/production credit first.",
    },
]
st.dataframe(pd.DataFrame(product_lanes), width="stretch", hide_index=True)

with st.expander("Registration boundary to keep visible in every review"):
    st.write(
        "FINRA describes Series 6 as a limited representative qualification. NYLIFE Securities states that its "
        "financial services professionals may not solicit or recommend general securities such as individual stocks and bonds. "
        "Passing exams alone does not establish active registration, state approval, firm association, insurance appointment, "
        "or product authorization. Confirm current status and scope in NYL/NYLIFE Securities systems before any securities activity."
    )
    st.markdown(
        "- [FINRA Series 6 scope](https://www.finra.org/registration-exams-ce/qualification-exams/series6)  \n"
        "- [FINRA Series 63 overview](https://www.finra.org/registration-exams-ce/qualification-exams/series63)  \n"
        "- [NYLIFE Securities products and disclosures](https://www.newyorklife.com/securities/products)  \n"
        "- [NYL protection products](https://www.newyorklife.com/products/insurance)  \n"
        "- [NYL investments and annuities](https://www.newyorklife.com/products/investments)  \n"
        "- [NYL Group Benefit Solutions](https://www.newyorklife.com/group-benefit-solutions)"
    )

st.subheader("Where to focus first")
st.markdown(
    "**Most promising initial hypothesis:** start with warm relationships and business-owner/professional referrals, "
    "then build a repeatable retirement and protection discovery process. Your luxury and high-value sales background "
    "fits a service-led model; your operating and leadership experience gives you credible questions for owners. "
    "Test this against actual meetings and placed business each month."
)
segments = [
    {
        "Priority": 1,
        "Segment": "Warm relationships and introductions",
        "Why test first": "Your prior sales experience is strongest in trust, repeat business, and referral-led relationships.",
        "Opening motion": "Reconnect where permitted; offer a useful review or introduction, and ask about current priorities before discussing products.",
    },
    {
        "Priority": 2,
        "Segment": "Founder-led businesses and professional practices",
        "Why test": "Your business-operations background supports owner-level conversations about continuity, key people, and benefits.",
        "Opening motion": "Use a specific public business trigger, then ask permission for a short discovery conversation.",
    },
    {
        "Priority": 3,
        "Segment": "COIs: CPAs, estate/business attorneys, commercial bankers, benefits consultants, and M&A/business brokers",
        "Why test": "They encounter business transitions and planning questions; durable two-way value matters more than a quick referral request.",
        "Opening motion": "Lead with professional fit, shared education, and reliable follow-through; follow each organization's solicitation rules.",
    },
    {
        "Priority": 4,
        "Segment": "Executives and professionals nearing a documented transition",
        "Why test": "Your rollover and retirement-income research gives you a foundation for structured alternatives conversations.",
        "Opening motion": "Use an approved rollover comparison and neutral fact-finding; coordinate with securities/retirement specialists.",
    },
    {
        "Priority": 5,
        "Segment": "Employers, associations, and affinity groups",
        "Why test": "One employer relationship can create education and service opportunities across a group.",
        "Opening motion": "Find the right internal GBS or institutional partner before discussing plan design, quoting, or compensation.",
    },
]
st.dataframe(pd.DataFrame(segments), width="stretch", hide_index=True)

st.subheader("Central Florida territory and networking")
area_rows = [
    {
        "Rank": x["rank"],
        "Market": x["area"],
        "County": x["county"],
        "Relationship-development angle": x["primary_play"],
        "Public research source": x["source_url"],
    }
    for x in ORLANDO_PRIORITY_AREAS
]
st.dataframe(pd.DataFrame(area_rows), width="stretch", hide_index=True)
st.caption(
    "These are territory-planning ideas based on area-level public information, not a way to infer an individual's "
    "wealth, suitability, or insurance need."
)

org_rows = [
    {
        "Rank": x["rank"],
        "Organization": x["organization"],
        "Suggested approach": x["join_timing"],
        "Why it may fit": x["why"],
        "Research link": x["url"],
    }
    for x in NETWORKING_ORGANIZATIONS[:6]
]
st.dataframe(pd.DataFrame(org_rows), width="stretch", hide_index=True)
st.caption(
    "Visit before joining, confirm current membership cost/eligibility and NYL approval, and comply with each group's "
    "solicitation rules. Prioritize West Orange and Winter Park chambers, then test BNI chapters. Treat ACG as a "
    "relationship network and honor its non-solicitation policy."
)
st.markdown(
    "**Professional influencers to develop:** CPAs and tax professionals, estate/business attorneys, commercial bankers, "
    "benefits consultants and HR/payroll advisers, M&A/business brokers, commercial real-estate professionals, and "
    "community leaders. Build a two-way professional relationship; do not buy referrals or imply an endorsement."
)

st.subheader("Monday morning: set the week's mission")
week_start = today - timedelta(days=today.weekday())
st.caption(f"Planning week: Monday {week_start:%B %d, %Y} • 10-minute Monday review, 10-minute Friday closeout")
monday_rows = [
    {"Order": 1, "Monday priority": "Reconcile production", "Action": "Check official NYL credited-commission and case-status reports; separate submitted, issued, placed, paid, pending, and reversed business."},
    {"Order": 2, "Monday priority": "Protect near-term cases", "Action": "Prioritize client service, outstanding requirements, and compliant next steps on cases already in motion."},
    {"Order": 3, "Monday priority": "Fill qualified meetings", "Action": "Work warm introductions and the highest-quality cause-based prospects; confirm a dated next action for every active record."},
    {"Order": 4, "Monday priority": "Develop COIs", "Action": "Schedule useful professional conversations and one relationship-building event or introduction."},
    {"Order": 5, "Monday priority": "Improve one funnel stage", "Action": "Review actual conversations → booked → held → placed → credited results and choose one measurable experiment."},
]
st.dataframe(pd.DataFrame(monday_rows), width="stretch", hide_index=True)
st.info(
    f"Default weekly commission pace: ${weekly_goal:,.0f}. Each Monday, reconcile the actual pace in the official "
    "compensation report, then set the week's case and activity targets from your realized case economics and conversion data."
)

st.subheader("A strict lead gate: cause, contact, evidence, next action")
lead_gate = [
    {"Gate": "1 • Cause", "Pass standard": "A specific, current, public business/professional event or a permission-based referral explains why outreach is timely. Write the cause in one sentence."},
    {"Gate": "2 • Identity and contact", "Pass standard": "Confirm the decision-maker's identity and role plus at least one current, public, business-appropriate contact channel."},
    {"Gate": "3 • Evidence", "Pass standard": "Store the source URL, source date, verification date, and exact fact supporting the cause. A score or demographic signal alone is not evidence."},
    {"Gate": "4 • Fit", "Pass standard": "Record the segment and a tentative conversation topic as a hypothesis—not a conclusion that the person needs a product."},
    {"Gate": "5 • Deduplication", "Pass standard": "Check names, business, email, phone, prior imports, and existing Salesforce records, including records previously updated or rejected."},
    {"Gate": "6 • Action", "Pass standard": "Give the lead a permitted first step, owner, and dated follow-up. If there is no useful next action, do not count it as qualified."},
]
st.dataframe(pd.DataFrame(lead_gate), width="stretch", hide_index=True)
st.warning(
    "Hold or exclude records with no verifiable cause, stale or missing contact details, ambiguous identity, unsupported "
    "wealth/need assumptions, or a duplicate in the exclusion universe. Keep research candidates separate from validated "
    "net-new leads. Preserve the standing project rule: do not export a replacement batch until at least 1,000 leads pass "
    "the validation gate. Research may be prepared for review; the app does not auto-contact prospects."
)

st.subheader("30 / 60 / 90-day operating checkpoints")
checkpoints = [
    {"Window": "Before / first 30 days", "Focus": "Confirm contract trigger, commission definitions, active registrations, state/product appointments, approved systems, specialist handoffs, and actual case-credit rules. Test two relationship lanes."},
    {"Window": "Days 31–60", "Focus": "Use actual funnel data to compare warm introductions, owner/professional conversations, and retirement-transition opportunities. Remove weak sources; deepen the best COI relationships."},
    {"Window": "Days 61–90", "Focus": "Present a short scorecard to your manager: credited production, pipeline stage quality, meetings, conversion by source, compliance gates, and the next-quarter capacity plan."},
]
st.dataframe(pd.DataFrame(checkpoints), width="stretch", hide_index=True)

st.warning(
    "Commission goals can create conflicts of interest. Make recommendations only after approved fact-finding, "
    "suitability/best-interest review, required disclosures, and supervision. Do not use this tool to store client "
    "identifiers or confidential financial/health information. The app's public link and current storage status should "
    "be reviewed before entering any personal or client-level data."
)
