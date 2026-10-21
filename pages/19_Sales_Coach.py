from __future__ import annotations

from datetime import date, datetime
from email.utils import parsedate_to_datetime
from html import unescape
import json
import os
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

import streamlit as st

from core.branding import brand_hero

st.set_page_config(page_title="Sales Coach | Chris Haake", page_icon="🧭", layout="wide")
brand_hero(
    "Sales Coach",
    "A weekly operating conversation for goals, decisions, market context, and the next right action.",
    "Monday 10:00 AM • Private working session",
)

NY = ZoneInfo("America/New_York")
now = datetime.now(NY)
week_start = date.fromordinal(now.date().toordinal() - now.weekday())

st.info(
    "Use this page as your Monday check-in and return whenever a question comes up. Do not enter client names, "
    "contact details, account or policy numbers, health information, or confidential NYL material. Notes stay in "
    "the active browser session only. If an AI API key is configured and you confirm the per-message authorization, "
    "your chat text, public headlines, session-added NYL updates, and aggregate trading observation are sent to the "
    "configured OpenAI provider to generate the response."
)

agenda, resources, news, references = st.tabs(["🧭 Weekly Coach", "🌐 Public Intelligence", "📝 NYL Updates", "🔗 NYL Link Library"])

with agenda:
    st.subheader("Monday 10:00 AM weekly reset")
    st.caption(f"Week of {week_start:%A, %B %d, %Y} • Eastern Time")
    st.markdown(
        "Review actual credited production, protect active cases, choose the best qualified opportunities, "
        "schedule relationship-building, and commit to a short list of actions for this week."
    )
    with st.form("weekly_coach_agenda"):
        left, right = st.columns(2)
        wins = left.text_area("What moved forward last week?", height=90, placeholder="Use counts or general themes; no client details.")
        concern = right.text_area("What concern or decision do you want to work through?", height=90, placeholder="Describe the issue without identifying a client.")
        pipeline = left.text_area("What qualified opportunities have a real cause and dated next step?", height=90)
        capacity = right.text_area("What is your capacity and calendar this week?", height=90)
        top_goal = st.text_input("One measurable weekly outcome")
        submitted = st.form_submit_button("Build this week's coaching brief", type="primary")
    if submitted:
        st.session_state["coach_weekly_brief"] = {
            "wins": wins.strip(), "concern": concern.strip(), "pipeline": pipeline.strip(),
            "capacity": capacity.strip(), "goal": top_goal.strip(), "week": week_start.isoformat(),
        }
        st.success("Weekly brief prepared for this session.")
    brief = st.session_state.get("coach_weekly_brief")
    if brief and brief.get("week") == week_start.isoformat():
        st.markdown("#### This week's brief")
        if brief.get("goal"):
            st.metric("Weekly outcome", brief["goal"])
        for label, key in [("Wins", "wins"), ("Concern to resolve", "concern"), ("Qualified opportunities", "pipeline"), ("Capacity", "capacity")]:
            if brief.get(key):
                st.markdown(f"**{label}:** {brief[key]}")
        st.caption("Use the conversation below to turn the concern into options, a prioritized plan, and a clear escalation if needed.")

    st.subheader("Talk it through")
    st.caption(
        "Natural-language coaching uses an OpenAI API key configured in Streamlit secrets or OPENAI_API_KEY. "
        "Without a key, the page uses a labeled structured-guidance fallback and does not pretend to be an AI conversation."
    )
    api_key = None
    try:
        api_key = st.secrets.get("OPENAI_API_KEY")
    except Exception:
        api_key = None
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    model = None
    try:
        model = st.secrets.get("OPENAI_MODEL")
    except Exception:
        model = None
    model = model or os.getenv("OPENAI_MODEL", "gpt-5-mini")
    consent = st.checkbox("I authorize sending this coach message, my session NYL updates, and aggregate trading observation to the configured OpenAI API. They contain no client identifiers or confidential NYL information.", key="coach_safe_input")
    if not api_key:
        st.warning("Guided mode is active. Configure OPENAI_API_KEY in the app's approved secret store to enable natural-language AI replies.")
    messages = st.session_state.setdefault("sales_coach_messages", [])
    for item in messages:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])
    prompt = st.chat_input("What do you want to work through with your coach?")
    if prompt:
        sensitive_patterns = [
            r"\b\d{3}-\d{2}-\d{4}\b",
            r"\b\d{9,}\b",
            r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
            r"\b(?:\+?1[ .-]?)?(?:\(?\d{3}\)?[ .-]?)\d{3}[ .-]?\d{4}\b",
            r"\b(?:policy|account|ssn|social security|date of birth|dob)\s*(?:number|#|is|:)?\s*[A-Z0-9-]{5,}\b",
        ]
        if not consent:
            st.warning("Confirm the note contains no client or confidential NYL information before continuing.")
        elif any(re.search(pattern, prompt, flags=re.I) for pattern in sensitive_patterns):
            st.error("This message looks like it may contain identifying or account information, so it was not sent or added to the session.")
        else:
            messages.append({"role": "user", "content": prompt})
            if api_key:
                system_instructions = (
                    "You are a practical weekly sales and professional-development coach for a newly registered New York Life "
                    "representative in Central Florida. Help the user identify options, set priorities, practice clear client-first "
                    "language, and make measurable weekly plans. Never give individualized securities, investment, insurance, annuity, "
                    "tax, or legal advice; never suggest a product based on compensation; never infer a person's need or wealth. "
                    "For securities, rollover, suitability, product availability, underwriting, commission credit, licensing, NYL policy, "
                    "internal systems, or a compliance concern, tell the user what to ask and direct them to their manager, compliance, "
                    "the appropriate appointed specialist, or current approved NYL source. Separate verified facts from hypotheses. "
                    "When discussing market context, stay educational, state the source and its date, and do not predict prices or "
                    "recommend trades. For each concern, give: (1) what you heard, (2) 2-3 options and trade-offs, (3) the next 3 "
                    "actions with priority, (4) a question to ask the manager when appropriate, and (5) one measurable weekly commitment. "
                    "Do not ask for client-identifying or confidential information."
                )
                brief_text = json.dumps(st.session_state.get("coach_weekly_brief", {}), ensure_ascii=False)[:2500]
                market_text = json.dumps(st.session_state.get("coach_market_headlines", []), ensure_ascii=False)[:5000]
                nyl_updates = json.dumps(st.session_state.get("coach_nyl_updates", []), ensure_ascii=False)[:3000]
                trading_context = str(st.session_state.get("coach_trading_observation", ""))[:1500]
                input_items = [{"role": m["role"], "content": m["content"]} for m in messages[-12:]]
                input_items.insert(0, {"role": "user", "content": f"Current week brief (non-client planning notes): {brief_text}\\n\\nSelected public headlines: {market_text}\\n\\nUser-entered NYL updates (unverified; use as user-provided context): {nyl_updates}\\n\\nAggregate market context supplied by user (not independently verified): {trading_context}"})
                body = json.dumps({"model": model, "instructions": system_instructions, "input": input_items, "max_output_tokens": 900}).encode("utf-8")
                request = urllib.request.Request(
                    "https://api.openai.com/v1/responses", data=body,
                    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                    method="POST",
                )
                try:
                    with urllib.request.urlopen(request, timeout=40) as response:
                        payload = json.loads(response.read().decode("utf-8"))
                    answer = payload.get("output_text", "")
                    if not answer:
                        parts = []
                        for output in payload.get("output", []):
                            for content in output.get("content", []):
                                if content.get("type") == "output_text":
                                    parts.append(content.get("text", ""))
                        answer = "\n".join(parts)
                    if not answer:
                        answer = "I could not read a coaching response from the model. Please try again or use the structured weekly brief."
                except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError) as exc:
                    answer = f"The AI coach request did not complete ({type(exc).__name__}). Your note remains only in this browser session; try again later or use the weekly brief."
                except Exception as exc:
                    answer = f"The AI coach request failed ({type(exc).__name__}). Check the configured model and API connection."
            else:
                lower = prompt.lower()
                if any(word in lower for word in ["compliance", "suitability", "rollover", "recommend", "product", "license", "registration", "commission", "contract", "policy", "case"]):
                    answer = (
                        "I hear a decision that may depend on current NYL rules or case facts.\n\n"
                        "1. **Pause and define the question:** write the decision you need, the facts you have, and what remains unknown.\n"
                        "2. **Use an approved source:** check the current NYL/NYLIFE Securities material and note its date.\n"
                        "3. **Escalate before acting:** take the specific question to your manager, compliance, or the appointed product/benefits specialist. Ask who owns the next step and how activity or case credit is handled.\n\n"
                        "For this week, set a 15-minute follow-up with the right internal resource and keep the opportunity in research status until the gate is resolved. This is structured guidance, not an AI interpretation of the issue."
                    )
                elif any(word in lower for word in ["market", "stock", "fed", "inflation", "rate", "economy", "trading"]):
                    answer = (
                        "Let's keep this educational and source-led. Review the current public headlines in Public Intelligence, "
                        "separate the reported data from your interpretation, and prepare one plain-language explanation plus one "
                        "question for a sophisticated investor. Do not forecast a return or use your trading app as a recommendation. "
                        "If the question turns into an individual allocation or security recommendation, involve your registered supervisor."
                    )
                else:
                    answer = (
                        "Let's turn that into a decision and a small plan. What outcome matters most this week, what is the next "
                        "observable action, and what information is still missing? Start with the highest-quality warm path or active "
                        "case, set a calendar time for the next step, and review the result Friday. If the issue involves NYL policy, "
                        "product access, licensing, suitability, compensation, or a client-specific decision, bring the exact question "
                        "to your manager or the appropriate specialist before acting."
                    )
            messages.append({"role": "assistant", "content": answer})
            st.rerun()
    st.caption("Conversation, weekly notes, and pasted updates are held in Streamlit session state only. They are not stored as prospect or client records.")

