from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import streamlit as st

from core.branding import brand_hero
from core.rep_profile import REP_NAME, TERRITORY_LABEL
from core.planner import FunnelAssumptions, build_plan, pace_status
from core.war_room import (
    adaptive_assumptions,
    build_daily_mission,
    build_weekly_mission,
    count_selling_days,
    funnel_health,
    weakest_link,
)
from data.db import (
    get_activity,
    init_db,
    persistent_storage_enabled,
    storage_backend,
    totals,
    upsert_daily_activity,
)

BUILD_VERSION = "2026-09-03 • Simi Valley Advisor Growth OS"

st.set_page_config(page_title=f"Daily War Room | {REP_NAME}", page_icon="🎯", layout="wide")
init_db()

brand_hero(
    "Daily War Room",
    "Turn the production goal into today's exact mission, track the funnel, and keep execution focused on the few actions that move revenue forward.",
    f"{REP_NAME} • {TERRITORY_LABEL}",
)

s1, s2, s3 = st.columns([1, 1, 2])
s1.success("WAR ROOM • ONLINE")
s2.info("PACE ENGINE • ACTIVE")
s3.caption(f"Build {BUILD_VERSION} • Compensation assumptions remain editable until verified against the official NYL plan.")

if persistent_storage_enabled():
    st.success("Activity storage is connected to persistent cloud storage.")
else:
    st.warning(
        f"Activity storage: {storage_backend()}. The War Room is operational, but history is not yet on persistent cloud storage."
    )

with st.sidebar:
    st.markdown("### 🎯 Mission Setup")
    commission_goal = st.number_input("Commission goal ($)", min_value=0.0, value=3000.0, step=250.0)
    goal_end_date = st.date_input("Goal deadline", value=date.today() + timedelta(days=29))
    selling_days = st.multiselect(
        "Selling days",
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        default=["Mon", "Tue", "Wed", "Thu", "Fri"],
    )
    active_days_remaining = max(1, count_selling_days(date.today(), goal_end_date, selling_days))
    period_days = max(1, (goal_end_date - date.today()).days + 1)

    st.divider()
    st.markdown("### ⚡ Performance Mode")
    execution_buffer_pct = st.slider("Execution buffer above minimum", 0, 50, 10, step=5)
    execution_buffer = 1 + execution_buffer_pct / 100
    record_multiplier = st.select_slider(
        "Primary target mode",
        options=[1.0, 1.25, 1.5, 2.0, 3.0],
        value=1.0,
        format_func=lambda x: "Gate" if x == 1.0 else f"{x:g}× Goal",
    )

    st.divider()
    st.markdown("### 📊 Funnel Assumptions")
    avg_commission = st.number_input("Avg. commission per placed sale ($)", min_value=1.0, value=750.0, step=50.0)
    close_rate = st.slider("Held appointment → sale", 1, 100, 30) / 100
    show_rate = st.slider("Booked → held", 1, 100, 75) / 100
    booking_rate = st.slider("Conversation → booked", 1, 100, 25) / 100
    contact_rate = st.slider("Outreach → conversation", 1, 100, 30) / 100

activity_totals = totals()
earned = float(activity_totals["commission"])
baseline = FunnelAssumptions(
    avg_commission_per_sale=avg_commission,
    close_rate=close_rate,
    show_rate=show_rate,
    booking_rate=booking_rate,
    contact_rate=contact_rate,
)
adaptive = adaptive_assumptions(activity_totals, baseline)
primary_goal = commission_goal * record_multiplier
plan = build_plan(primary_goal, earned, active_days_remaining, adaptive)

elapsed_days = max(0, 30 - period_days) if commission_goal == 3000 and period_days <= 30 else 0
pace = pace_status(primary_goal, earned, elapsed_days, max(1, elapsed_days + period_days))
daily = build_daily_mission(plan, execution_buffer)

week_end = min(goal_end_date, date.today() + timedelta(days=6))
selling_days_this_week = count_selling_days(date.today(), week_end, selling_days)
weekly = build_weekly_mission(plan, selling_days_this_week, execution_buffer)

st.subheader("Command Overview")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Primary Goal", f"${primary_goal:,.0f}")
c2.metric("Earned", f"${earned:,.0f}")
c3.metric("Remaining", f"${plan.remaining_commission:,.0f}")
c4.metric("Selling Days Left", active_days_remaining)
c5.metric("Pace", str(pace["status"]).title(), f"${float(pace['pace_delta']):,.0f} vs pace")

st.progress(min(1.0, earned / primary_goal) if primary_goal else 1.0)

st.markdown("### Today's Mission")
t1, t2, t3, t4, t5, t6 = st.columns(6)
t1.metric("Commission", f"${daily.commission:,.0f}")
t2.metric("Sales", daily.sales)
t3.metric("Held", daily.held_appointments)
t4.metric("Booked", daily.booked_appointments)
t5.metric("Conversations", daily.conversations)
t6.metric("Outreach", daily.outreach_attempts)

st.success(
    f"WINNING MISSION • {daily.outreach_attempts} outreach attempts → {daily.conversations} conversations → "
    f"{daily.booked_appointments} booked → {daily.held_appointments} held → {daily.sales} placed sale(s) • "
    f"Commission pace target ${daily.commission:,.0f}."
)

