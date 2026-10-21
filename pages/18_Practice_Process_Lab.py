from __future__ import annotations

import streamlit as st
from core.branding import brand_hero

st.set_page_config(page_title="Practice & Process Lab | Chris Haake", page_icon="🎭", layout="wide")
brand_hero("Practice & Process Lab", "Build confidence through realistic client conversations, clear explanations, and disciplined follow-through.", "Chris Haake • New York Life")

st.info("Practice tool only. Client replies are generated from built-in scenario branches, not a live AI or NYL system. Verify current product, licensing, compliance, and process guidance through approved NYL resources. Do not enter real client identifiers, account details, health information, or confidential financial facts.")

practice, playbooks, knowledge = st.tabs(["🎭 Conversation Practice", "🧭 Process Frameworks", "🧠 Learning & Review"])

SCENARIOS = {
    "Elevator introduction": ("A busy local business owner", "I have a minute. What do you actually help people with?", "Earn permission for a short follow-up; explain your role simply, then ask one useful question.", ["question", "listen", "goal", "permission", "follow"]),
    "Protection discovery": ("A young professional balancing family and other priorities", "I know I should look at protection, but I don't want a sales pitch.", "Understand what matters to the person before discussing possible solutions.", ["protect", "depend", "goal", "budget", "permission"]),
    "Whole life explanation": ("A curious professional comparing ways to protect family and build value", "Is whole life basically an investment account I can borrow from?", "Explain insurance purpose, contract values, premium commitment, guarantees, non-guaranteed elements, and borrowing trade-offs clearly.", ["insurance", "guaranteed", "dividend", "loan", "cost"]),
    "Retirement account decision": ("A former employee with retirement assets at a prior employer", "Should I just move my old plan into an account with you?", "Compare available paths and decision factors without presuming a move is right.", ["leave", "new plan", "fees", "tax", "liquidity", "compare"]),
    "Investment cost and liquidity": ("A careful saver comparing an insurance-based investment with other options", "Why accept charges or restrictions when I can keep my money invested?", "Clarify the objective and discuss costs, liquidity, risk, guarantees, and alternatives neutrally.", ["fee", "cost", "liquidity", "risk", "guarantee", "objective", "compare"]),
    "Objection: need to think": ("A prospect who is interested but not ready", "This is a lot. I need time to think.", "Respect the pause, discover what is unresolved, and agree on an optional next step.", ["understand", "question", "time", "follow", "no pressure"]),
}
with practice:
    name = st.selectbox("Choose a practice scenario", list(SCENARIOS))
    persona, opening, objective, signals = SCENARIOS[name]
    st.caption(f"Client persona: {persona}")
    st.markdown(f"**Client opens:** “{opening}”")
    st.write(f"**Your practice objective:** {objective}")
    if st.session_state.get("active_practice_scenario") != name:
        st.session_state.active_practice_scenario = name
        st.session_state.practice_turns = []
    response = st.text_area("Your response", placeholder="Write or dictate what you would say. Keep it conversational and ask one clear question.", height=130, key="practice_response")
    send_col, reset_col = st.columns([1, 5])
    submitted = send_col.button("Respond", type="primary")
    if reset_col.button("Restart scenario"):
        st.session_state.practice_turns = []
        st.rerun()
    if submitted:
        low = response.strip().lower()
        if not low:
            st.warning("Enter a practice response first.")
        else:
            hits = [term for term in signals if term in low]
            if any(term in low for term in ["guaranteed return", "always", "best", "no risk", "tax free"]):
                reply = "I want to be careful with promises. What is guaranteed, what can change, and where could I see that in writing?"
                note = "Avoid absolute claims. Separate contractual guarantees from elements that may change, and use approved materials."
            elif any(term in low for term in ["fee", "cost", "charge", "surrender"]):
                reply = "What other choices should I compare, and what trade-offs would each involve?"
                note = "Acknowledge costs directly, describe meaningful trade-offs, and compare suitable alternatives fairly."
            elif any(term in low for term in ["think", "time", "pressure", "follow"]):
                reply = "Could you send me a short summary of what we discussed? I can decide later whether I want to continue."
                note = "Respect the person's timing. Ask permission for a specific, low-pressure follow-up."
            elif any(term in low for term in ["question", "what matters", "goal", "tell me", "objective", "protect", "compare"]):
                reply = "What would you want to understand first, and how would you help me compare options without assuming I need one particular solution?"
                note = "Stay in discovery: priorities, constraints, decision process, and understanding come before a recommendation."
            elif any(term in low for term in ["rollover", "annuity", "policy", "whole life", "buy", "product"]):
                reply = "Before discussing a solution, what would you need to understand about my situation?"
                note = "Lead with the person's decision criteria and situation. Avoid moving into a product explanation too early."
            else:
                reply = "Can you make that more specific to me? What would you ask next before suggesting anything?"
                note = "Try one open question, reflect what you hear, and ask permission before explaining a solution."
            st.session_state.practice_turns.append((response.strip(), reply, note, len(hits), len(signals)))
    for you, client, _, _, _ in st.session_state.get("practice_turns", []):
        with st.chat_message("user"):
            st.markdown(you)
        with st.chat_message("assistant"):
            st.markdown(client)
            st.caption("Simulated client response • built-in scenario branch")
    if st.session_state.get("practice_turns"):
        _, _, note, score, total = st.session_state.practice_turns[-1]
        st.subheader("Coaching check")
        st.write(note)
        st.progress(min(score / max(3, total), 1.0), text="Relevant conversation signals in your response")
        st.caption("Review: Did you listen, ask a useful question, explain accurately, address trade-offs, and agree on a permission-based next step?")
    with st.expander("Elevator talk, explanation, and closing drills"):
        st.markdown("- **30-second introduction:** who you help, what you help clarify, and one permission-based question.\n- **Clear explanation:** purpose, how it works, costs, liquidity, risks, guarantees, and what may change.\n- **Close:** summarize the person's stated priorities and ask if they want to review a next step. Never manufacture urgency.\n- **Objection drill:** acknowledge the concern, clarify what sits behind it, answer only what you know, then check understanding.")

