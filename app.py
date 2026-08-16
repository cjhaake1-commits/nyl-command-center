from __future__ import annotations

from datetime import date
import math

import pandas as pd
import streamlit as st

from core.planner import FunnelAssumptions, build_plan, pace_status
from data.db import get_activity, init_db, totals, upsert_daily_activity

st.set_page_config(page_title="NYL Command Center", page_icon="🎯", layout="wide")
init_db()

st.title("NYL Command Center")
st.caption("Goal-to-action planning for your first 30 days and beyond. Keep compensation assumptions editable until verified against your official NYL plan.")

with st.sidebar:
    st.header("Goal Setup")
    commission_goal = st.number_input("Commission goal ($)", min_value=0.0, value=3000.0, step=250.0)
    period_days = st.number_input("Goal period (calendar days)", min_value=1, value=30, step=1)
    elapsed_days = st.number_input("Days elapsed", min_value=0, max_value=int(period_days), value=0, step=1)
    active_days_remaining = st.number_input(
        "Active selling days remaining",
        min_value=1,
        value=max(1, int(period_days - elapsed_days)),
        step=1,
        help="Use the number of days you actually plan to prospect/sell, not just calendar days.",
    )

    st.divider()
    st.subheader("Funnel Assumptions")
    avg_commission = st.number_input("Avg. commission per placed sale ($)", min_value=1.0, value=750.0, step=50.0)
    close_rate = st.slider("Held appointment → sale", 1, 100, 30) / 100
    show_rate = st.slider("Booked → held", 1, 100, 75) / 100
    booking_rate = st.slider("Conversation → booked", 1, 100, 25) / 100
    contact_rate = st.slider("Outreach → conversation", 1, 100, 30) / 100

activity_totals = totals()
earned = float(activity_totals["commission"])
assumptions = FunnelAssumptions(
    avg_commission_per_sale=avg_commission,
    close_rate=close_rate,
    show_rate=show_rate,
    booking_rate=booking_rate,
    contact_rate=contact_rate,
)
plan = build_plan(commission_goal, earned, int(active_days_remaining), assumptions)
pace = pace_status(commission_goal, earned, int(elapsed_days), int(period_days))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Goal", f"${commission_goal:,.0f}")
c2.metric("Earned", f"${earned:,.0f}")
c3.metric("Remaining", f"${plan.remaining_commission:,.0f}")
c4.metric("Pace", str(pace["status"]).title(), f"${float(pace['pace_delta']):,.0f} vs pace")

st.progress(min(1.0, earned / commission_goal) if commission_goal else 1.0)

st.subheader("Goal → Required Production")
p1, p2, p3, p4, p5 = st.columns(5)
p1.metric("Sales needed", plan.sales_needed)
p2.metric("Held appts", plan.held_appointments_needed)
p3.metric("Booked appts", plan.booked_appointments_needed)
p4.metric("Conversations", plan.conversations_needed)
p5.metric("Outreach attempts", plan.outreach_attempts_needed)

st.subheader("Today's Minimum Winning Pace")
d1, d2, d3, d4, d5, d6 = st.columns(6)
d1.metric("Commission/day", f"${plan.daily_commission_target:,.0f}")
d2.metric("Sales/day", f"{plan.daily_sales_target:.2f}")
d3.metric("Held/day", f"{plan.daily_held_appointments:.1f}")
d4.metric("Booked/day", f"{plan.daily_booked_appointments:.1f}")
d5.metric("Conversations/day", f"{plan.daily_conversations:.1f}")
d6.metric("Outreach/day", f"{plan.daily_outreach_attempts:.1f}")

st.info(
    f"If these assumptions hold, the current plan calls for about {math.ceil(plan.daily_outreach_attempts)} outreach attempts, "
    f"{math.ceil(plan.daily_conversations)} live conversations, {math.ceil(plan.daily_booked_appointments)} booked appointments, "
    f"and {math.ceil(plan.daily_held_appointments)} held appointments per active selling day."
)

st.subheader("Record-Setting Scenarios")
scenario_rows = []
for label, multiplier in [("Gate", 1.0), ("Stretch", 1.5), ("2× Gate", 2.0), ("3× Gate", 3.0)]:
    sp = build_plan(commission_goal * multiplier, earned, int(active_days_remaining), assumptions)
    scenario_rows.append({
        "Scenario": label,
        "Commission target": commission_goal * multiplier,
        "Sales needed": sp.sales_needed,
        "Held appts": sp.held_appointments_needed,
        "Conversations": sp.conversations_needed,
        "Outreach attempts": sp.outreach_attempts_needed,
        "Outreach/day": round(sp.daily_outreach_attempts, 1),
    })
st.dataframe(pd.DataFrame(scenario_rows), use_container_width=True, hide_index=True)

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
    submitted = st.form_submit_button("Save day")
    if submitted:
        upsert_daily_activity(
            str(activity_date), int(outreach), int(conversations), int(booked),
            int(held), int(sales), float(commission), notes
        )
        st.success("Daily activity saved. Refreshing totals on your next interaction.")

history = get_activity()
if history:
    df = pd.DataFrame(history)
    st.subheader("Performance History")
    st.dataframe(df.drop(columns=["id"]), use_container_width=True, hide_index=True)

    chart_df = df[["activity_date", "commission"]].copy()
    chart_df["activity_date"] = pd.to_datetime(chart_df["activity_date"])
    chart_df["cumulative_commission"] = chart_df["commission"].cumsum()
    st.line_chart(chart_df.set_index("activity_date")[["cumulative_commission"]])

    csv = df.drop(columns=["id"]).to_csv(index=False).encode("utf-8")
    st.download_button("Export activity CSV", csv, "nyl_activity.csv", "text/csv")

st.divider()
st.caption(
    "MVP boundary: this tool is for personal productivity, goal planning, and performance tracking. "
    "Do not store client SSNs, account numbers, medical information, or other sensitive client data here. "
    "Keep product recommendations and regulated client communications in approved NYL systems and workflows."
)
