from __future__ import annotations

from datetime import date

import pandas as pd
import streamlit as st

from core.lead_readiness import evaluate_lead_readiness

from core.branding import brand_hero
from data.public_leads import PUBLIC_LEADS
from data.hnw_leads import HNW_LEADS
from data.marketing_network_leads import MARKETING_NETWORK_LEADS
from data.rollover_leads import ROLLOVER_LEADS, ROLLOVER_SCREEN, ROLLOVER_REVIEW_POINTS, ROLLOVER_OUTREACH

st.set_page_config(page_title="Prospect Discovery | Chris Haake", page_icon="🎯", layout="wide")

brand_hero(
    "Prospect Discovery",
    "A continuously growing Central Florida intelligence layer: business triggers, HNW and household signals, centers of influence, career transitions, and high-fit referral networks — all tied back to public evidence.",
    "Chris Haake • Intelligence Engine",
)

business_df = pd.DataFrame(PUBLIC_LEADS)
hnw_df = pd.DataFrame(HNW_LEADS)
marketing_df = pd.DataFrame(MARKETING_NETWORK_LEADS)
rollover_df = pd.DataFrame(ROLLOVER_LEADS)

# Readiness is separate from opportunity fit: it assesses public research completeness only.
# It never infers private need, assets, suitability, or willingness to transact.
_source_frames = [
    ("Business", business_df),
    ("HNW / COI", hnw_df),
    ("Retirement transition", rollover_df),
    ("Referral network", marketing_df),
]
def _norm(value):
    return "".join(ch.lower() for ch in str(value or "") if ch.isalnum())

_identity_rows = []
for _lane, _frame in _source_frames:
    for _, _row in _frame.iterrows():
        _tokens = set()
        _name = _norm(_row.get("Name", ""))
        if _name:
            _tokens.add("name:" + _name)
        for _field in ("Business email", "Email", "Public Contact", "Contact"):
            _v = _norm(_row.get(_field, ""))
            if _v and "@" in _v:
                _tokens.add("email:" + _v)
        for _field in ("Business phone", "Phone", "Public phone"):
            _v = "".join(ch for ch in str(_row.get(_field, "")) if ch.isdigit())
            if len(_v) >= 10:
                _tokens.add("phone:" + _v[-10:])
        _identity_rows.append(_tokens)
_token_counts = {}
for _tokens in _identity_rows:
    for _token in _tokens:
        _token_counts[_token] = _token_counts.get(_token, 0) + 1
_duplicate_tokens = {key for key, count in _token_counts.items() if count > 1}

def _row_is_duplicate(row):
    tokens = set()
    name = _norm(row.get("Name", ""))
    if name:
        tokens.add("name:" + name)
    for field in ("Business email", "Email", "Public Contact", "Contact"):
        value = _norm(row.get(field, ""))
        if value and "@" in value:
            tokens.add("email:" + value)
    for field in ("Business phone", "Phone", "Public phone"):
        value = "".join(ch for ch in str(row.get(field, "")) if ch.isdigit())
        if len(value) >= 10:
            tokens.add("phone:" + value[-10:])
    return bool(tokens & _duplicate_tokens)

def _annotate(frame, lane):
    rows = []
    for _, row in frame.iterrows():
        record = row.to_dict()
        result = evaluate_lead_readiness(record, today=date.today(), duplicate_in_catalog=_row_is_duplicate(record))
        record["Research lane"] = lane
        record["Lead readiness"] = result["status"]
        record["Readiness score"] = result["score"]
        record["Missing gates"] = result["missing_gates"]
        rows.append(record)
    return pd.DataFrame(rows)

business_df = _annotate(business_df, "Business / employer")
hnw_df = _annotate(hnw_df, "HNW / COI")
rollover_df = _annotate(rollover_df, "Retirement transition")
marketing_df = _annotate(marketing_df, "Referral network")

research_universe = pd.concat([frame for _, frame in _source_frames], ignore_index=True, sort=False) if _source_frames else pd.DataFrame()
# Rebuild from annotated tables so the visible queue uses exactly the same gate.
annotated_frames = [business_df, hnw_df, rollover_df, marketing_df]
research_universe = pd.concat(annotated_frames, ignore_index=True, sort=False)
prime_records = research_universe[research_universe["Lead readiness"].str.startswith("PRIME")] if not research_universe.empty else research_universe
reverify_records = research_universe[research_universe["Lead readiness"].str.startswith("REVERIFY")] if not research_universe.empty else research_universe
hold_records = research_universe[research_universe["Lead readiness"].str.startswith("HOLD")] if not research_universe.empty else research_universe