with playbooks:
    st.subheader("Repeatable conversation and case frameworks")
    st.caption("General learning frameworks based on your prior work and practice needs. They are not official process instructions or substitutes for current NYL procedures.")
    with st.expander("Before recommending or explaining anything", expanded=True):
        st.markdown("1. Establish purpose and permission.\n2. Ask about goals, people or obligations involved, timing, constraints, and what a good outcome means.\n3. Reflect back what you heard and invite correction.\n4. Identify what information is still missing.\n5. Compare reasonable paths, including keeping the current arrangement where relevant.\n6. Explain costs, liquidity, risks, tax considerations, guarantees and limits in plain language.\n7. Confirm understanding, document rationale through approved systems, and agree on a next step.")
    with st.expander("Retirement account decisions"):
        st.markdown("Help the person compare the former employer plan, a new employer plan when available, an IRA or other eligible destination, and taking a distribution. Explore fees, investment choices, services, liquidity, tax consequences, time horizon, protections, and plan-specific features. Verify facts using current statements and approved tools. Do not assume a rollover is suitable or promise a tax result.")
    with st.expander("Protection conversations"):
        st.markdown("Start with the need to protect, affordability, time horizon, and the person's priorities. Distinguish insurance protection from accumulation or investment features. Explain contract guarantees separately from non-guaranteed elements; discuss borrowing and access limitations accurately. Confirm details using current approved materials.")
    with st.expander("Investment and annuity explanations"):
        st.markdown("Clarify the goal and compare other paths before discussing an investment-based contract. Cover market risk, fees, liquidity and surrender terms, investment choices, tax treatment, and any guarantees with their conditions. Use current approved product documents and required supervision.")
    with st.expander("Business owner, employer, and referral conversations"):
        st.markdown("Open with the business or community issue the person cares about. Ask how decisions are made and who else should be involved. For benefits or specialized business needs, coordinate with the appropriate NYL team and confirm role, eligibility, handoff, and crediting internally.")

with knowledge:
    st.subheader("Turn learning into fluency")
    st.markdown("Use this loop with your approved study materials, course notes, and manager coaching:")
    st.markdown("1. **Retrieve:** explain the concept from memory in plain language.\n2. **Apply:** answer a realistic client question without reading a script.\n3. **Stress-test:** name a cost, risk, limitation, or alternative.\n4. **Verify:** find the current approved source for every technical statement.\n5. **Reflect:** record one strong phrase and one improvement in your private notes.")
    product = st.selectbox("Choose a quick knowledge drill", ["Protection and whole life", "Retirement account options", "Annuity costs and liquidity", "Securities scope and authorization", "Group and workplace benefits"])
    prompts = {
        "Protection and whole life": "Explain the difference between the protection need and the policy's cash value. Which elements are contractually guaranteed, and what can change?",
        "Retirement account options": "What paths should be compared before a rollover, and what client facts would change the analysis?",
        "Annuity costs and liquidity": "Name the major cost and access questions a client should understand before comparing an annuity with other investments.",
        "Securities scope and authorization": "What is your active registration and firm authorization for this activity? What current approved document governs the product?",
        "Group and workplace benefits": "Which NYL team should be involved, and what must be confirmed before representing that you can quote or place group coverage?",
    }
    st.info(prompts[product])
    answer = st.text_area("Your practice answer", placeholder="Answer from memory, then verify it in current approved material.", height=110)
    if st.button("Review my answer"):
        if not answer.strip():
            st.warning("Write an answer before reviewing.")
        else:
            st.write("Check your answer for: accurate purpose, plain language, meaningful costs and limits, reasonable alternatives, a current approved source, and a clear statement of what you still need to verify.")
            st.caption("This is a self-review rubric, not product, legal, tax, or compliance advice.")
    st.caption("No uploaded training documents or internal procedures are reproduced or linked here. Keep client-specific scenarios and confidential facts out of this publicly accessible app.")