with resources:
    st.subheader("Public information for an educated market conversation")
    st.caption(
        "Headlines refresh on page load from public RSS feeds and can be refreshed on demand. This is a source briefing, "
        "not continuous surveillance, a market forecast, or a recommendation."
    )
    FEEDS = [
        ("Federal Reserve", "https://www.federalreserve.gov/feeds/press_all.xml"),
        ("U.S. Securities and Exchange Commission", "https://www.sec.gov/news/pressreleases.rss"),
        ("Bureau of Labor Statistics", "https://www.bls.gov/feed/bls_latest.rss"),
        ("U.S. Energy Information Administration", "https://www.eia.gov/rss/todayinenergy.xml"),
    ]

    @st.cache_data(ttl=1800, show_spinner=False)
    def load_headlines(refresh_key: int = 0):
        found = []
        for source, url in FEEDS:
            req = urllib.request.Request(url, headers={"User-Agent": "NYLCommandCenter/1.0 public-source-brief contact: app-user"})
            try:
                with urllib.request.urlopen(req, timeout=8) as response:
                    raw = response.read(1_000_000)
                root = ET.fromstring(raw)
                for node in root.iter():
                    tag = node.tag.rsplit("}", 1)[-1].lower()
                    if tag not in ("item", "entry"):
                        continue
                    fields = {}
                    for child in list(node):
                        key = child.tag.rsplit("}", 1)[-1].lower()
                        if key == "link":
                            fields[key] = child.attrib.get("href") or (child.text or "").strip()
                        elif child.text:
                            fields[key] = unescape(child.text.strip())
                    title, link = fields.get("title", ""), fields.get("link", "")
                    stamp = fields.get("pubdate") or fields.get("published") or fields.get("updated") or fields.get("date", "")
                    try:
                        published = parsedate_to_datetime(stamp)
                    except Exception:
                        try:
                            published = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
                        except Exception:
                            published = None
                    if title and link:
                        found.append({"source": source, "title": title, "url": link, "published": published.isoformat() if published else "Date not provided"})
            except Exception:
                continue
        found.sort(key=lambda item: item["published"], reverse=True)
        return found[:24], datetime.now(NY).isoformat(timespec="minutes")

    if st.button("Refresh public headlines now", key="refresh_coach_headlines"):
        load_headlines.clear()
    headlines, refreshed_at = load_headlines(int(st.session_state.get("coach_refresh_counter", 0)))
    if st.button("Reload feeds", key="reload_coach_feeds"):
        st.session_state["coach_refresh_counter"] = int(st.session_state.get("coach_refresh_counter", 0)) + 1
        load_headlines.clear()
        st.rerun()
    st.caption(f"Feed check: {refreshed_at} Eastern • successful feed items: {len(headlines)} • cache window: 30 minutes")
    st.session_state["coach_market_headlines"] = headlines[:12]
    if headlines:
        for item in headlines[:16]:
            st.markdown(f"- [{item['title']}]({item['url']})  \n  {item['source']} • {item['published']}")
    else:
        st.warning("Public feeds did not respond. Use the primary-source links below; no headline or market status is being inferred.")
    st.markdown("**NYL and industry updates**")
    st.markdown(
        "- [New York Life newsroom](https://www.newyorklife.com/newsroom)\n"
        "- [FINRA investor insights](https://www.finra.org/investors/insights)\n"
        "- [NAIC consumer and insurance resources](https://content.naic.org/consumer)\n"
        "- [FINRA Series 6 scope](https://www.finra.org/registration-exams-ce/qualification-exams/series6)\n"
        "- [Federal Reserve data and releases](https://www.federalreserve.gov/data.htm)\n"
        "- [BLS news releases](https://www.bls.gov/bls/newsrels.htm)"
    )
    st.markdown("**Trading-app context (optional)**")
    st.caption("This page does not connect to the separate trading application. Share only non-confidential, aggregated observations such as broad index performance, volatility, or sector trends; never paste account, client, or trade identifiers.")
    trading_note = st.text_area("Add a non-confidential market observation to discuss", key="coach_trading_observation", height=90)
    if trading_note.strip():
        st.session_state["coach_trading_observation"] = trading_note.strip()