def num_high(df: pd.DataFrame, col: str, threshold: float) -> int:
    if df.empty or col not in df.columns:
        return 0
    return int((pd.to_numeric(df[col], errors="coerce") >= threshold).sum())

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Business Leads", len(business_df), f"{num_high(business_df, 'Opportunity score', 90)} score 90+")
c2.metric("HNW / COI", len(hnw_df), f"{num_high(hnw_df, 'Opportunity score', 95)} score 95+")
c3.metric("Rollover Signals", len(rollover_df), "former-employer career transitions")
c4.metric("Referral Network", len(marketing_df), f"{num_high(marketing_df, 'Audience fit score', 95)} fit 95+")
c5.metric("Research Cadence", "On-demand", "source checks shown below")

st.info("Evidence standard: public-source facts stay separate from planning hypotheses. Prefer warm introductions. Never infer private financial condition, retirement-plan participation, account balance, or rollover need from career or social-media signals.")

st.subheader("Prime prospect gate — human review before Salesforce")
st.caption(
    "A high opportunity score is not readiness. PRIME requires a specific public cause, a dated source no more than 30 days old, "
    "a current public contact route, an actionable next step, and no duplicate within these research catalogs. "
    "This is research completeness only—not evidence of client need, suitability, intent, or Salesforce clearance."
)
rc1, rc2, rc3 = st.columns(3)
rc1.metric("PRIME • review", len(prime_records), "passes current research gates")
rc2.metric("REVERIFY", len(reverify_records), "source date needs refresh")
rc3.metric("HOLD", len(hold_records), "missing evidence / contact / action / unique record")
st.caption(
    "Priority sourcing lanes: business owners and employers (key-person, continuity, executive and employee protection discovery; "
    "route group benefits and any worksite program through the approved NYL team); public career transitions for retirement-plan reviews; "
    "and HNW / COI introductions where protection, brokerage-eligible investments, or annuity conversations emerge from documented needs."
)
if len(prime_records):
    st.markdown("#### PRIME — ready for your review")
    prime_cols = ["Research lane", "Name", "Company", "Role", "Opportunity score", "Trigger", "Signal", "Warm path", "Business email", "Business phone", "Source URL", "Verified date", "Next action"]
    st.dataframe(prime_records[[col for col in prime_cols if col in prime_records.columns]], width="stretch", hide_index=True)
else:
    st.warning("No candidate currently passes every PRIME gate. Do not treat a high fit/opportunity score or a public wealth signal as a ready lead.")
if len(reverify_records):
    with st.expander(f"Reverify source dates ({len(reverify_records)})"):
        review_cols = ["Research lane", "Name", "Company", "Role", "Opportunity score", "Trigger", "Signal", "Business email", "Business phone", "Source URL", "Verified date", "Next action", "Missing gates"]
        ordered = reverify_records.sort_values(["Readiness score", "Opportunity score"], ascending=[False, False], kind="stable")
        st.dataframe(ordered[[col for col in review_cols if col in ordered.columns]].head(25), width="stretch", hide_index=True)
st.caption(
    "Before Salesforce upload, separately deduplicate against current CRM records and the complete Created / Updated / Rejected import history, "
    "confirm the required import schema, and use only NYL-approved outreach and review steps."
)

tab_business, tab_hnw, tab_rollover, tab_marketing = st.tabs(["Business Prospects", "HNW / Households & COIs", "401(k) / Former Employer", "Marketing / Referral Network"])

