from __future__ import annotations

import streamlit as st

from core.branding import brand_hero

st.set_page_config(page_title="Series 7 Study Guide | Chris Haake", page_icon="📚", layout="wide")
brand_hero(
    "Series 7 Study Guide",
    "An exploratory, self-paced map of the General Securities Representative exam—built around FINRA’s public outline.",
    "STUDY DESK • Familiarization, not exam authorization",
)

st.info(
    "You are exploring this exam for future preparation. This page is an independent learning aid, not professional "
    "exam-prep material or NYL training. Verify all details against current FINRA and firm materials before scheduling. "
    "Reading this guide or passing an exam does not by itself expand your current registration, firm approval, or permitted activities."
)

st.markdown(
    "**Exam snapshot:** FINRA lists 125 scored items, 3 hours 45 minutes, and a 72% passing score. The exam also includes "
    "10 unscored pretest items. The SIE is a co-requisite; representative-level exams require firm sponsorship. "
    "[FINRA Series 7 overview](https://www.finra.org/registration-exams-ce/qualification-exams/series7) · "
    "[Official content outline](https://www.finra.org/sites/default/files/Series_7_Content_Outline.pdf)"
)

tab_guide, tab_videos, tab_review = st.tabs(["📘 Study map", "▶️ Long-form video", "🧠 Recall & self-check"])

