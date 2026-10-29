from __future__ import annotations

import streamlit as st
from core.rep_profile import REP_INITIALS, REP_NAME, TERRITORY_GROWTH_LABEL, TERRITORY_LABEL


def sidebar_brand() -> None:
    with st.sidebar:
        st.markdown(
            f"""
            <div class="brand-lockup">
              <div class="brand-crown">◆ &nbsp; NEW YORK LIFE &nbsp; ◆</div>
<div class="brand-team-row">
              <span class="brand-jet" aria-label="fighter jet">
                <svg viewBox="0 0 100 100" role="img" aria-hidden="true">
                  <path d="M50 3 57 29 88 45 88 52 59 46 56 73 70 86 70 92 50 88 30 92 30 86 44 73 41 46 12 52 12 45 43 29Z"/>
                  <path class="brand-jet-cockpit" d="m50 15 4 18h-8z"/>
                </svg>
              </span>
              <div>
                <div class="brand-team-label">TEAM MAVERICK</div>
                <div class="brand-name">{REP_NAME.upper()}</div>
              </div>
            </div>
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
