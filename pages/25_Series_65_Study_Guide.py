from __future__ import annotations

import streamlit as st

from core.branding import brand_hero

st.set_page_config(page_title="Series 65 Study Guide | Chris Haake", page_icon="📖", layout="wide")
brand_hero(
    "Series 65 Study Guide",
    "A self-paced introduction to investment adviser concepts, securities law, portfolio analysis, and ethical practice.",
    "STUDY DESK • Familiarization, not exam authorization",
)

st.info(
    "This is an independent early-learning guide, not professional exam-prep material or NYL training. NASAA and the "
    "applicable state regulator control the official outline and licensing requirements. An exam pass alone does not "
    "authorize investment-adviser activity; registration and firm approval must also be complete."
)

st.markdown(
    "**Exam snapshot:** NASAA lists 130 scored questions plus 10 pretest questions, 180 minutes, and 92 correct "
    "answers required to pass. The Series 65 is the Uniform Investment Adviser Law Examination. "
    "[NASAA exam overview](https://www.nasaa.org/exams/general-exam-information/series-65-exam-content-outline/) · "
    "[Current test specifications](https://www.nasaa.org/exams/general-exam-information/series-65-exam-content-outline/series-65-outline/) · "
    "[NASAA Series 65 study guide](https://www.nasaa.org/wp-content/uploads/2023/09/NASAA-Series-65-Exam-Study-Guide.pdf)"
)

tab_guide, tab_videos, tab_review = st.tabs(["📘 Study map", "▶️ Long-form video", "🧠 Recall & self-check"])