with news:
    st.subheader("Add a public or approved NYL update")
    st.caption("Use public announcements or non-confidential material that your firm permits you to discuss. This notebook stays in the active session and is not independently verified. When you send a coach prompt, its contents are included only after you confirm the per-message OpenAI sharing authorization.")
    with st.form("coach_news_update"):
        update = st.text_area("What changed, where was it published, and when?", height=130, placeholder="Headline + public URL + date, or a brief non-confidential update.")
        allowed = st.checkbox("I have removed client data and confidential/internal-only details.", key="coach_news_safe")
        add_update = st.form_submit_button("Add update to this session")
    if add_update:
        bad = bool(re.search(r"\b\d{3}-\d{2}-\d{4}\b|\b\d{9,}\b|\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", update, flags=re.I))
        if not allowed:
            st.warning("Confirm the update contains no client data or confidential/internal-only information.")
        elif bad:
            st.error("The update looks like it may contain identifying information and was not saved.")
        elif update.strip():
            st.session_state.setdefault("coach_nyl_updates", []).append({"text": update.strip(), "date": now.isoformat(timespec="minutes")})
            st.success("Update added to this session notebook. It will be shared with the next AI coach prompt only if you confirm the per-message authorization.")
    for item in reversed(st.session_state.get("coach_nyl_updates", [])):
        st.markdown(f"- {item['text']}  \n  Added {item['date']} Eastern")
    if st.session_state.get("coach_trading_observation"):
        st.markdown("**Current trading-app observation**")
        st.write(st.session_state["coach_trading_observation"])
    st.caption("This session notebook is sent with coach prompts only when you confirm the per-message OpenAI sharing authorization. Do not add client or confidential NYL information. Do not treat a public announcement as a change to your license, appointment, product authority, or NYL process; verify those with current official systems and your manager.")


