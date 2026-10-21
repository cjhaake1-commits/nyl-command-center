from __future__ import annotations

import json
import urllib.error
import urllib.parse
from datetime import datetime, timezone

from core import market_monitor


def test_chart_quote_parses_price_change_and_timestamp(monkeypatch):
    quote_time = 1_792_613_665

    def fake_fetch_json(url, timeout=12):
        assert "/v8/finance/chart/%5EGSPC?" in url
        assert timeout == 6
        return {
            "chart": {
                "result": [{
                    "meta": {
                        "regularMarketPrice": 105.0,
                        "chartPreviousClose": 100.0,
                        "regularMarketTime": quote_time,
                    },
                    "timestamp": [quote_time],
                }]
            }
        }

    monkeypatch.setattr(market_monitor, "_fetch_json", fake_fetch_json)
    row = market_monitor._fetch_chart_quote("S&P 500", "^GSPC")

    assert row is not None
    assert row["Last"] == 105.0
    assert row["Change"] == 5.0
    assert row["Change %"] == 5.0
    assert row["Quote time (UTC)"] == datetime.fromtimestamp(
        quote_time, tz=timezone.utc
    ).strftime("%Y-%m-%d %H:%M UTC")


def test_market_quotes_fall_back_to_chart_endpoint(monkeypatch):
    def fake_fetch_json(url, timeout=12):
        if "/v7/finance/quote?" in url:
            raise urllib.error.HTTPError(url, 401, "blocked", {}, None)

        assert "/v8/finance/chart/" in url
        encoded_symbol = url.split("/v8/finance/chart/", 1)[1].split("?", 1)[0]
        symbol = urllib.parse.unquote(encoded_symbol)
        return {
            "chart": {
                "result": [{
                    "meta": {
                        "regularMarketPrice": 101.0,
                        "chartPreviousClose": 100.0,
                        "regularMarketTime": 1_792_613_665,
                    },
                    "timestamp": [1_792_613_665],
                }]
            }
        }

    monkeypatch.setattr(market_monitor, "_fetch_json", fake_fetch_json)
    market_monitor.fetch_market_quotes.clear()
    rows, status = market_monitor.fetch_market_quotes()
    market_monitor.fetch_market_quotes.clear()

    assert len(rows) == 10
    assert rows[0]["Symbol"] == "^GSPC"
    assert rows[0]["Last"] == 101.0
    assert "Yahoo Finance chart fallback" in status
