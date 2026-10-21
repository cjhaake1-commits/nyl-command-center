from __future__ import annotations

import os
import re
from dataclasses import dataclass
from urllib.parse import quote_plus

import requests
import streamlit as st


@dataclass
class SearchItem:
    title: str
    url: str
    snippet: str
    source: str
    published: str = ""


def _search_config() -> tuple[str, str]:
    try:
        key = st.secrets.get("TAVILY_API_KEY", "")
        endpoint = st.secrets.get("TAVILY_ENDPOINT", "https://api.tavily.com/search")
    except Exception:
        key, endpoint = "", "https://api.tavily.com/search"
    return str(key or os.getenv("TAVILY_API_KEY", "")).strip(), str(endpoint).strip()


def search_public_web(query: str, max_results: int = 8) -> tuple[list[SearchItem], str]:
    """Search public web through optional configured Tavily key; never fabricates fallback results."""
    api_key, endpoint = _search_config()
    if not api_key:
        return [], "Public web search is not configured. Add an approved TAVILY_API_KEY secret to enable live subject research."
    try:
        response = requests.post(
            endpoint,
            json={
                "api_key": api_key,
                "query": query,
                "topic": "general",
                "search_depth": "basic",
                "max_results": max_results,
                "include_answer": False,
                "include_raw_content": False,
            },
            timeout=15,
        )
        response.raise_for_status()
        payload = response.json()
        items = []
        for row in payload.get("results", []):
            title = str(row.get("title") or "").strip()
            url = str(row.get("url") or "").strip()
            snippet = re.sub(r"\s+", " ", str(row.get("content") or "")).strip()
            if title and url.startswith(("http://", "https://")):
                items.append(SearchItem(
                    title=title,
                    url=url,
                    snippet=snippet[:700],
                    source=str(row.get("source") or ""),
                    published=str(row.get("published_date") or ""),
                ))
        if not items:
            return [], "Search completed but returned no usable public sources."
        return items, ""
    except (requests.RequestException, ValueError) as exc:
        return [], f"Search unavailable ({type(exc).__name__}). Check provider configuration and try again."


def _subject_query(subject: str, kind: str, location: str) -> str:
    suffix = f" {location}" if location.strip() else ""
    kind_terms = {
        "Person / professional": " professional biography role employer public work",
        "Business / organization": " company services leadership news official",
        "Industry / topic": " latest trends official data",
    }[kind]
    return f'"{subject.strip()}"{suffix}{kind_terms}'


def render_subject_briefing() -> None:
    st.title("Quick Subject Briefing")
    st.caption("Fast, source-linked public research for professional conversations. Search results can be wrong or outdated; verify them before relying on them.")

    with st.form("quick_subject_brief"):
        kind = st.selectbox("Subject type", ["Person / professional", "Business / organization", "Industry / topic"])
        subject = st.text_input("Name or subject", placeholder="Person, firm, organization, or topic")
        location = st.text_input("Location or industry context (optional)", placeholder="e.g. Orlando, FL • healthcare")
        submitted = st.form_submit_button("Build public-source briefing", type="primary")

    if submitted:
        if len(subject.strip()) < 2:
            st.warning("Enter a subject to search.")
        elif re.search(r"\b\d{3}-\d{2}-\d{4}\b|\b\d{9,}\b|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|\b(?:policy|account|ssn|dob)\b", subject + " " + location, flags=re.I):
            st.error("Remove identifiers or personal contact/account information. This tool accepts public professional search terms only.")
        else:
            query = _subject_query(subject, kind, location)
            with st.spinner("Searching public sources…"):
                items, error = search_public_web(query)
            if error:
                st.warning(error)
            else:
                st.session_state["subject_brief_query"] = query
                st.session_state["subject_brief_items"] = [item.__dict__ for item in items]
                st.session_state["subject_brief_created"] = __import__("datetime").datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
                st.session_state.pop("subject_brief_notes", None)

    items = st.session_state.get("subject_brief_items", [])
    query = st.session_state.get("subject_brief_query")
    if items and query:
        st.caption(f"Search run: {st.session_state.get('subject_brief_created', 'time unavailable')} • Query: {query}")
        st.subheader("Verified talking-point workflow")
        st.info("This page does not infer wealth, health, family status, financial need, or suitability. Treat every result as a lead for your own public-source verification.")
        st.markdown("1. **What is confirmed?** Use only facts visible in a cited public source.\n2. **Why could it matter?** Connect the fact to a neutral business or industry question.\n3. **What remains unknown?** Ask rather than assume.\n4. **What is the natural opener?** Show curiosity and ask permission before discussing your work.")
        for i, item in enumerate(items, start=1):
            with st.container(border=True):
                st.markdown(f"**{i}. [{item['title']}]({item['url']})**")
                source_meta = " · ".join(x for x in [item.get("source", ""), item.get("published", "")] if x)
                if source_meta:
                    st.caption(source_meta)
                if item.get("snippet"):
                    st.write(item["snippet"])
                st.caption("Use as an unverified research lead. Open the source and confirm identity, date, and context.")
        st.subheader("Conversation prep")
        prep = st.columns(3)
        prep[0].markdown("**Possible opener**\n\n“I saw your work on [confirmed public item]. What are you focused on next?”")
        prep[1].markdown("**Business question**\n\n“What is changing in your industry or organization that is taking most of your attention?”")
        prep[2].markdown("**Permission close**\n\n“If useful, would a brief conversation about how I work with people in this area be welcome?”")
        if st.button("Clear briefing", key="clear_subject_brief"):
            st.session_state.pop("subject_brief_items", None)
            st.session_state.pop("subject_brief_query", None)
            st.session_state.pop("subject_brief_created", None)
            st.rerun()

    st.divider()
    st.subheader("Research gate")
    st.markdown("- Use public professional or organizational sources only.\n- Confirm identity and recency directly in source material.\n- Keep notes out of this app if they contain client or prospect personal data; enter approved prospect records into Salesforce only after your firm’s rules permit.\n- A public business event can justify a question; it does not establish financial need or product fit.")
    st.caption("Live search requires an approved search-provider key in deployment secrets. No results are synthesized when it is not configured.")
