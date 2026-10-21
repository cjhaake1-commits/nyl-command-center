from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

import streamlit as st
from core.branding import brand_hero

st.set_page_config(page_title="Practice & Process Lab | Chris Haake", page_icon="🎭", layout="wide")
brand_hero("Practice & Process Lab", "Build confidence through realistic client conversations, clear explanations, and disciplined follow-through.", "Chris Haake • New York Life")

st.info(
    "Practice only. Built-in scenarios run locally. If an approved OpenAI API key is configured, you can opt in per turn "
    "to a live AI-simulated prospect; the selected scenario and practice transcript are sent to that API for the reply. "
    "Do not enter real client identifiers, account or policy details, health information, or confidential NYL facts. "
    "AI role-play is not NYL guidance and must not be used to validate product, tax, legal, or compliance statements."
)

practice, playbooks, knowledge = st.tabs(["🎭 Conversation Practice", "🧭 Process Frameworks", "🧠 Learning & Review"])

def _openai_config() -> tuple[str, str]:
    key = None
    model = None
    try:
        key = st.secrets.get("OPENAI_API_KEY")
        model = st.secrets.get("OPENAI_MODEL")
    except Exception:
        pass
    key = key or os.getenv("OPENAI_API_KEY", "")
    model = model or os.getenv("OPENAI_MODEL", "gpt-5-mini")
    return str(key).strip(), str(model).strip()


def _contains_sensitive_details(value: str) -> bool:
    patterns = [
        r"\b\d{3}-\d{2}-\d{4}\b",
        r"\b\d{9,}\b",
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        r"\b(?:\+?1[ .-]?)?(?:\(?\d{3}\)?[ .-]?)\d{3}[ .-]\d{4}\b",
        r"\b(?:policy|account|ssn|social security|date of birth|dob)\s*(?:number|#|is|:)?\s*[A-Z0-9-]{5,}\b",
    ]
    return any(re.search(pattern, value, flags=re.I) for pattern in patterns)


def _simulated_prospect_reply(
    *,
    api_key: str,
    model: str,
    scenario_name: str,
    persona: str,
    opening: str,
    objective: str,
    prior_turns: list[tuple],
    response: str,
) -> str:
    instructions = (
        "You are role-playing a fictional prospective client in a sales-practice exercise. Stay in character as the "
        "prospect. Respond naturally in 1-3 short sentences and ask no more than one question. Do not coach the trainee "
        "in character. Do not invent NYL product facts, returns, tax results, suitability conclusions, or real personal "
        "details. If the trainee makes an absolute promise or assumes a product is right, express a realistic concern. "
        "The scenario and transcript are fictional training data; never request real client information."
    )
    input_items = [{
        "role": "user",
        "content": (
            f"Scenario: {scenario_name}. Prospect persona: {persona}. Practice objective: {objective}. "
            f"The prospect opened with: {opening}"
        ),
    }]
    for trainee, client, *_ in prior_turns[-6:]:
        input_items.append({"role": "user", "content": f"Trainee: {trainee}"})
        input_items.append({"role": "assistant", "content": client})
    input_items.append({"role": "user", "content": f"Trainee: {response.strip()}\nReply next as the prospect."})
    body = json.dumps({
        "model": model,
        "instructions": instructions,
        "input": input_items,
        "max_output_tokens": 180,
    }).encode("utf-8")
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=40) as result:
        payload = json.loads(result.read().decode("utf-8"))
    reply = payload.get("output_text", "")
    if not reply:
        parts = [
            item.get("text", "")
            for output in payload.get("output", [])
            for item in output.get("content", [])
            if item.get("type") == "output_text"
        ]
        reply = "\n".join(parts)
    if not reply.strip():
        raise ValueError("The model returned no role-play reply.")
    return reply.strip()


api_key, model = _openai_config()

