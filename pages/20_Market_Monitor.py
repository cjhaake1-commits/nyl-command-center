from __future__ import annotations

import streamlit as st

from core.branding import brand_hero

st.set_page_config(page_title="Market Monitor | Chris Haake", page_icon="📊", layout="wide")
brand_hero(
    "Market Monitor",
    "A current, source-linked briefing on major markets, Treasury rates, and market news.",
    "Chris Haake • New York Life",
)

from core.market_monitor import render_market_dashboard

render_market_dashboard()