st.markdown("### This Week's Mission")
w1, w2, w3, w4, w5, w6 = st.columns(6)
w1.metric("Commission", f"${weekly.commission:,.0f}")
w2.metric("Sales", weekly.sales)
w3.metric("Held", weekly.held_appointments)
w4.metric("Booked", weekly.booked_appointments)
w5.metric("Conversations", weekly.conversations)
w6.metric("Outreach", weekly.outreach_attempts)

st.subheader("Adaptive Forecast")
a1, a2, a3, a4, a5 = st.columns(5)
a1.metric("Avg commission / sale", f"${adaptive.avg_commission_per_sale:,.0f}")
a2.metric("Close rate", f"{adaptive.close_rate:.0%}")
a3.metric("Show rate", f"{adaptive.show_rate:.0%}")
a4.metric("Booking rate", f"{adaptive.booking_rate:.0%}")
a5.metric("Contact rate", f"{adaptive.contact_rate:.0%}")
st.caption("The forecast blends actual performance with baseline assumptions so early results do not create wild swings.")

health = funnel_health(activity_totals, baseline)
weak = weakest_link(health)
st.subheader("Weakest-Link Detector")
health_rows = []
for m in health:
    is_money = "commission" in m.stage.lower()
    health_rows.append({
        "Stage": m.stage,
        "Actual": "—" if m.actual is None else (f"${m.actual:,.0f}" if is_money else f"{m.actual:.1%}"),
        "Target": f"${m.target:,.0f}" if is_money else f"{m.target:.1%}",
        "Sample": m.sample_size,
        "Status": m.status,
    })
st.dataframe(pd.DataFrame(health_rows), width="stretch", hide_index=True)
if weak:
    st.warning(f"Current weakest link: {weak.stage}. Attack this stage first because it is furthest below target.")
else:
    st.info("Log activity to activate the weakest-link detector.")

st.subheader("Goal → Required Production")
p1, p2, p3, p4, p5 = st.columns(5)
p1.metric("Sales needed", plan.sales_needed)
p2.metric("Held appts", plan.held_appointments_needed)
p3.metric("Booked appts", plan.booked_appointments_needed)
p4.metric("Conversations", plan.conversations_needed)
p5.metric("Outreach attempts", plan.outreach_attempts_needed)

st.subheader("Record-Setting Scenarios")
scenario_rows = []
for label, multiplier in [("Gate", 1.0), ("1.5× Goal", 1.5), ("2× Goal", 2.0), ("3× Goal", 3.0)]:
    sp = build_plan(commission_goal * multiplier, earned, active_days_remaining, adaptive)
    dm = build_daily_mission(sp, execution_buffer)
    scenario_rows.append({
        "Scenario": label,
        "Commission target": commission_goal * multiplier,
        "Sales needed": sp.sales_needed,
        "Held appts": sp.held_appointments_needed,
        "Conversations": sp.conversations_needed,
        "Outreach attempts": sp.outreach_attempts_needed,
        "Outreach/day": dm.outreach_attempts,
        "Conversations/day": dm.conversations,
    })
st.dataframe(pd.DataFrame(scenario_rows), width="stretch", hide_index=True)

st.subheader("Log Today's Actuals")
with st.form("daily_activity"):
    activity_date = st.date_input("Date", value=date.today())
    a1, a2, a3 = st.columns(3)
    outreach = a1.number_input("Outreach attempts", min_value=0, value=0, step=1)
    conversations = a2.number_input("Conversations", min_value=0, value=0, step=1)
    booked = a3.number_input("Appointments booked", min_value=0, value=0, step=1)
    a4, a5, a6 = st.columns(3)
    held = a4.number_input("Appointments held", min_value=0, value=0, step=1)
    sales = a5.number_input("Placed sales", min_value=0, value=0, step=1)
    commission = a6.number_input("Commission credited ($)", min_value=0.0, value=0.0, step=50.0)
    notes = st.text_area("Notes / lessons")
    submitted = st.form_submit_button("Save Day", type="primary")
    if submitted:
        upsert_daily_activity(
            str(activity_date), int(outreach), int(conversations), int(booked),
            int(held), int(sales), float(commission), notes
        )
        st.success("Daily activity saved. The remaining mission has been recalculated.")
        st.rerun()

history = get_activity()
if history:
    df = pd.DataFrame(history)
    st.subheader("Performance History")
    st.dataframe(df.drop(columns=["id"]), width="stretch", hide_index=True)

    chart_df = df[["activity_date", "commission"]].copy()
    chart_df["activity_date"] = pd.to_datetime(chart_df["activity_date"])
    chart_df["cumulative_commission"] = chart_df["commission"].cumsum()
    st.line_chart(chart_df.set_index("activity_date")[["cumulative_commission"]])

    csv = df.drop(columns=["id"]).to_csv(index=False).encode("utf-8")
    st.download_button("Export Activity CSV", csv, "paul_deck_activity.csv", "text/csv")

st.divider()
st.caption(
    f"{REP_NAME} Daily War Room • Personal productivity and production planning only. "
    "Keep regulated client information, recommendations, and communications in approved NYL systems and workflows."
)
