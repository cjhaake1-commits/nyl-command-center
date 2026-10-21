from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

import streamlit as st

USER_AGENT = "NYL-Command-Center/1.0 (public professional briefing)"


def _search_config() -> tuple[str, str]:
    try:
        key = st.secrets.get("TAVILY_API_KEY", "")
        endpoint = st.secrets.get("TAVILY_ENDPOINT", "https://api.tavily.com/search")
    except Exception:
        key, endpoint = "", "https://api.tavily.com/search"
    return str(key or os.getenv("TAVILY_API_KEY", "")).strip(), str(endpoint).strip()


def _web_search(query: str) -> tuple[list[dict], str]:
    key, endpoint = _search_config()
    if not key:
        return [], "Search provider is not configured. Use the direct search links below, or configure an approved TAVILY_API_KEY in deployment secrets."
    payload = {
        "api_key": key,
        "query": query,
        "topic": "general",
        "search_depth": "basic",
        "max_results": 7,
        "include_answer": False,
        "include_raw_content": False,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"User-Agent": USER_AGENT, "Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
        items = []
        for row in result.get("results", []):
            title = str(row.get("title") or "").strip()
            url = str(row.get("url") or "").strip()
            snippet = re.sub(r"\s+", " ", str(row.get("content") or "")).strip()
            if title and url.startswith(("http://", "https://")):
                items.append({
                    "title": title,
                    "url": url,
                    "snippet": snippet[:650],
                    "source": str(row.get("source") or ""),
                })
        if not items:
            return [], "Search completed but returned no usable public sources."
        return items, ""
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
        return [], f"Search unavailable ({type(exc).__name__})."


def _query(subject: str, kind: str, context: str) -> str:
    suffix = f" {context.strip()}" if context.strip() else ""
    scopes = {
        "Person / professional": " professional biography role employer public work",
        "Business / organization": " company services leadership news official",
        "Industry / topic": " recent trends official data",
    }
    return f'"{subject.strip()}"{suffix}{scopes[kind]}'


def _has_identifiers(text: str) -> bool:
    patterns = [
        r"\b\d{3}-\d{2}-\d{4}\b",
        r"\b\d{9,}\b",
        r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
        r"\b(?:policy|account|ssn|dob|date of birth)\b",
    ]
    return any(re.search(p, text, re.I) for p in patterns)


def render_subject_briefing() -> None:
    st.title("Quick Subject Briefing")
    st.caption("Prepare with public professional information and source-linked talking points. Search results can be wrong, incomplete, or outdated; open the original source before relying on a fact.")
    kind = st.selectbox("Briefing type", ["Person / professional", "Business / organization", "Industry / topic"])
    subject = st.text_input("Name or subject", placeholder="Person, company, organization, or industry")
    context = st.text_input("Location or professional context (optional)", placeholder="e.g., Orlando, FL • healthcare")
    if st.button("Build briefing", type="primary"):
        combined = f"{subject} {context}"
        if len(subject.strip()) < 2:
            st.warning("Enter a subject to search.")
        elif _has_identifiers(combined):
            st.error("Remove personal identifiers, email addresses, phone numbers, and account or policy references. This is public professional research only.")
        else:
            query = _query(subject, kind, context)
            with st.spinner("Searching public professional sources…"):
                items, error = _web_search(query)
            if error:
                st.warning(error)
            else:
                st.session_state["subject_brief_items"] = items
                st.session_state["subject_brief_query"] = query
                st.session_state["subject_brief_created"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    items = st.session_state.get("subject_brief_items", [])
    query = st.session_state.get("subject_brief_query")
    if items and query:
        st.caption(f"Search run: {st.session_state.get('subject_brief_created', 'time unavailable')} • Query: {query}")
        st.info("This tool does not infer wealth, health, family circumstances, financial need, suitability, or product fit. Treat results as research leads and verify the source and identity.")
        st.subheader("Public-source briefing")
        for i, item in enumerate(items, 1):
            with st.container(border=True):
                st.markdown(f"**{i}. [{item['title']}]({item['url']})**")
                if item.get("source"):
                    st.caption(item["source"])
                if item.get("snippet"):
                    st.write(item["snippet"])
                st.caption("Unverified until you open and review the source.")
        st.subheader("Talking points")
        a, b, c = st.columns(3)
        a.markdown("**Curious opener**\n\n“I saw your work on [confirmed public item]. What are you focused on next?”")
        b.markdown("**Discovery question**\n\n“What changes in your industry or organization are taking most of your attention?”")
        c.markdown("**Permission-based next step**\n\n“If useful, would a short conversation about how I work with people in this area be welcome?”")
        st.caption("Facts should lead to thoughtful questions, not assumptions about a person's finances or need for a product.")
        if st.button("Clear briefing"):
            st.session_state.pop("subject_brief_items", None)
            st.session_state.pop("subject_brief_query", None)
            st.session_state.pop("subject_brief_created", None)
            st.rerun()

    st.divider()
    st.subheader("Use the lookup well")
    st.markdown("- Search public professional, company, and industry sources only.\n- Confirm the identity, date, and context at the original source.\n- Use public events or business changes as a reason to ask a question, not as proof of financial need.\n- Keep personal prospect/client notes in firm-approved systems; this briefing is session-only.")
    st.caption("Direct search options: " + " · ".join([
        f"[Web search](https://www.google.com/search?q={urllib.parse.quote_plus(subject + ' ' + context)})",
        f"[News search](https://news.google.com/search?q={urllib.parse.quote_plus(subject + ' ' + context)})",
        f"[LinkedIn search](https://www.linkedin.com/search/results/people/?keywords={urllib.parse.quote_plus(subject)})",
    ]))
    st.caption("Automated source retrieval requires an approved search-provider key. The page never fabricates results when the key is missing.")
