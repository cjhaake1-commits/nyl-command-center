from __future__ import annotations

import json
from datetime import datetime, timezone
from sqlalchemy import text
from data.db import engine


def init_community_tables() -> None:
    db = engine()
    serial = "INTEGER PRIMARY KEY AUTOINCREMENT" if db.dialect.name == "sqlite" else "BIGSERIAL PRIMARY KEY"
    with db.begin() as conn:
        conn.execute(text(f"""CREATE TABLE IF NOT EXISTS community_requests (
            id {serial}, created_at VARCHAR(40) NOT NULL, rep_email VARCHAR(255) NOT NULL,
            request_type VARCHAR(80) NOT NULL, focus VARCHAR(120) NOT NULL,
            territory VARCHAR(120) NOT NULL, request_text TEXT NOT NULL,
            status VARCHAR(40) NOT NULL DEFAULT 'NEW'
        )"""))
        conn.execute(text(f"""CREATE TABLE IF NOT EXISTS community_prospects (
            id {serial}, created_at VARCHAR(40) NOT NULL, rep_email VARCHAR(255) NOT NULL,
            segment VARCHAR(80) NOT NULL, name VARCHAR(255) NOT NULL,
            organization VARCHAR(255) NOT NULL DEFAULT '', city VARCHAR(120) NOT NULL DEFAULT '',
            state VARCHAR(40) NOT NULL DEFAULT '', contact_route VARCHAR(255) NOT NULL DEFAULT '',
            source_url TEXT NOT NULL DEFAULT '', qualification_status VARCHAR(80) NOT NULL DEFAULT 'RESEARCH',
            permission_status VARCHAR(100) NOT NULL DEFAULT 'Not confirmed',
            notes TEXT NOT NULL DEFAULT '', dedupe_key VARCHAR(512) NOT NULL UNIQUE
        )"""))
        conn.execute(text(f"""CREATE TABLE IF NOT EXISTS community_events (
            id {serial}, created_at VARCHAR(40) NOT NULL, rep_email VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL, organizer VARCHAR(255) NOT NULL DEFAULT '',
            start_date VARCHAR(10) NOT NULL, end_date VARCHAR(10) NOT NULL DEFAULT '',
            start_time VARCHAR(40) NOT NULL DEFAULT '', location TEXT NOT NULL DEFAULT '',
            event_type VARCHAR(100) NOT NULL DEFAULT '', source_url TEXT NOT NULL DEFAULT '',
            status VARCHAR(80) NOT NULL DEFAULT 'User-submitted — verify',
            notes TEXT NOT NULL DEFAULT '', dedupe_key VARCHAR(512) NOT NULL UNIQUE
        )"""))


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def submit_request(rep_email: str, request_type: str, focus: str, territory: str, request_text: str) -> None:
    init_community_tables()
    with engine().begin() as conn:
        conn.execute(text("""INSERT INTO community_requests
            (created_at, rep_email, request_type, focus, territory, request_text, status)
            VALUES (:created_at,:rep_email,:request_type,:focus,:territory,:request_text,'NEW')"""),
            dict(created_at=_now(), rep_email=rep_email, request_type=request_type,
                 focus=focus, territory=territory, request_text=request_text))


def list_requests(limit: int = 100) -> list[dict]:
    init_community_tables()
    with engine().connect() as conn:
        rows = conn.execute(text("SELECT * FROM community_requests ORDER BY id DESC LIMIT :limit"),
                            {"limit": int(limit)}).mappings().all()
        return [dict(r) for r in rows]


