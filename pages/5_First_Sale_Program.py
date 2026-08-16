from __future__ import annotations

import pandas as pd
import streamlit as st

from core.master_playbook import (
    DAILY_TIME_BLOCKS,
    FIRST_100_COMPOSITION,
    FIRST_SALE_SPRINT,
    HEALTHY_CONVERSION_RANGES,
    PIPELINE_STAGES,
    TOUCH_SEQUENCES,
    TWELVE_WEEK_PLAN,
    WEEKLY_TARGETS,
)

st.set_page_config(page_title="NYL First-Sale Program", page_icon="🚀", layout="wide")

st.title("First-Sale Operating Program")
st.caption("Built from your Greater Orlando Prospecting Automation & First-Sale Program and companion control-center workbook.")

st.warning(
    "Planning sandbox only. New York Life systems should remain the system of record for live prospect/client information unless the firm expressly approves otherwise. "
    "Automate queues, reminders and recordkeeping; keep judgment, recommendations, and client communications human-led and firm-approved."
)

st.subheader("Weekly Operating Standard")
cols = st.columns(4)
items = list(WEEKLY_TARGETS.items())
for i, (key, value) in enumerate(items):
    label = key.replace("_", " ").title()
    cols[i % 4].metric(label, value)

st.subheader("First 100 Account Composition")
st.dataframe(pd.DataFrame(FIRST_100_COMPOSITION), width="stretch", hide_index=True)

st.subheader("Pipeline Architecture")
st.caption("Pipeline truth rule: every active opportunity needs a defined stage, exit criterion, dated next action, and accountable owner.")
st.dataframe(pd.DataFrame(PIPELINE_STAGES), width="stretch", hide_index=True)

st.subheader("Touch Sequences")
for sequence_name, rows in TOUCH_SEQUENCES.items():
    with st.expander(sequence_name, expanded=sequence_name == "Owner 14-Day"):
        st.dataframe(
            pd.DataFrame(rows, columns=["Timing", "Channel", "Action", "Stop condition"]),
            width="stretch",
            hide_index=True,
        )

st.subheader("Daily Time Blocks")
st.dataframe(
    pd.DataFrame(DAILY_TIME_BLOCKS, columns=["Time", "Block", "Minimum output"]),
    width="stretch",
    hide_index=True,
)

st.subheader("30-Day First-Sale Sprint")
st.dataframe(pd.DataFrame(FIRST_SALE_SPRINT), width="stretch", hide_index=True)

st.subheader("Healthy Conversion Ranges")
conversion_rows = [
    {
        "Conversion": name,
        "Healthy low": f"{low:.0%}",
        "Healthy high": f"{high:.0%}",
        "If below range": action,
    }
    for name, low, high, action in HEALTHY_CONVERSION_RANGES
]
st.dataframe(pd.DataFrame(conversion_rows), width="stretch", hide_index=True)

st.subheader("12-Week Implementation Calendar")
st.dataframe(
    pd.DataFrame(TWELVE_WEEK_PLAN, columns=["Week", "Primary build", "Field target", "Decision"]),
    width="stretch",
    hide_index=True,
)

st.success(
    "Quarter-one win condition: one narrow positioning statement, two acquisition channels, a reliable weekly activity rhythm, a clean CRM, "
    "three or more productive COIs, a repeatable diagnostic, and enough conversion data to decide what to scale."
)
