from __future__ import annotations

import random
from datetime import date, datetime, timedelta

import streamlit as st

from core.exam_training import FLASHCARDS, FL_215_LESSONS, QUESTIONS, SIE_DOMAINS, SIE_LESSONS, SOURCES, THREE_DAY_PLANS
from core.florida_215_high_yield import HIGH_YIELD_CARDS, OFFICIAL_ONLY_BUCKETS, PUBLIC_SIGNAL_NOTE, SCENARIO_PATTERNS
from core.fl215_blueprint import CONSENSUS_PRIORITIES, FL215_BLUEPRINT, FL215_EXAM_FACTS, MEMORIZATION_BUCKETS, PUBLIC_STUDY_CONSENSUS

st.set_page_config(page_title="NYL Exam Training Center", page_icon="🎓", layout="wide")

DEFAULTS = {"quiz_history": [], "card_ratings": {}, "missed_ids": [], "simulation": None, "exam_date": date.today()+timedelta(days=3), "hy_ratings": {}, "hy_idx": 0}
for key, value in DEFAULTS.items():
    if key not in st.session_state: st.session_state[key] = value

def lessons_for(track): return SIE_LESSONS if track == "SIE" else FL_215_LESSONS
def questions_for(track): return [x for x in QUESTIONS if x["track"] == track]
def qid(q): return f"{q['track']}|{q['domain']}|{q['q']}"
def record(q, correct, source):
    st.session_state.quiz_history.append({"track":q["track"],"domain":q["domain"],"correct":bool(correct),"source":source,"qid":qid(q),"at":datetime.now().isoformat(timespec="seconds")})
    if not correct: st.session_state.missed_ids.append(qid(q))
def stats(track):
    attempts=[x for x in st.session_state.quiz_history if x["track"]==track]; cards=[x for x in FLASHCARDS if x["track"]==track]
    accuracy=sum(x["correct"] for x in attempts)/len(attempts) if attempts else 0
    by={}
    for domain in lessons_for(track):
        rows=[x for x in attempts if x["domain"]==domain]; by[domain]=sum(x["correct"] for x in rows)/len(rows) if rows else 0
    mastered=sum(st.session_state.card_ratings.get(x["id"],0)>=4 for x in cards); floor=min(by.values()) if by else 0; card_pct=mastered/len(cards) if cards else 0
    return attempts,cards,mastered,accuracy,by,round(100*(.60*accuracy+.25*floor+.15*card_pct))

st.title("🎓 NYL Exam Training Center — 3-Day Pass Sprint")
st.caption("Active recall first. Practice second. Recycle every miss.")
st.warning("Original study material only. Public candidate discussions are used only as topic signals—not as recalled/live exam questions. Current official Florida/Pearson material controls exam facts and state-specific rules.")

track=st.sidebar.radio("Training track",["Florida 2-15","SIE"])
base_modes=["3-Day Mission","Readiness Dashboard"]
if track=="Florida 2-15": base_modes += ["Official Exam Blueprint","Consensus Priority Map","Most-Testable Memory Deck","Recognition Drills"]
base_modes += ["Bullet Lessons","Spaced Flashcards","Quick Practice","Timed Simulation","Missed Question Recycler","Weak Areas","Official Sources"]
mode=st.sidebar.radio("Mode",base_modes)
exam_date=st.sidebar.date_input("Exam date",value=st.session_state.exam_date,min_value=date.today()); st.session_state.exam_date=exam_date; days_left=max((exam_date-date.today()).days,0); st.sidebar.metric("Days remaining",days_left)
lessons=lessons_for(track); questions=questions_for(track); attempts,cards,mastered,accuracy,by_domain,readiness=stats(track)

if mode=="3-Day Mission":
    st.header(f"{track}: 3-Day Mission")
    for plan in THREE_DAY_PLANS[track]:
        with st.expander(plan["day"],expanded=True):
            st.markdown(f"**Goal:** {plan['goal']}")
            for item in plan["blocks"]: st.markdown(f"- {item}")
    if track=="Florida 2-15":
        st.info("Current full exam target: 165 total questions in 165 minutes. Build instant recall first, then recognition, then full-length endurance.")
        st.markdown("**Consensus study rules**")
        for x in PUBLIC_STUDY_CONSENSUS: st.markdown(f"- {x}")