SCENARIOS = {
    "Elevator introduction": ("A busy local business owner", "I have a minute. What do you actually help people with?", "Earn permission for a short follow-up; explain your role simply, then ask one useful question.", ["question", "listen", "goal", "permission", "follow"]),
    "Protection discovery": ("A young professional balancing family and other priorities", "I know I should look at protection, but I don't want a sales pitch.", "Understand what matters to the person before discussing possible solutions.", ["protect", "depend", "goal", "budget", "permission"]),
    "Whole life explanation": ("A curious professional comparing ways to protect family and build value", "Is whole life basically an investment account I can borrow from?", "Explain insurance purpose, contract values, premium commitment, guarantees, non-guaranteed elements, and borrowing trade-offs clearly.", ["insurance", "guaranteed", "dividend", "loan", "cost"]),
    "Retirement account decision": ("A former employee with retirement assets at a prior employer", "Should I just move my old plan into an account with you?", "Compare available paths and decision factors without presuming a move is right.", ["leave", "new plan", "fees", "tax", "liquidity", "compare"]),
    "Investment cost and liquidity": ("A careful saver comparing an insurance-based investment with other options", "Why accept charges or restrictions when I can keep my money invested?", "Clarify the objective and discuss costs, liquidity, risk, guarantees, and alternatives neutrally.", ["fee", "cost", "liquidity", "risk", "guarantee", "objective", "compare"]),
    "Objection: need to think": ("A prospect who is interested but not ready", "This is a lot. I need time to think.", "Respect the pause, discover what is unresolved, and agree on an optional next step.", ["understand", "question", "time", "follow", "no pressure"]),
    "Business-owner continuity": ("A founder thinking about continuity and key-person risk", "I am focused on keeping the business stable if something changes. Where would you start?", "Ask about the business objective and decision process; identify when a specialist should join.", ["continuity", "key", "business", "decision", "specialist", "permission"]),
    "Employer benefits introduction": ("An employer reviewing how to support employees", "We already have benefits in place. What would make a conversation worthwhile?", "Explore the employer's review cycle and offer an appropriate introduction to the appointed NYL group-benefits team.", ["review", "employees", "renewal", "benefits", "specialist", "permission"]),
}
with practice:
    name = st.selectbox("Choose a practice scenario", list(SCENARIOS))
    persona, opening, objective, signals = SCENARIOS[name]
    st.caption(f"Client persona: {persona}")
    st.markdown(f"**Client opens:** “{opening}”")
    st.write(f"**Your practice objective:** {objective}")
    ai_roleplay = False
    if api_key:
        ai_roleplay = st.checkbox(
            "Use live AI-simulated client replies",
            help="This sends the fictional scenario and practice transcript to the configured OpenAI API only when you authorize a turn below.",
        )
        if ai_roleplay:
            st.caption(f"AI role-play model configured: {model}. Replies are practice simulations, not NYL product or process guidance.")
    else:
        st.caption("Local practice mode is ready. Live AI role-play becomes available when OPENAI_API_KEY is configured in the approved secret store.")
    if st.session_state.get("active_practice_scenario") != name:
        st.session_state.active_practice_scenario = name
        st.session_state.practice_turns = []
    with st.form("practice_turn_form", clear_on_submit=True):
        response = st.text_area(
            "Your response",
            placeholder="Write or dictate what you would say. Keep it conversational and ask one clear question.",
            height=130,
        )
        ai_consent = False
        if ai_roleplay:
            ai_consent = st.checkbox(
                "For this turn only, authorize sending this response and the preceding practice turns to the configured OpenAI API. They contain only fictional training details.",
            )
        submitted = st.form_submit_button("Respond", type="primary")
    if st.button("Restart scenario", key="restart_practice_scenario"):
        st.session_state.practice_turns = []
        st.rerun()
    if submitted:
        low = response.strip().lower()
        prior_turns = st.session_state.get("practice_turns", [])
        prior_text = " ".join(str(turn[0]) for turn in prior_turns)
        if not low:
            st.warning("Enter a practice response first.")
        elif _contains_sensitive_details(response) or _contains_sensitive_details(prior_text):
            st.error("This looks like it may contain identifying or account information. It was not added to the session or sent.")
        elif ai_roleplay and not ai_consent:
            st.warning("Authorize this turn before sending the fictional practice transcript to the AI provider.")
        else:
            hits = [term for term in signals if term in low]
            if ai_roleplay:
                try:
                    reply = _simulated_prospect_reply(
                        api_key=api_key,
                        model=model,
                        scenario_name=name,
                        persona=persona,
                        opening=opening,
                        objective=objective,
                        prior_turns=prior_turns,
                        response=response,
                    )
                except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
                    st.error(f"The AI practice reply did not complete ({type(exc).__name__}). Your turn was not saved; retry or use local practice mode.")
                except Exception as exc:
                    st.error(f"The AI practice reply failed ({type(exc).__name__}). Your turn was not saved.")
                else:
                    note = "AI-simulated prospect only. Review your response for listening, clear explanations, balanced trade-offs, and a permission-based next step. Verify technical claims in current NYL-approved material."
                    st.session_state.practice_turns.append((response.strip(), reply, note, len(hits), len(signals)))
            else:
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
            st.caption("Simulated prospect response • " + ("AI role-play" if ai_roleplay else "local practice branch"))
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