with tab_guide:
    st.subheader("Official content weighting")
    st.caption("NASAA's public outline groups the exam into four areas. Weighting determines the relative number of questions.")
    st.dataframe(
        [
            {"Area": "1 • Economic factors and business information", "Share": "15%", "Study focus": "Economic indicators, business cycles, financial statements, and analytical methods."},
            {"Area": "2 • Investment vehicle characteristics", "Share": "25%", "Study focus": "Securities, pooled investments, fixed income, derivatives, insurance products, and risks."},
            {"Area": "3 • Client investment recommendations and strategies", "Share": "30%", "Study focus": "Client profile, portfolio construction, tax, retirement, education, and special situations."},
            {"Area": "4 • Laws, regulations, and unethical business practices", "Share": "30%", "Study focus": "State/federal law, registration, fiduciary duties, disclosures, custody, prohibited practices, and ethics."},
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Concept guide")
    with st.expander("1. Economics and business information", expanded=True):
        st.markdown(
            "- Understand real versus nominal values, inflation, interest rates, monetary/fiscal policy, business cycles, and leading/coincident/lagging indicators.\n"
            "- Learn the broad meaning of yield-curve shapes and how rates, inflation, and growth can affect security prices; avoid turning relationships into certain forecasts.\n"
            "- Read income statements, balance sheets, and cash-flow statements at an introductory level; distinguish liquidity, leverage, profitability, and operating cash flow.\n"
            "- Review time value of money, present/future value, return measures, and risk/return concepts."
        )
    with st.expander("2. Investment vehicles and risk"):
        st.markdown(
            "- Compare equity, debt, government and municipal securities, mutual funds, ETFs, closed-end funds, UITs, REITs, private/alternative investments, options, and insurance products.\n"
            "- For each, identify ownership/claim, income source, liquidity, pricing, costs, tax considerations, market/credit/inflation/interest-rate risk, and guarantees or their absence.\n"
            "- Understand diversification, correlation, systematic versus unsystematic risk, standard deviation, beta, duration, and the limits of historical performance.\n"
            "- Learn suitability-relevant features without treating any product's tax treatment or guarantee as a substitute for the full client picture."
        )
    with st.expander("3. Client profiles, portfolio construction, and planning"):
        st.markdown(
            "- Collect goals, time horizon, liquidity needs, income/resources, obligations, experience, risk capacity and tolerance, tax context, and decision constraints.\n"
            "- Know asset-allocation, rebalancing, dollar-cost averaging, active/passive management, and basic portfolio theory. No strategy assures a gain or prevents loss.\n"
            "- Compare account types and planning contexts such as retirement, education, trusts, estates, business entities, and insurance needs.\n"
            "- Evaluate recommendations in context, including fees, tax effects, liquidity, concentration, alternatives, and conflicts; ask what is missing before concluding."
        )
    with st.expander("4. State and federal securities law"):
        st.markdown(
            "- Build a role map: investment adviser (IA) versus investment adviser representative (IAR); broker-dealer (BD) versus agent. Understand the distinction between firm and individual registration.\n"
            "- Study federal/state jurisdiction, registration and exemption concepts, notice filing, de minimis rules, custody, books and records, advertising, and advisory contracts.\n"
            "- Focus on definitions and fact patterns: who is acting, for what compensation, in which jurisdiction, for which client, and under which exemption or registration.\n"
            "- Use NASAA's current study guide and the current statutes/rules reflected in your official materials. Legal details can change."
        )
    with st.expander("5. Fiduciary duty, ethics, and conflicts"):
        st.markdown(
            "- Understand the fiduciary relationship and the duty to act in the client's best interest, disclose material conflicts, and avoid misleading claims.\n"
            "- Learn prohibited and unethical practices, principal/cross transactions, borrowing/lending, custody, discretion, performance advertising, testimonials, referrals, and recordkeeping as described in the current outline.\n"
            "- Ask: What conflict exists? Was it fully and clearly disclosed? Can it be eliminated or mitigated? Is the recommendation still in the client's best interest? What must be documented or escalated?\n"
            "- Never use exam notes as authority for a real client situation; verify current policy and involve compliance/supervision."
        )
    st.subheader("Suggested leisurely path")
    st.markdown(
        "Start with one weekly 30–45 minute session. Study concepts in the official weighting order, but keep law/ethics "
        "in regular rotation because it is both a large exam area and foundational to professional conduct. Close the material "
        "and retrieve definitions from memory; work small scenario questions; explain why the tempting alternatives are wrong; "
        "keep an error log; then revisit after a few days and again the following week. When the exam is actually scheduled, "
        "shift to full outline coverage, current prep materials, and timed practice with detailed feedback."
    )
    st.caption("This guide summarizes publicly available topic categories in original wording. Use NASAA's current outline and official study guide for exact scope and definitions.")

with tab_videos:
    st.subheader("Long-form YouTube study picks")
    st.caption(
        "YouTube does not provide comparable star ratings for these exam videos, and public like counts are inconsistent. "
        "The selections are based on course structure, publicly visible curriculum/detail, channel history, and engagement signals "
        "where discoverable. No video has a verified pass-rate advantage."
    )
    st.markdown(
        "1. **[Series 65 free exam-prep playlist — Series 7 Guru / Dean Tinney](https://www.youtube.com/playlist?list=PLK1IazV_JQbGn7K_gBAD_TWW_TLrlRxA5)** — Long-form topic lectures and a large established exam-prep channel; search results surfaced individual lectures with tens of thousands of views. Select the full-length lectures rather than short quizzes.\n"
        "2. **[Series 65 complete study playlist — Focused Exam Strategy](https://www.youtube.com/playlist?list=PLT9ng_7TzM_jw9hgiUXXa-2b7-5OwLKs8)** — Recently assembled 43-video course with broad outline coverage; useful for a structured lecture path.\n"
        "3. **[Complete Series 65 investment adviser study playlist — Open Exam Prep](https://www.youtube.com/playlist?list=PLi1e52n1YnBSbRaGXzF_AnM05jzDSMDAN)** — A 75-episode structured lesson/podcast sequence. Episodes are shorter than the first option, but the complete playlist is a long-format course path."
    )
    st.caption("A single continuous, high-engagement full-length Series 65 lecture could not be confirmed with reliable public length/ratings signals. These playlist courses are the better-supported long-form options found. Verify each current playlist against NASAA's latest outline.")
    st.markdown("**Recommended use:** take notes in your own words, stop before a worked answer, attempt the problem yourself, and check legal topics against the NASAA study guide. Use video as instruction, not as your only assessment.")

with tab_review:
    st.subheader("Retrieval-practice cards")
    questions = [
        ("How many questions count toward the Series 65 score, and what is the current passing threshold?", "130 scored questions; at least 92 correct. The exam also includes 10 pretest items."),
        ("Why does a rising market interest rate often pressure existing bond prices?", "New bonds may offer higher yields, reducing the relative value of existing fixed cash flows. The price response depends on duration and other features."),
        ("What is systematic risk?", "Market-wide risk that diversification cannot eliminate; company-specific risk can often be reduced through diversification."),
        ("What are the four broad statement types used to assess a business?", "Income statement, balance sheet, cash-flow statement, and statement of shareholders' equity; learn their roles and relationships."),
        ("Why is disclosure alone not a complete ethical analysis?", "A disclosed conflict still must be managed consistently with fiduciary obligations and applicable law; disclosure does not automatically make a recommendation appropriate."),
        ("Does passing Series 65 itself authorize fee-based advisory work?", "No. Required state/firm registration, association, approvals, and applicable rules must also be satisfied."),
    ]
    for i, (q, a) in enumerate(questions, start=1):
        with st.expander(f"Card {i} • {q}"):
            st.write(a)

    st.subheader("Mini self-check")
    q = st.selectbox("Choose a prompt", [x[0] for x in questions], key="series65_self_check")
    response = st.text_area("Answer from memory before opening the card above", key="series65_response", height=110)
    if st.button("Show a review cue", key="series65_review"):
        match = next(a for prompt, a in questions if prompt == q)
        st.info("Compare your answer with this review cue: " + match)

    st.markdown("**When formal prep begins:** confirm the exam's current specifications, state requirements, firm pathway, approved study materials, and registration status with your manager or compliance contact.")
