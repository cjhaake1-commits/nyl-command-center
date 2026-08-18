from __future__ import annotations

import random
from collections import defaultdict
from datetime import date, datetime, timedelta

import streamlit as st

from core.exam_training import (
    FLASHCARDS,
    FL_215_LESSONS,
    QUESTIONS,
    SIE_DOMAINS,
    SIE_LESSONS,
    SOURCES,
    THREE_DAY_PLANS,
)

st.set_page_config(page_title="NYL Exam Training Center", page_icon="🎓", layout="wide")

# Session-persistent study state. This intentionally avoids storing regulated client information.
DEFAULTS = {
    "quiz_history": [],
    "card_ratings": {},
    "missed_ids": [],
    "simulation": None,
    "simulation_answers": {},
    "simulation_started": None,
    "simulation_submitted": False,
    "exam_date": date.today() + timedelta(days=3),
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


def track_lessons(track):
    return SIE_LESSONS if track == "SIE" else FL_215_LESSONS


def track_questions(track):
    return [x for x in QUESTIONS if x["track"] == track]


def question_id(question):
    return f"{question['track']}|{question['domain']}|{question['q']}"


def weighted_sie_sample(n=75):
    pool = track_questions("SIE")
    selected = []
    for domain, meta in SIE_DOMAINS.items():
        domain_pool = [x for x in pool if x["domain"] == domain]
        count = meta["scored_items"]
        if len(domain_pool) >= count:
            selected.extend(random.sample(domain_pool, count))
        else:
            selected.extend(random.choices(domain_pool, k=count))
    random.shuffle(selected)
    return selected[:n]


def mixed_sample(track, n):
    pool = track_questions(track)
    if n <= len(pool):
        return random.sample(pool, n)
    return random.choices(pool, k=n)


def record_answer(question, correct, source):
    qid = question_id(question)
    st.session_state.quiz_history.append({
        "track": question["track"],
        "domain": question["domain"],
        "correct": bool(correct),
        "source": source,
        "qid": qid,
        "at": datetime.now().isoformat(timespec="seconds"),
    })
    if not correct:
        st.session_state.missed_ids.append(qid)


def mastery_stats(track):
    attempts = [x for x in st.session_state.quiz_history if x["track"] == track]
    cards = [x for x in FLASHCARDS if x["track"] == track]
    mastered_cards = sum(st.session_state.card_ratings.get(x["id"], 0) >= 4 for x in cards)
    accuracy = sum(x["correct"] for x in attempts) / len(attempts) if attempts else 0
    by_domain = {}
    for domain in track_lessons(track):
        rows = [x for x in attempts if x["domain"] == domain]
        by_domain[domain] = (sum(x["correct"] for x in rows) / len(rows)) if rows else 0
    domain_floor = min(by_domain.values()) if by_domain else 0
    card_pct = mastered_cards / len(cards) if cards else 0
    readiness = round(100 * (0.60 * accuracy + 0.25 * domain_floor + 0.15 * card_pct))
    return attempts, cards, mastered_cards, accuracy, by_domain, readiness


st.title("🎓 NYL Exam Training Center — 3-Day Pass Sprint")
st.caption("Learn → active recall → timed testing → diagnose → recycle misses → prove readiness.")
st.info("The SIE is a FINRA securities exam. Florida 2-15 Health & Life (Including Annuities & Variable Contracts) is a separate Florida insurance license exam. Train them separately.")
st.warning("Original study questions only — not live or recalled exam questions. Verify changing Florida-specific rules and numbers against current Florida DFS-approved material.")

track = st.sidebar.radio("Training track", ["SIE", "Florida 2-15"])
mode = st.sidebar.radio(
    "Mode",
    ["3-Day Mission", "Readiness Dashboard", "Bullet Lessons", "Spaced Flashcards", "Quick Practice", "Timed Simulation", "Missed Question Recycler", "Weak Areas", "Official Sources"],
)
exam_date = st.sidebar.date_input("Exam date", value=st.session_state.exam_date, min_value=date.today())
st.session_state.exam_date = exam_date
days_left = max((exam_date - date.today()).days, 0)
st.sidebar.metric("Days remaining", days_left)

lessons = track_lessons(track)
questions = track_questions(track)
attempts, cards, mastered_cards, accuracy, by_domain, readiness = mastery_stats(track)

if mode == "3-Day Mission":
    st.header(f"{track}: 3-Day Mission Plan")
    if days_left > 3:
        st.success(f"You have {days_left} days. Run this 3-day sprint in the final three days and use the extra time for spaced review.")
    elif days_left == 0:
        st.error("Exam day: do not cram. Use only rapid recall, formulas/definitions and calm review.")
    else:
        st.warning(f"{days_left} day(s) remaining. Treat the schedule below as mandatory high-priority blocks.")
    for plan in THREE_DAY_PLANS[track]:
        with st.expander(plan["day"], expanded=True):
            st.markdown(f"**Goal:** {plan['goal']}")
            for item in plan["blocks"]:
                st.markdown(f"- {item}")
    st.divider()
    st.subheader("Pass-sprint rules")
    st.markdown("- Do not just reread. Every study block must end with recall or questions.\n- Review every wrong answer and every guessed answer.\n- Spend disproportionate SIE time on Products & Risks and Trading/Accounts.\n- Do at least two full timed simulations before exam day.\n- Target 80%+ overall and no domain below 75%; 85%+ repeated simulations is the comfort zone used by this trainer.\n- Stop heavy study the night before and protect sleep.")

elif mode == "Readiness Dashboard":
    st.header(f"{track} Readiness Dashboard")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Readiness", f"{readiness}%")
    c2.metric("Question accuracy", f"{accuracy:.0%}")
    c3.metric("Questions answered", len(attempts))
    c4.metric("Cards mastered", f"{mastered_cards}/{len(cards)}")
    c5.metric("Days left", days_left)
    st.progress(readiness / 100)
    if readiness >= 85 and attempts and all(v >= .75 for v in by_domain.values()):
        st.success("PASS ZONE: current evidence is strong. Keep performance stable and protect sleep.")
    elif readiness >= 75:
        st.warning("BORDERLINE: close weak domains before relying on your score.")
    else:
        st.error("NOT READY YET: use the 3-Day Mission, weak-area drills and missed-question recycler.")
    st.subheader("Domain mastery")
    for domain, domain_accuracy in by_domain.items():
        st.write(f"**{domain}: {domain_accuracy:.0%}**")
        st.progress(domain_accuracy)
    if track == "SIE":
        st.subheader("Official scored-item weighting")
        for domain, meta in SIE_DOMAINS.items():
            st.write(f"**{domain}: {meta['scored_items']} of 75 scored questions ({meta['weight']:.0%})**")
            st.progress(meta["weight"])

elif mode == "Bullet Lessons":
    st.header(f"{track} High-Yield Bullet System")
    domain = st.selectbox("Domain", list(lessons))
    for i, bullet in enumerate(lessons[domain], 1):
        with st.expander(f"{i}. Recall first — then open", expanded=False):
            st.markdown(bullet)
            st.caption("Close this and explain the rule aloud in one sentence.")
    st.info("Retention protocol: read once → close it → explain aloud → answer a related question → revisit misses later.")

elif mode == "Spaced Flashcards":
    st.header(f"{track} Spaced-Repetition Flashcards")
    domain = st.selectbox("Domain", ["All domains"] + list(lessons))
    pool = [x for x in cards if domain == "All domains" or x["domain"] == domain]
    pool.sort(key=lambda x: st.session_state.card_ratings.get(x["id"], 0))
    idx_key = f"card_idx_{track}_{domain}"
    if idx_key not in st.session_state:
        st.session_state[idx_key] = 0
    card = pool[st.session_state[idx_key] % len(pool)]
    rating = st.session_state.card_ratings.get(card["id"], 0)
    st.caption(f"{card['domain']} • mastery {rating}/5")
    st.markdown(f"## {card['prompt']}")
    st.write("Say the answer aloud before revealing it.")
    with st.expander("Reveal answer"):
        st.success(card["answer"])
    cols = st.columns(4)
    ratings = [(1, "Again"), (2, "Hard"), (4, "Good"), (5, "Easy")]
    for col, (score, label) in zip(cols, ratings):
        if col.button(label, use_container_width=True):
            st.session_state.card_ratings[card["id"]] = score
            st.session_state[idx_key] += 1
            st.rerun()
    st.caption("Again/Hard cards stay at the front of the deck. Good/Easy cards count toward mastery.")

elif mode == "Quick Practice":
    st.header(f"{track} Quick Practice")
    domain = st.selectbox("Question set", ["All domains"] + list(lessons))
    pool = questions if domain == "All domains" else [x for x in questions if x["domain"] == domain]
    key = f"quick_{track}_{domain}"
    if key not in st.session_state:
        st.session_state[key] = random.choice(pool)
    qn = st.session_state[key]
    st.caption(qn["domain"])
    st.subheader(qn["q"])
    choice = st.radio("Choose one", qn["choices"], index=None, key=f"choice_{question_id(qn)}_{len(attempts)}")
    if st.button("Submit", type="primary", disabled=choice is None):
        correct = qn["choices"].index(choice) == qn["answer"]
        record_answer(qn, correct, "quick")
        if correct:
            st.success("Correct.")
        else:
            st.error(f"Incorrect. Correct answer: {qn['choices'][qn['answer']]}")
        st.info(qn["why"])
        st.session_state[key] = random.choice(pool)

elif mode == "Timed Simulation":
    st.header(f"{track} Timed Simulation")
    if track == "SIE":
        st.write("**Full mode:** 75 scored-style questions, weighted 12 / 33 / 23 / 7, with a 105-minute target clock. The live exam also contains unscored pretest items.")
        size = st.select_slider("Simulation size", options=[15, 30, 50, 75], value=75)
        minutes = round(105 * size / 75)
    else:
        st.write("Use this as a mixed Florida concept simulation. Confirm the current official Florida candidate information for the live exam's exact administration details.")
        max_size = min(60, len(questions))
        options = [x for x in [15, 30, 45, 60] if x <= max_size]
        size = st.select_slider("Simulation size", options=options, value=options[-1])
        minutes = max(30, round(size * 1.4))
    c1, c2 = st.columns(2)
    if c1.button("Start new simulation", type="primary", use_container_width=True):
        if track == "SIE" and size == 75:
            sim = weighted_sie_sample(75)
        else:
            sim = mixed_sample(track, size)
        st.session_state.simulation = {"track": track, "questions": sim, "minutes": minutes}
        st.session_state.simulation_answers = {}
        st.session_state.simulation_started = datetime.now()
        st.session_state.simulation_submitted = False
        st.rerun()
    sim = st.session_state.simulation
    if sim and sim["track"] == track:
        elapsed = (datetime.now() - st.session_state.simulation_started).total_seconds() / 60
        remaining = max(sim["minutes"] - elapsed, 0)
        st.metric("Target time remaining", f"{int(remaining)} min")
        st.progress(min(elapsed / sim["minutes"], 1.0))
        with st.form("simulation_form"):
            for i, qn in enumerate(sim["questions"], 1):
                st.markdown(f"**{i}. {qn['q']}**")
                st.session_state.simulation_answers[i] = st.radio(
                    f"Question {i}", qn["choices"], index=None, key=f"sim_{i}_{question_id(qn)}", label_visibility="collapsed"
                )
            submitted = st.form_submit_button("Submit simulation", type="primary")
        if submitted:
            correct_count = 0
            unanswered = 0
            review = []
            for i, qn in enumerate(sim["questions"], 1):
                answer = st.session_state.simulation_answers.get(i)
                if answer is None:
                    correct = False
                    unanswered += 1
                else:
                    correct = qn["choices"].index(answer) == qn["answer"]
                correct_count += int(correct)
                record_answer(qn, correct, "simulation")
                if not correct:
                    review.append((i, qn, answer))
            pct = correct_count / len(sim["questions"])
            st.session_state.simulation_submitted = True
            st.subheader(f"Score: {correct_count}/{len(sim['questions'])} — {pct:.0%}")
            if pct >= .85:
                st.success("Strong simulation. Review every miss and guessed answer, then reproduce this score.")
            elif pct >= .70:
                st.warning("Around passing territory for SIE-style scoring, but not a safe margin. Drive toward repeated 80–85%+ practice.")
            else:
                st.error("Below target. Review misses by domain before taking another full simulation.")
            if unanswered:
                st.warning(f"{unanswered} unanswered question(s) were scored incorrect.")
            st.subheader("Review misses")
            for i, qn, answer in review:
                with st.expander(f"Question {i}: {qn['domain']}"):
                    st.write(qn["q"])
                    st.error(f"Your answer: {answer or 'Unanswered'}")
                    st.success(f"Correct: {qn['choices'][qn['answer']]}")
                    st.info(qn["why"])

elif mode == "Missed Question Recycler":
    st.header(f"{track} Missed-Question Recycler")
    missed = set(st.session_state.missed_ids)
    pool = [x for x in questions if question_id(x) in missed]
    if not pool:
        st.success("No recorded misses for this track. Keep testing.")
    else:
        st.write(f"{len(pool)} unique missed question(s) waiting for recovery.")
        qn = random.choice(pool)
        st.caption(qn["domain"])
        st.subheader(qn["q"])
        choice = st.radio("Choose one", qn["choices"], index=None, key=f"recycle_{question_id(qn)}_{len(attempts)}")
        if st.button("Recycle answer", type="primary", disabled=choice is None):
            correct = qn["choices"].index(choice) == qn["answer"]
            record_answer(qn, correct, "recycle")
            if correct:
                st.success("Recovered. Correct.")
                st.session_state.missed_ids = [x for x in st.session_state.missed_ids if x != question_id(qn)]
            else:
                st.error(f"Still missed. Correct: {qn['choices'][qn['answer']]}")
            st.info(qn["why"])

elif mode == "Weak Areas":
    st.header(f"{track} Weak-Area Coach")
    if not attempts:
        st.info("Complete Quick Practice or a simulation first.")
    else:
        ranked = sorted(by_domain.items(), key=lambda x: x[1])
        for domain, domain_accuracy in ranked:
            rows = [x for x in attempts if x["domain"] == domain]
            st.write(f"**{domain}: {domain_accuracy:.0%} ({len(rows)} attempts)**")
            st.progress(domain_accuracy)
            if domain_accuracy < .75:
                st.error("Critical: study bullets + flashcards + 15 focused questions before another simulation.")
            elif domain_accuracy < .85:
                st.warning("Needs reinforcement: recycle misses and retest.")
            else:
                st.success("Strong domain. Maintain with spaced review.")
        weakest = ranked[0][0]
        st.info(f"Next action: work **{weakest}** first. Do not spend equal time on already-strong domains.")

elif mode == "Official Sources":
    st.header("Official / Primary Study Sources")
    st.write("Use these to verify exam structure, current outlines, licensing rules and Florida-specific numbers that may change.")
    for name, url in SOURCES:
        st.markdown(f"- [{name}]({url})")
    st.divider()
    st.markdown("**Trainer policy:** public outlines and official rules → original teaching material and original practice questions. Never use stolen, recalled or purported live exam questions.")