with tab_guide:
    st.subheader("Study in proportion to the exam")
    st.markdown(
        "FINRA assigns 91 of 125 items (73%) to Function 3. Spend the greatest share of your eventual study time "
        "on product characteristics, recommendations and suitability, transfers, and records. Learn the smaller "
        "functions too, but do not give them equal study time."
    )
    st.dataframe(
        [
            {"Function": "1 • Seeks business", "Items": 9, "Share": "7%", "Study focus": "Permitted communications, solicitation, public offerings, and ethical conduct."},
            {"Function": "2 • Opens accounts", "Items": 11, "Share": "9%", "Study focus": "Customer profile, objectives, account types, documentation, and account rules."},
            {"Function": "3 • Recommendations & servicing", "Items": 91, "Share": "73%", "Study focus": "Securities products, risks, features, suitability, transfers, records, and customer information."},
            {"Function": "4 • Transactions", "Items": 14, "Share": "11%", "Study focus": "Orders, execution, settlement, confirmations, and handling customer instructions."},
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Concept guide")
    with st.expander("1. Customer profile and suitability foundations", expanded=True):
        st.markdown(
            "- Build a complete profile: objectives, time horizon, liquidity needs, financial situation, experience, and risk tolerance.\n"
            "- Match the recommendation to the customer's profile and applicable firm standards; distinguish a customer's stated preference from a well-supported recommendation.\n"
            "- Understand account ownership and authority: individual, joint, custodial, trust, retirement, business, and discretionary/non-discretionary relationships.\n"
            "- Know when information is missing or inconsistent; clarify before acting. Documentation and supervision matter."
        )
    with st.expander("2. Equity securities"):
        st.markdown(
            "- Common stock: ownership and voting rights; dividends are not guaranteed. Preferred stock typically has priority over common dividends and liquidation, but remains subject to issuer and market risk.\n"
            "- Understand primary versus secondary markets, public offerings, rights, warrants, ADRs, and basic corporate actions.\n"
            "- Read a quote and distinguish market, limit, stop, and stop-limit orders; an order's execution price and timing are not guaranteed."
        )
    with st.expander("3. Debt, municipal, and government securities"):
        st.markdown(
            "- Bond price and market yields generally move in opposite directions. Credit risk, duration/interest-rate risk, call risk, reinvestment risk, and liquidity risk are distinct.\n"
            "- Recognize coupon, maturity, par, current yield, yield to maturity, and tax-equivalent yield concepts. Know that tax treatment depends on facts and jurisdiction.\n"
            "- Distinguish corporate, U.S. Treasury, agency, and municipal obligations; issuer structure and guarantees differ."
        )
    with st.expander("4. Investment companies and pooled products"):
        st.markdown(
            "- Compare open-end mutual funds, closed-end funds, ETFs, UITs, money-market funds, REITs, and variable products by structure, pricing, liquidity, costs, risks, and tax treatment.\n"
            "- For mutual funds, learn NAV, offering price, sales charges, breakpoints, rights of accumulation, and letters of intent. For ETFs/closed-end funds, market price may differ from underlying NAV.\n"
            "- Product labels do not determine suitability; expenses, liquidity, holdings, objective, and customer circumstances matter."
        )
    with st.expander("5. Options and packaged strategies"):
        st.markdown(
            "- A call gives its buyer the right to buy; a put gives its buyer the right to sell. The option writer has an obligation if assigned.\n"
            "- Practice payoff diagrams and breakeven calculations for long calls/puts, covered calls, protective puts, spreads, and straddles. Know maximum gain/loss and the risks of uncovered writing.\n"
            "- Use intrinsic value + time value = premium, and understand exercise, assignment, expiration, and American/European style distinctions."
        )
    with st.expander("6. Customer accounts, retirement, margin, and tax concepts"):
        st.markdown(
            "- Learn cash versus margin accounts, Regulation T concepts, maintenance requirements, margin calls, and the risks of leverage.\n"
            "- Identify basic IRA, employer plan, education, trust, and custodial account features without assuming that an asset transfer or rollover is appropriate.\n"
            "- Separate tax concepts commonly tested from personalized tax advice; refer case-specific tax questions to a qualified professional."
        )
    with st.expander("7. Rules, communications, records, and transaction lifecycle"):
        st.markdown(
            "- Learn the roles of FINRA, SEC, MSRB, exchanges, clearing agencies, and state regulators at a high level.\n"
            "- Know the broad lifecycle: order entry, handling/routing, execution, confirmation, settlement, and recordkeeping.\n"
            "- Review communications standards, prohibited practices, AML concepts, privacy, complaint escalation, and supervision using current official sources."
        )

    st.subheader("Suggested leisurely path")
    st.markdown(
        "Use a light recurring rhythm rather than a cram schedule: one 30–45 minute block each week, then increase "
        "only when an exam date is real. A practical cycle is: (1) read one official-outline section, (2) close the notes "
        "and explain it from memory, (3) solve a few original practice problems, (4) record the error and why the right answer "
        "wins, (5) revisit the concept after several days and again the next week. Prioritize retrieval with feedback and spaced review; "
        "video is a supplement, not a substitute for question practice or current exam materials."
    )
    st.caption("FINRA's public outline is the authority for content coverage and weights. This guide paraphrases topic areas; it does not reproduce protected exam questions.")

with tab_videos:
    st.subheader("Long-form YouTube study picks")
    st.caption(
        "You asked for long-format videos. YouTube does not expose comparable star ratings for these exam videos, and likes "
        "are not consistently visible through public search. Picks below are ranked by useful observable signals—course structure, "
        "coverage, instructor/channel footprint, and visible engagement where available—not a claimed pass-rate ranking."
    )
    st.markdown(
        "1. **[Series 7 Exam Cram Course — Series 7 Guru](https://www.youtube.com/playlist?list=PLK1IazV_JQbEr44OXWnmE8NSviwommHj-)** — A 15-lesson course playlist of long class replays, described by the publisher as equivalent to its four-day cram course. Strongest structured long-form option located.\n"
        "2. **[Series 7 exam lecture playlist — Brian Lee / TestGeek](https://www.youtube.com/playlist?list=PLK1IazV_JQbHRNYBPbgzqLo8dheSRomsd)** — A 32-lecture playlist; search results show examples around 1–2 hours and substantial view counts on selected classes. Useful for deeper topic-by-topic explanations.\n"
        "3. **[Complete FINRA regulatory crash course — Exam Pass Pro](https://www.youtube.com/watch?v=ofZqAxl73bo)** — One continuous ~2-hour overview with a timestamped topic map. Newer and broad, but its channel footprint and view count are much smaller; use as a supplement."
    )
    st.caption("Check each playlist's current video lengths and publication dates before relying on it; content may be updated or removed. For the clearest official outline-to-lesson match, use FINRA's linked PDF first.")
    st.markdown("**Recommended use:** watch in short segments, pause before worked answers, solve the example independently, then explain the rule without looking. Take notes on ambiguities to check against current FINRA material.")

with tab_review:
    st.subheader("Retrieval-practice cards")
    questions = [
        ("How many scored items are assigned to Function 3, and why does that matter for study allocation?", "91 of 125 (73%); allocate the largest share of eventual preparation time to products, recommendations, transfers, and records."),
        ("What happens to bond prices when market yields rise, all else equal?", "Prices generally fall. Then distinguish interest-rate/duration risk from credit, call, liquidity, and reinvestment risks."),
        ("Who has the right and who has the obligation in a standard listed option?", "The buyer has a right; the writer has an obligation if assigned."),
        ("Does a rollover question establish that a rollover is suitable?", "No. Compare eligible paths and relevant features using current facts and approved firm process; do not presume a destination."),
        ("What is the difference between a mutual fund's NAV and its public offering price?", "NAV is per-share net asset value; a sales charge, when applicable, can make offering price higher. Learn each fund's pricing structure."),
        ("Does passing Series 7 alone authorize a person to conduct securities business?", "No. The SIE co-requisite, active registration/association, state and firm approvals, and supervision requirements also apply."),
    ]
    for i, (q, a) in enumerate(questions, start=1):
        with st.expander(f"Card {i} • {q}"):
            st.write(a)

    st.subheader("Mini self-check")
    q = st.selectbox("Choose a prompt", [x[0] for x in questions], key="series7_self_check")
    response = st.text_area("Answer from memory before opening the card above", key="series7_response", height=110)
    if st.button("Show a review cue", key="series7_review"):
        match = next(a for prompt, a in questions if prompt == q)
        st.info("Compare your answer with this review cue: " + match)

    st.markdown("**When formal prep begins:** obtain the current FINRA outline and firm-approved materials, verify sponsorship/eligibility with your supervisor, use a reputable question bank aligned to the current outline, and schedule timed practice only after core concepts are stable.")