def save_prospect(rep_email: str, segment: str, name: str, organization: str = "",
                  city: str = "", state: str = "", contact_route: str = "",
                  source_url: str = "", qualification_status: str = "RESEARCH",
                  permission_status: str = "Not confirmed", notes: str = "") -> bool:
    init_community_tables()
    key = "|".join((segment, name, organization, city, state)).casefold().strip()
    with engine().begin() as conn:
        result = conn.execute(text("""INSERT INTO community_prospects
            (created_at,rep_email,segment,name,organization,city,state,contact_route,source_url,
             qualification_status,permission_status,notes,dedupe_key)
            VALUES (:created_at,:rep_email,:segment,:name,:organization,:city,:state,:contact_route,
             :source_url,:qualification_status,:permission_status,:notes,:dedupe_key)
            ON CONFLICT (dedupe_key) DO NOTHING"""),
            dict(created_at=_now(), rep_email=rep_email, segment=segment, name=name,
                 organization=organization, city=city, state=state, contact_route=contact_route,
                 source_url=source_url, qualification_status=qualification_status,
                 permission_status=permission_status, notes=notes, dedupe_key=key))
        return result.rowcount > 0


def list_prospects(segment: str | None = None, limit: int = 2000) -> list[dict]:
    init_community_tables()
    query = "SELECT * FROM community_prospects"
    params = {"limit": int(limit)}
    if segment:
        query += " WHERE segment = :segment"
        params["segment"] = segment
    query += " ORDER BY id DESC LIMIT :limit"
    with engine().connect() as conn:
        rows = conn.execute(text(query), params).mappings().all()
        return [dict(r) for r in rows]


def add_event(rep_email: str, title: str, organizer: str, start_date: str,
              end_date: str = "", start_time: str = "", location: str = "",
              event_type: str = "", source_url: str = "", notes: str = "",
              status: str = "User-submitted — verify") -> bool:
    init_community_tables()
    key = "|".join((title, start_date, location)).casefold().strip()
    with engine().begin() as conn:
        result = conn.execute(text("""INSERT INTO community_events
            (created_at,rep_email,title,organizer,start_date,end_date,start_time,location,event_type,
             source_url,status,notes,dedupe_key)
            VALUES (:created_at,:rep_email,:title,:organizer,:start_date,:end_date,:start_time,:location,
             :event_type,:source_url,:status,:notes,:dedupe_key)
            ON CONFLICT (dedupe_key) DO NOTHING"""),
            dict(created_at=_now(), rep_email=rep_email, title=title, organizer=organizer,
                 start_date=start_date, end_date=end_date, start_time=start_time, location=location,
                 event_type=event_type, source_url=source_url, status=status, notes=notes, dedupe_key=key))
        return result.rowcount > 0


def list_events(limit: int = 2000) -> list[dict]:
    init_community_tables()
    with engine().connect() as conn:
        rows = conn.execute(text("""SELECT * FROM community_events
            ORDER BY start_date ASC, id ASC LIMIT :limit"""), {"limit": int(limit)}).mappings().all()
        return [dict(r) for r in rows]


def import_csv_rows(rep_email: str, records: list[dict], segment: str) -> tuple[int, int]:
    added = 0
    skipped = 0
    for row in records:
        name = str(row.get("name") or row.get("Name") or row.get("Organization") or row.get("organization") or "").strip()
        if not name:
            skipped += 1
            continue
        inserted = save_prospect(
            rep_email=rep_email,
            segment=str(row.get("segment") or segment),
            name=name,
            organization=str(row.get("organization") or row.get("Organization") or ""),
            city=str(row.get("city") or row.get("City") or ""),
            state=str(row.get("state") or row.get("State") or ""),
            contact_route=str(row.get("contact_route") or row.get("Work Phone") or row.get("Work Email") or ""),
            source_url=str(row.get("source_url") or row.get("Source URL") or row.get("Public Source URLs") or ""),
            qualification_status=str(row.get("qualification_status") or row.get("Qualification Status") or "RESEARCH"),
            permission_status=str(row.get("permission_status") or "Not confirmed"),
            notes=str(row.get("notes") or row.get("Notes") or ""),
        )
        added += int(inserted)
        skipped += int(not inserted)
    return added, skipped