elif mode=="Readiness Dashboard":
    st.header(f"{track} Readiness")
    c1,c2,c3,c4=st.columns(4); c1.metric("Readiness",f"{readiness}%"); c2.metric("Accuracy",f"{accuracy:.0%}"); c3.metric("Questions",len(attempts)); c4.metric("Cards mastered",f"{mastered}/{len(cards)}")
    st.progress(readiness/100)
    if readiness>=85 and attempts: st.success("PASS ZONE — reproduce this performance before exam day.")
    elif readiness>=75: st.warning("BORDERLINE — close weak areas and recycle every miss.")
    else: st.error("NOT READY YET — run the mission and high-yield deck.")
    for d,s in sorted(by_domain.items(),key=lambda x:x[1]): st.write(f"**{d}: {s:.0%}**"); st.progress(s)

elif mode=="Official Exam Blueprint":
    st.header("📋 Current Florida 2-15 Exam Blueprint")
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Total questions",FL215_EXAM_FACTS["total_questions"]); c2.metric("Scored",FL215_EXAM_FACTS["scored_questions"]); c3.metric("Unscored pretest",FL215_EXAM_FACTS["pretest_questions"]); c4.metric("Time",f"{FL215_EXAM_FACTS['time_minutes']} min")
    st.caption("The candidate cannot identify which questions are pretest, so treat all 165 as scored-quality questions.")
    for topic,weight in FL215_BLUEPRINT:
        approx=round(FL215_EXAM_FACTS["scored_questions"]*weight)
        st.write(f"**{topic}: {weight:.0%} (~{approx} scored questions)**"); st.progress(weight)
    st.success("Key takeaway: the three Florida statutes/rules sections combine to 33% of the scored exam. Florida law cannot be an afterthought.")

elif mode=="Consensus Priority Map":
    st.header("🧭 What to Prioritize")
    st.write("Official weighting is the anchor. Public candidate reports only increase drill priority; they never override the official outline.")
    for row in CONSENSUS_PRIORITIES:
        with st.expander(f"{row['priority']} — {row['topic']}", expanded=row["priority"]=="Very high"):
            st.write(row["why"]); st.caption(f"Evidence: {row['basis']}")
    st.subheader("Memorization buckets")
    for bucket,items in MEMORIZATION_BUCKETS.items():
        with st.expander(bucket):
            for item in items: st.markdown(f"- {item}")

elif mode=="Most-Testable Memory Deck":
    st.header("🔥 Florida 2-15 Most-Testable Memory Deck")
    st.info(PUBLIC_SIGNAL_NOTE)
    st.write("This mode is optimized for fast memorization and recognition. Priority 5 cards appear before lower-priority cards you already know.")
    category=st.selectbox("Category",["All"]+sorted({c["category"] for c in HIGH_YIELD_CARDS}))
    pool=[c for c in HIGH_YIELD_CARDS if category=="All" or c["category"]==category]
    pool.sort(key=lambda c:(st.session_state.hy_ratings.get(c["front"],0),-c["priority"]))
    card=pool[st.session_state.hy_idx%len(pool)]; rating=st.session_state.hy_ratings.get(card["front"],0)
    st.caption(f"{card['category']} • priority {'★'*card['priority']} • mastery {rating}/5")
    st.markdown(f"## {card['front']}"); st.write("Say the definition/rule out loud in one sentence.")
    with st.expander("Reveal answer"): st.success(card["back"])
    cols=st.columns(4)
    for col,(score,label) in zip(cols,[(1,"Again"),(2,"Hard"),(4,"Know it"),(5,"Instant")]):
        if col.button(label,use_container_width=True): st.session_state.hy_ratings[card["front"]]=score; st.session_state.hy_idx+=1; st.rerun()
    known=sum(v>=4 for v in st.session_state.hy_ratings.values()); st.progress(known/len(HIGH_YIELD_CARDS)); st.caption(f"Instant/known: {known}/{len(HIGH_YIELD_CARDS)}")
    with st.expander("Numbers and deadlines: official-source-only bucket"):
        for x in OFFICIAL_ONLY_BUCKETS: st.markdown(f"- {x}")

elif mode=="Recognition Drills":
    st.header("⚡ Recognition Drills"); st.write("Goal: identify the concept in under 10 seconds.")
    scenario,answer=random.choice(SCENARIO_PATTERNS); st.subheader(scenario); st.text_input("Name the concept")
    if st.button("Reveal"): st.success(answer); st.caption("If you hesitated, mark that concept Again/Hard in the memory deck.")

elif mode=="Bullet Lessons":
    st.header(f"{track} Bullet Lessons"); domain=st.selectbox("Domain",list(lessons))
    for i,b in enumerate(lessons[domain],1):
        with st.expander(f"{i}. Recall first — then reveal"): st.write(b)