with tab_business:
    top_left, top_right = st.columns([1.5, 1])
    with top_left:
        st.markdown("### Business Intelligence")
        st.caption("Founder-led companies, registrations, expansions, hiring, contracts, chambers and other observable business triggers.")
    with top_right:
        q = st.text_input("Search business intelligence", key="business_search", placeholder="Name, company, industry, area, trigger...")
    view = business_df.copy()
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if not view.empty and "Opportunity score" in view.columns:
        view = view.sort_values(["Readiness score", "Opportunity score", "Warmth score"], ascending=[False, False, False], kind="stable")
    if view.empty:
        st.info("No business prospects match this view.")
    else:
        st.markdown("#### Priority Queue")
        for _, row in view.head(5).iterrows():
            with st.expander(f"{row.get('Name','')} • {row.get('Company','')} | Opportunity {row.get('Opportunity score','—')}"):
                a, b = st.columns([1.2, 1])
                a.write(f"**Why now:** {row.get('Why now','')}")
                a.write(f"**Trigger:** {row.get('Trigger','')}")
                b.write(f"**Warm path:** {row.get('Warm path','')}")
                b.write(f"**Next action:** {row.get('Next action','')}")
                if row.get("Source URL"):
                    st.caption(f"Source: {row.get('Source URL')}")
        preferred = ["Lead readiness", "Readiness score", "Missing gates", "Name", "Company", "Role", "Industry", "Area", "Opportunity score", "Warmth score", "Trigger", "Warm path", "Next action", "Verified date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

with tab_hnw:
    head, controls = st.columns([1.35, 1])
    with head:
        st.markdown("### Household & Influence Intelligence")
        st.caption("Documented founder ownership, philanthropy, family enterprise, investment activity and trusted-advisor relationships.")
    with controls:
        q = st.text_input("Search households / COIs", key="hnw_search", placeholder="Name, organization, area, signal...")
    lead_types = sorted(str(x) for x in hnw_df.get("Lead type", pd.Series(dtype=str)).dropna().unique())
    selected_types = st.multiselect("Relationship lane", lead_types, default=lead_types, key="hnw_types")
    view = hnw_df.copy()
    if selected_types and "Lead type" in view.columns:
        view = view[view["Lead type"].astype(str).isin(selected_types)]
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if not view.empty and "Opportunity score" in view.columns:
        view = view.sort_values(["Readiness score", "Opportunity score", "Warmth score"], ascending=[False, False, False], kind="stable")
    if view.empty:
        st.info("No HNW / COI records match this view.")
    else:
        st.markdown("#### Highest-Leverage Relationships")
        cards = st.columns(3)
        for i, (_, row) in enumerate(view.head(3).iterrows()):
            with cards[i]:
                st.metric(str(row.get("Name", "Prospect")), f"{row.get('Opportunity score','—')}/100", str(row.get("Lead type", "")))
                st.caption(str(row.get("Signal", "")))
        preferred = ["Lead readiness", "Readiness score", "Missing gates", "Lead type", "Name", "Company", "Role", "Area", "Signal", "Signal strength", "Opportunity score", "Warmth score", "Warm path", "Next action", "Verified date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

with tab_rollover:
    st.markdown("### Former-Employer Retirement Plan Signals")
    st.caption("Find public career transitions where a person left an employer with 100+ employees after 3+ years. This is a reason to offer a retirement-plan review, not evidence that a 401(k) exists or that a rollover is appropriate.")

    r1, r2, r3, r4 = st.columns(4)
    r1.metric("Former employer size", f"{ROLLOVER_SCREEN['former_employer_min_headcount']}+")
    r2.metric("Minimum tenure", f"{ROLLOVER_SCREEN['former_employer_min_tenure_years']:.0f}+ years")
    r3.metric("Preferred recency", f"{ROLLOVER_SCREEN['preferred_change_recency_months']} months")
    r4.metric("Geography", "Central Florida")

    st.warning("Do not say or imply that leaving an old employer plan is a mistake. A participant may reasonably keep assets in the old plan, move them to a new employer plan if permitted, roll to an IRA, or take a distribution. Any recommendation must compare the actual alternatives, costs, investments, services, tax effects and protections.")

    q = st.text_input("Search rollover signals", key="rollover_search", placeholder="Name, former employer, new employer, title, area...")
    view = rollover_df.copy()
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if view.empty:
        st.info("No verified rollover-signal leads have been added yet. Research uses public LinkedIn/Facebook professional information, company bios and career announcements; private social content is excluded.")
    else:
        preferred = ["Lead readiness", "Readiness score", "Missing gates", "Name", "Current Company", "Current Role", "Former Employer", "Former Role", "Former Employer Size", "Tenure Years", "Change Date", "Area", "Public Contact", "Signal", "Source URL", "Verified Date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

    st.markdown("#### Dossier review points")
    for item in ROLLOVER_REVIEW_POINTS:
        st.write(f"- {item}")

    st.markdown("#### Meeting-first outreach")
    st.text_area("Phone", ROLLOVER_OUTREACH["phone"], height=190, key="rollover_phone")
    st.text_area("Email", ROLLOVER_OUTREACH["email"], height=280, key="rollover_email")

with tab_marketing:
    head, controls = st.columns([1.35, 1])
    with head:
        st.markdown("### Referral Audience Intelligence")
        st.caption("Creators and community accounts selected for Central Florida homeowner, mover, investor, affluent-family and business-owner audience overlap.")
    with controls:
        q = st.text_input("Search referral network", key="marketing_search", placeholder="Creator, handle, category, market...")
    view = marketing_df.copy()
    if q.strip() and not view.empty:
        mask = view.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        view = view[mask]
    if not view.empty and "Audience fit score" in view.columns:
        view = view.sort_values(["Readiness score", "Audience fit score", "Reach score"], ascending=[False, False, False], kind="stable")
    if view.empty:
        st.info("No marketing/referral records match this view.")
    else:
        st.markdown("#### Top Audience Matches")
        cards = st.columns(3)
        for i, (_, row) in enumerate(view.head(3).iterrows()):
            with cards[i]:
                st.metric(str(row.get("Name", "Creator")), f"{row.get('Audience fit score','—')}/100", str(row.get("Audience size", "")))
                st.caption(str(row.get("Why fit", "")))
        preferred = ["Lead readiness", "Readiness score", "Missing gates", "Name", "Brand", "Category", "Area", "Audience size", "Audience fit score", "Reach score", "Referral potential", "Why fit", "Best angle", "Verified date"]
        st.dataframe(view[[c for c in preferred if c in view.columns]], width="stretch", hide_index=True)

st.divider()
st.caption("Research inputs only. Confirm source accuracy and applicable consent, privacy, do-not-contact, platform, licensing, fiduciary/rollover and NYL communications requirements before outreach or campaign execution.")
