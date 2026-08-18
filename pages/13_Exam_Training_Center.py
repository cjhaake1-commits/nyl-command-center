from __future__ import annotations

import random
import streamlit as st

from core.exam_training import FL_215_LESSONS, QUESTIONS, SIE_DOMAINS, SIE_LESSONS, SOURCES

st.set_page_config(page_title="NYL Exam Training Center", page_icon="🎓", layout="wide")

if "mastered_cards" not in st.session_state:
    st.session_state.mastered_cards = set()
if "quiz_history" not in st.session_state:
    st.session_state.quiz_history = []

st.title("🎓 NYL Exam Training Center")
st.caption("Learn → recall → test → diagnose → repeat until exam-ready.")
st.info("The SIE is a FINRA exam, not a Florida state exam. Florida 2-15 insurance licensing is a separate track. This trainer keeps them separate so you learn the correct rule set for each exam.")
st.warning("Study aid only. Questions are original practice items, not actual or recalled exam questions. Always verify changing state rules against the current official Florida DFS/Pearson VUE materials.")

track = st.sidebar.radio("Training track", ["SIE", "Florida 2-15"])
mode = st.sidebar.radio("Mode", ["Dashboard", "Bullet Lessons", "Flashcards", "Practice Test", "Weak Areas", "Official Sources"])

lessons = SIE_LESSONS if track == "SIE" else FL_215_LESSONS
track_questions = [q for q in QUESTIONS if q["track"] == track]

if mode == "Dashboard":
    st.header(f"{track} Readiness Dashboard")
    mastered = len([x for x in st.session_state.mastered_cards if x.startswith(track + "|")])
    total_cards = sum(len(v) for v in lessons.values())
    attempts = [h for h in st.session_state.quiz_history if h["track"] == track]
    accuracy = (sum(h["correct"] for h in attempts) / len(attempts) * 100) if attempts else 0
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Cards mastered", f"{mastered}/{total_cards}")
    c2.metric("Questions answered", len(attempts))
    c3.metric("Practice accuracy", f"{accuracy:.0f}%")
    c4.metric("Target", "80%+ practice")
    st.progress(mastered / total_cards if total_cards else 0)
    if track == "SIE":
        st.subheader("Official SIE exam weighting")
        for domain, weight in SIE_DOMAINS.items():
            st.write(f"**{domain}: {weight:.0%}**")
            st.progress(weight)
        st.caption("Use the heavier Products & Risks and Trading/Accounts domains to allocate more study time.")
    else:
        st.subheader("Florida 2-15 study map")
        for domain in lessons:
            st.write(f"• **{domain}**")
        st.caption("Florida rules can change. Use this app for concepts and active recall, then verify state-specific numbers/rules against current official material.")

elif mode == "Bullet Lessons":
    st.header(f"{track} Bullet-Point Learning System")
    domain = st.selectbox("Domain", list(lessons))
    for i, bullet in enumerate(lessons[domain], 1):
        st.markdown(f"### {i}. {bullet}")
        st.caption("Say it back in your own words before moving on.")
    st.divider()
    st.markdown("**Retention rule:** Read once → explain aloud → answer from memory → test it in Practice Test mode.")

elif mode == "Flashcards":
    st.header(f"{track} Flashcards")
    domain = st.selectbox("Domain", list(lessons))
    cards = lessons[domain]
    idx = st.number_input("Card", 1, len(cards), 1) - 1
    card_id = f"{track}|{domain}|{idx}"
    st.markdown(f"## Prompt\nExplain this concept without looking:\n\n**{domain} — concept {idx + 1}**")
    with st.expander("Reveal answer"):
        st.success(cards[idx])
    col1, col2 = st.columns(2)
    if col1.button("✅ I know this", use_container_width=True):
        st.session_state.mastered_cards.add(card_id)
        st.rerun()
    if col2.button("🔁 Review again", use_container_width=True):
        st.session_state.mastered_cards.discard(card_id)
        st.rerun()
    st.caption("Mastered" if card_id in st.session_state.mastered_cards else "Not mastered yet")

elif mode == "Practice Test":
    st.header(f"{track} Practice Test")
    st.caption("Question bank is intentionally expandable. Add more original questions over time while preserving official topic weighting.")
    domain_filter = st.selectbox("Question set", ["All domains"] + list(lessons))
    pool = track_questions if domain_filter == "All domains" else [q for q in track_questions if q["domain"] == domain_filter]
    if not pool:
        st.warning("No questions are loaded for that domain yet.")
    else:
        if "current_question" not in st.session_state or st.session_state.get("current_track") != track or st.session_state.get("current_filter") != domain_filter:
            st.session_state.current_question = random.choice(pool)
            st.session_state.current_track = track
            st.session_state.current_filter = domain_filter
            st.session_state.answered = False
        q = st.session_state.current_question
        st.subheader(q["q"])
        choice = st.radio("Choose one", q["choices"], index=None)
        if st.button("Submit answer", type="primary", disabled=choice is None):
            selected = q["choices"].index(choice)
            correct = selected == q["answer"]
            st.session_state.quiz_history.append({"track": track, "domain": q["domain"], "correct": correct})
            st.session_state.answered = True
            st.session_state.last_correct = correct
        if st.session_state.get("answered"):
            if st.session_state.get("last_correct"):
                st.success("Correct.")
            else:
                st.error(f"Incorrect. Correct answer: {q['choices'][q['answer']]}")
            st.info(q["why"])
            if st.button("Next question"):
                st.session_state.current_question = random.choice(pool)
                st.session_state.answered = False
                st.rerun()

elif mode == "Weak Areas":
    st.header(f"{track} Weak-Area Coach")
    attempts = [h for h in st.session_state.quiz_history if h["track"] == track]
    if not attempts:
        st.info("Complete practice questions first. Your misses will automatically build a weak-area study list.")
    else:
        for domain in lessons:
            rows = [h for h in attempts if h["domain"] == domain]
            if not rows:
                continue
            accuracy = sum(r["correct"] for r in rows) / len(rows)
            st.write(f"**{domain}: {accuracy:.0%} ({len(rows)} attempts)**")
            st.progress(accuracy)
            if accuracy < .80:
                st.warning("Priority review area. Return to Bullet Lessons + Flashcards, then retest.")
        st.markdown("### Exam-readiness standard")
        st.write("Aim for repeated 80%+ practice performance across every domain—not one lucky passing score.")

elif mode == "Official Sources":
    st.header("Official / Primary Study Sources")
    st.write("Use these to verify exam structure, current outlines, licensing rules and any state-specific numbers that may change.")
    for name, url in SOURCES:
        st.markdown(f"- [{name}]({url})")
    st.divider()
    st.markdown("**Content policy for this trainer:** use public outlines and rules to create original teaching material and practice questions; never use stolen, recalled, or purported live exam questions.")