elif mode=="Spaced Flashcards":
    st.header(f"{track} Flashcards"); domain=st.selectbox("Domain",["All"]+list(lessons)); pool=[x for x in cards if domain=="All" or x["domain"]==domain]; pool.sort(key=lambda x:st.session_state.card_ratings.get(x["id"],0)); card=pool[0]
    st.subheader(card["prompt"])
    with st.expander("Reveal"): st.success(card["answer"])
    cols=st.columns(4)
    for col,(score,label) in zip(cols,[(1,"Again"),(2,"Hard"),(4,"Good"),(5,"Easy")]):
        if col.button(label,use_container_width=True): st.session_state.card_ratings[card["id"]]=score; st.rerun()

elif mode=="Quick Practice":
    st.header(f"{track} Quick Practice"); domain=st.selectbox("Set",["All"]+list(lessons)); pool=questions if domain=="All" else [x for x in questions if x["domain"]==domain]; q=random.choice(pool); st.caption(q["domain"]); st.subheader(q["q"]); choice=st.radio("Choose one",q["choices"],index=None)
    if st.button("Submit",type="primary",disabled=choice is None):
        correct=q["choices"].index(choice)==q["answer"]; record(q,correct,"quick"); st.success("Correct") if correct else st.error(f"Correct answer: {q['choices'][q['answer']]}"); st.info(q["why"])

elif mode=="Timed Simulation":
    st.header(f"{track} Timed Simulation")
    if track=="Florida 2-15":
        size=st.select_slider("Questions",options=[25,50,100,165],value=165)
        target_minutes=round(FL215_EXAM_FACTS["time_minutes"]*size/FL215_EXAM_FACTS["total_questions"])
        st.write(f"Target time: **{target_minutes} minutes**. Full simulation mirrors the current 165-question / 165-minute administration length.")
    else:
        size=st.select_slider("Questions",options=[15,30,50,75],value=75); target_minutes=round(105*size/75)
    if st.button("Start / restart",type="primary"): st.session_state.simulation={"track":track,"questions":random.choices(questions,k=size),"started":datetime.now(),"target_minutes":target_minutes}; st.rerun()
    sim=st.session_state.simulation
    if sim and sim["track"]==track:
        elapsed=(datetime.now()-sim["started"]).total_seconds()/60; remaining=max(sim["target_minutes"]-elapsed,0); st.metric("Target time remaining",f"{int(remaining)} min")
        with st.form("sim"):
            answers={}
            for i,q in enumerate(sim["questions"],1): st.markdown(f"**{i}. {q['q']}**"); answers[i]=st.radio(f"Q{i}",q["choices"],index=None,key=f"sim{i}{qid(q)}",label_visibility="collapsed")
            submit=st.form_submit_button("Score simulation")
        if submit:
            correct=0
            for i,q in enumerate(sim["questions"],1):
                ok=answers[i] is not None and q["choices"].index(answers[i])==q["answer"]; correct+=ok; record(q,ok,"simulation")
            pct=correct/len(sim["questions"]); st.subheader(f"Score: {correct}/{len(sim['questions'])} — {pct:.0%}")
            if pct>=.85: st.success("Strong. Review misses and reproduce this score.")
            elif pct>=.70: st.warning("Passing-range practice result, but keep building margin. Target repeated 80–85%+.")
            else: st.error("Below target. Review misses by topic before another full simulation.")

elif mode=="Missed Question Recycler":
    st.header("Missed Question Recycler"); missed=set(st.session_state.missed_ids); pool=[q for q in questions if qid(q) in missed]
    if not pool: st.success("No recorded misses for this track.")
    else:
        q=random.choice(pool); st.subheader(q["q"]); choice=st.radio("Choose one",q["choices"],index=None)
        if st.button("Submit recycled",disabled=choice is None):
            ok=q["choices"].index(choice)==q["answer"]; record(q,ok,"recycle"); st.success("Recovered") if ok else st.error(f"Correct: {q['choices'][q['answer']]}"); st.info(q["why"])
            if ok: st.session_state.missed_ids=[x for x in st.session_state.missed_ids if x!=qid(q)]

elif mode=="Weak Areas":
    st.header("Weak Areas")
    for d,s in sorted(by_domain.items(),key=lambda x:x[1]): st.write(f"**{d}: {s:.0%}**"); st.progress(s)

elif mode=="Official Sources":
    st.header("Official Sources")
    for name,url in SOURCES: st.markdown(f"- [{name}]({url})")
    if track=="Florida 2-15": st.info("For exact Florida day counts, dollar amounts, age limits, penalties and current administrative requirements, official material outranks public posts and prep-site recollections.")
