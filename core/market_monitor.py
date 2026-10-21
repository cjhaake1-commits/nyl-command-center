from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree

import pandas as pd
import streamlit as st

CACHE_SECONDS = 15 * 60
USER_AGENT = "NYL-Command-Center/1.0 (public market education dashboard)"


def _fetch_json(url: str, timeout: int = 12) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


@st.cache_data(ttl=CACHE_SECONDS, show_spinner=False)
def fetch_market_quotes() -> tuple[list[dict], str]:
    """Fetch delayed/public quote snapshots; never treats them as client recommendations."""
    symbols = {
        "S&P 500": "^GSPC",
        "Dow Jones": "^DJI",
        "Nasdaq Composite": "^IXIC",
        "Russell 2000": "^RUT",
        "10-Year Treasury Yield": "^TNX",
        "30-Year Treasury Yield": "^TYX",
        "Gold": "GC=F",
        "WTI Crude": "CL=F",
        "U.S. Dollar Index": "DX-Y.NYB",
        "Bitcoin": "BTC-USD",
    }
    query = urllib.parse.urlencode({"symbols": ",".join(symbols.values()), "fields": "symbol,shortName,regularMarketPrice,regularMarketChange,regularMarketChangePercent,regularMarketTime,currency"})
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?{query}"
    try:
        payload = _fetch_json(url)
        results = payload.get("quoteResponse", {}).get("result", [])
        by_symbol = {item.get("symbol"): item for item in results}
        rows = []
        for name, symbol in symbols.items():
            item = by_symbol.get(symbol)
            if not item or item.get("regularMarketPrice") is None:
                continue
            rows.append({
                "Market": name,
                "Symbol": symbol,
                "Last": float(item["regularMarketPrice"]),
                "Change": float(item.get("regularMarketChange") or 0),
                "Change %": float(item.get("regularMarketChangePercent") or 0),
                "Quote time (UTC)": datetime.fromtimestamp(
                    int(item.get("regularMarketTime") or 0), tz=timezone.utc
                ).strftime("%Y-%m-%d %H:%M UTC"),
            })
        return rows, datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError, KeyError) as exc:
        return [], f"Market feed unavailable ({type(exc).__name__})."


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_treasury_yields() -> tuple[list[dict], str]:
    """Read current Treasury par yields from the U.S. Treasury's public XML feed."""
    year = datetime.now(timezone.utc).year
    url = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value={year}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/xml"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            raw = response.read()
        root = ElementTree.fromstring(raw)
        entries = []
        for entry in root.iter():
            fields = {node.tag.split("}")[-1]: node.text for node in entry.iter()}
            if fields.get("NEW_DATE"):
                entries.append(fields)
        if not entries:
            return [], "Treasury yield data unavailable."
        fields = entries[-1]
        columns = [
            ("1 Mo", "BC_1MONTH"), ("3 Mo", "BC_3MONTH"), ("6 Mo", "BC_6MONTH"),
            ("1 Yr", "BC_1YEAR"), ("2 Yr", "BC_2YEAR"), ("5 Yr", "BC_5YEAR"),
            ("10 Yr", "BC_10YEAR"), ("20 Yr", "BC_20YEAR"), ("30 Yr", "BC_30YEAR"),
        ]
        rows = [{"Tenor": tenor, "Yield (%)": float(fields[key])} for tenor, key in columns if fields.get(key) not in (None, "", "N/A")]
        return rows, fields["NEW_DATE"]
    except (urllib.error.URLError, TimeoutError, ElementTree.ParseError, ValueError, KeyError) as exc:
        return [], f"Treasury feed unavailable ({type(exc).__name__})."


@st.cache_data(ttl=15 * 60, show_spinner=False)
def fetch_fed_news() -> list[dict]:
    url = "https://www.federalreserve.gov/feeds/press_all.xml"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/xml"})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            raw = response.read()
        root = ElementTree.fromstring(raw)
        rows = []
        for item in root.findall(".//item")[:10]:
            title = item.findtext("title", "").strip()
            link = item.findtext("link", "").strip()
            date_text = item.findtext("pubDate", "").strip()
            if title and link:
                try:
                    published = parsedate_to_datetime(date_text).astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
                except (TypeError, ValueError, OverflowError):
                    published = date_text
                rows.append({"title": title, "link": link, "published": published})
        return rows
    except (urllib.error.URLError, TimeoutError, ElementTree.ParseError):
        return []