with references:
    st.subheader("NYL Link Library")
    st.caption("Public reference links gathered from the app’s existing planning resources. This is not yet a copy of your Chrome New York Life bookmark folder.")
    starter_links = [
        ("New York Life", "Newsroom", "https://www.newyorklife.com/newsroom"),
        ("New York Life", "Insurance products", "https://www.newyorklife.com/products/insurance"),
        ("New York Life", "Retirement products", "https://www.newyorklife.com/products/retirement"),
        ("New York Life", "Investments", "https://www.newyorklife.com/products/investments"),
        ("New York Life", "NYLIFE Securities products", "https://www.newyorklife.com/securities/products"),
        ("Regulatory and market education", "FINRA Series 6 scope", "https://www.finra.org/registration-exams-ce/qualification-exams/series6"),
        ("Regulatory and market education", "FINRA Series 63 overview", "https://www.finra.org/registration-exams-ce/qualification-exams/series63"),
        ("Regulatory and market education", "FINRA investor insights", "https://www.finra.org/investors/insights"),
        ("Regulatory and market education", "SEC investor resources", "https://www.investor.gov/"),
        ("Regulatory and market education", "NAIC consumer resources", "https://content.naic.org/consumer"),
    ]
    for category in sorted({row[0] for row in starter_links}):
        st.markdown("#### " + category)
        for _, label, url in [row for row in starter_links if row[0] == category]:
            st.markdown("- [" + label + "](" + url + ")")
    st.markdown("#### Add your Chrome New York Life bookmarks")
    st.info("The connected Chrome profile did not expose a readable New York Life bookmark folder to this app. Paste only the links from that folder below, one per line as Title | https://link. Do not paste or upload your full bookmarks export; it may contain unrelated personal links. These additions stay in this browser session.")
    pasted = st.text_area("NYL bookmark links", key="nyl_bookmark_links_input", height=140, placeholder="Advisor portal | https://…\nProduct resource | https://…")
    if st.button("Add links to this session", key="add_nyl_bookmarks"):
        parsed = []
        invalid = []
        for raw_line in pasted.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if "|" in line:
                label, url = [part.strip() for part in line.split("|", 1)]
            else:
                label, url = line, line
            if url.startswith("https://"):
                parsed.append({"label": label or url, "url": url})
            else:
                invalid.append(line)
        if parsed:
            st.session_state["nyl_extra_links"] = parsed
            st.success(str(len(parsed)) + " links added to this session.")
        if invalid:
            st.warning(str(len(invalid)) + " line(s) were skipped because they did not contain an https:// link.")
    extra_links = st.session_state.get("nyl_extra_links", [])
    if extra_links:
        st.markdown("#### Links from your bookmark folder")
        for item in extra_links:
            st.markdown("- [" + item["label"] + "](" + item["url"] + ")")
    st.caption("The link library is session-only. It does not store client records and does not send bookmarks to the AI coach.")
