from __future__ import annotations

import streamlit as st
from core.rep_profile import REP_INITIALS, REP_NAME, TERRITORY_GROWTH_LABEL, TERRITORY_LABEL


def sidebar_brand() -> None:
    with st.sidebar:
        st.markdown(
            f"""
            <div class="brand-lockup">
              <div class="brand-crown">◆ &nbsp; NEW YORK LIFE &nbsp; ◆</div>
              <div class="brand-name">{REP_NAME.upper()}</div>
              <div class="brand-sub">ADVISOR COMMAND CENTER</div>
              <div class="brand-person">
                <div class="brand-avatar-placeholder">{REP_INITIALS}</div>
                <div>
                  <div class="brand-person-name">{REP_NAME}</div>
                  <div class="brand-person-role">New York Life • Advisor Growth OS</div>
                  <div class="brand-profile-status">{TERRITORY_LABEL}</div>
                </div>
              </div>
              <div class="brand-sidebar-note">
                <div class="brand-sidebar-note-label">{TERRITORY_GROWTH_LABEL}</div>
                <div class="brand-sidebar-note-copy">PROSPECT • PRIORITIZE • CONNECT • EXECUTE</div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