@st.cache_data(ttl=15 * 60, show_spinner=False)
def fetch_market_news(query: str = "Federal Reserve OR Treasury OR inflation OR employment") -> list[dict]:
    """Google News RSS provides headlines/source links; summaries are intentionally omitted."""
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode({"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"})
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/rss+xml, application/xml"})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            root = ElementTree.fromstring(response.read())
        rows = []
        for item in root.findall(".//item")[:12]:
            title = item.findtext("title", "").strip()
            link = item.findtext("link", "").strip()
            date_text = item.findtext("pubDate", "").strip()
            source_node = item.find("source")
            source = source_node.text.strip() if source_node is not None and source_node.text else ""
            if title and link:
                try:
                    published = parsedate_to_datetime(date_text).astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
                except (TypeError, ValueError, OverflowError):
                    published = date_text
                rows.append({"Headline": title, "Source": source, "Published (UTC)": published, "URL": link})
        return rows
    except (urllib.error.URLError, TimeoutError, ElementTree.ParseError):
        return []


def render_market_dashboard() -> None:
    st.title("Market Monitor")
    st.caption("A decision-support briefing for market literacy and client conversations. Data is public and delayed where noted; this page does not recommend a security, fund, bond, or product.")

    if st.button("Refresh public market data", type="primary"):
        st.cache_data.clear()
        st.rerun()

    tab_markets, tab_rates, tab_news, tab_context = st.tabs(
        ["Market snapshot", "Rates", "News", "Conversation context"]
    )

    with tab_markets:
        rows, fetched_at = fetch_market_quotes()
        if rows:
            st.caption(f"Snapshot request completed {fetched_at}. Individual quote timestamps are shown; feeds may be delayed.")
            frame = pd.DataFrame(rows)
            cols = st.columns(5)
            for i, row in enumerate(rows[:10]):
                with cols[i % 5]:
                    st.metric(row["Market"], f"{row['Last']:,.2f}", f"{row['Change']:+,.2f} ({row['Change %']:+.2f}%)")
            st.dataframe(frame, width="stretch", hide_index=True)
            st.line_chart(frame.set_index("Market")[["Change %"]], height=280)
        else:
            st.warning(fetched_at)
            st.info("The market monitor retries on the next page visit or when you press Refresh. It does not invent values when the provider is unavailable.")

    with tab_rates:
        rows, rate_date = fetch_treasury_yields()
        if rows:
            st.caption(f"U.S. Treasury par yield curve • observation date: {rate_date} • sourced from Treasury.gov.")
            curve = pd.DataFrame(rows)
            st.line_chart(curve.set_index("Tenor"), height=300)
            st.dataframe(curve, width="stretch", hide_index=True)
            st.caption("Par yields are reference rates, not a bond's yield to maturity, total return, or a quote for an investable security.")
        else:
            st.warning(rate_date)
        st.markdown("**Interpretation prompts**")
        st.markdown("- Compare short and long maturities; do not infer future rate moves from curve shape alone.\n- Rate changes affect bond prices and reinvestment differently across duration and credit quality.\n- For a specific bond or fund, verify current holdings, duration, credit quality, expenses, liquidity, and prospectus/official offering documents.")

    with tab_news:
        st.subheader("Federal Reserve releases")
        fed = fetch_fed_news()
        if fed:
            for item in fed:
                st.markdown(f"- [{item['title']}]({item['link']}) · {item['published']}")
        else:
            st.info("Federal Reserve news feed is unavailable right now.")
        st.subheader("Broader market headlines")
        query = st.text_input("Headline search", value="Federal Reserve OR Treasury OR inflation OR employment")
        news = fetch_market_news(query)
        if news:
            st.dataframe(pd.DataFrame(news), width="stretch", hide_index=True, column_config={"URL": st.column_config.LinkColumn("Source link")})
        else:
            st.info("No headlines loaded. Refresh later or use the direct source links below.")
        st.markdown("[Federal Reserve press releases](https://www.federalreserve.gov/newsevents/pressreleases.htm) · [U.S. Treasury interest rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates) · [BLS news releases](https://www.bls.gov/bls/newsrels.htm)")

    with tab_context:
        st.subheader("Use market information responsibly")
        st.markdown("Use this panel to explain **what happened and why it may matter**, then verify product and portfolio specifics in current approved materials. Separate observation, interpretation, and uncertainty.")
        st.markdown("1. State the date, source, and measurement.\n2. Describe the movement without attributing a cause unless a source supports it.\n3. Explain how rates, inflation, growth, and risk can affect different asset types.\n4. Name at least one counterpoint or uncertainty.\n5. For a named security or fund, verify current holdings, fees, risks, liquidity, share class, and governing disclosure.\n6. Do not convert a macro view into a recommendation; use required NYL/NYLIFE Securities supervision and disclosures.")
        st.info("This page is market education. It does not create an investment recommendation or replace firm-approved research.")
        st.markdown("**Trading research connection**")
        st.write("The separate trading platform is not currently exposing a stable, read-only six-pillar data feed to this app. No trading code or credentials are imported here. When its owner API is ready, connect only published, timestamped market observations and methodology notes—never account credentials, orders, positions, or client data.")

