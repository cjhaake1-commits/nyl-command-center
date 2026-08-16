from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

SQLITE_PATH = Path(__file__).resolve().parent / "nyl_command_center.db"


def _database_url() -> str:
    url = os.getenv("DATABASE_URL", "").strip()
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    return url or f"sqlite:///{SQLITE_PATH}"


def engine() -> Engine:
    return create_engine(_database_url(), pool_pre_ping=True, future=True)


def init_db() -> None:
    with engine().begin() as conn:
        if _database_url().startswith("sqlite"):
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS daily_activity (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    activity_date TEXT NOT NULL UNIQUE,
                    outreach_attempts INTEGER NOT NULL DEFAULT 0,
                    conversations INTEGER NOT NULL DEFAULT 0,
                    appointments_booked INTEGER NOT NULL DEFAULT 0,
                    appointments_held INTEGER NOT NULL DEFAULT 0,
                    sales INTEGER NOT NULL DEFAULT 0,
                    commission REAL NOT NULL DEFAULT 0,
                    notes TEXT DEFAULT ''
                )
            """))
        else:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS daily_activity (
                    id BIGSERIAL PRIMARY KEY,
                    activity_date VARCHAR(10) NOT NULL UNIQUE,
                    outreach_attempts INTEGER NOT NULL DEFAULT 0,
                    conversations INTEGER NOT NULL DEFAULT 0,
                    appointments_booked INTEGER NOT NULL DEFAULT 0,
                    appointments_held INTEGER NOT NULL DEFAULT 0,
                    sales INTEGER NOT NULL DEFAULT 0,
                    commission DOUBLE PRECISION NOT NULL DEFAULT 0,
                    notes TEXT DEFAULT ''
                )
            """))


def upsert_daily_activity(
    activity_date: str,
    outreach_attempts: int,
    conversations: int,
    appointments_booked: int,
    appointments_held: int,
    sales: int,
    commission: float,
    notes: str = "",
) -> None:
    values = {
        "activity_date": activity_date,
        "outreach_attempts": outreach_attempts,
        "conversations": conversations,
        "appointments_booked": appointments_booked,
        "appointments_held": appointments_held,
        "sales": sales,
        "commission": commission,
        "notes": notes,
    }

    with engine().begin() as conn:
        if _database_url().startswith("sqlite"):
            conn.execute(text("""
                INSERT INTO daily_activity (
                    activity_date, outreach_attempts, conversations,
                    appointments_booked, appointments_held, sales, commission, notes
                ) VALUES (
                    :activity_date, :outreach_attempts, :conversations,
                    :appointments_booked, :appointments_held, :sales, :commission, :notes
                )
                ON CONFLICT(activity_date) DO UPDATE SET
                    outreach_attempts=excluded.outreach_attempts,
                    conversations=excluded.conversations,
                    appointments_booked=excluded.appointments_booked,
                    appointments_held=excluded.appointments_held,
                    sales=excluded.sales,
                    commission=excluded.commission,
                    notes=excluded.notes
            """), values)
        else:
            conn.execute(text("""
                INSERT INTO daily_activity (
                    activity_date, outreach_attempts, conversations,
                    appointments_booked, appointments_held, sales, commission, notes
                ) VALUES (
                    :activity_date, :outreach_attempts, :conversations,
                    :appointments_booked, :appointments_held, :sales, :commission, :notes
                )
                ON CONFLICT (activity_date) DO UPDATE SET
                    outreach_attempts = EXCLUDED.outreach_attempts,
                    conversations = EXCLUDED.conversations,
                    appointments_booked = EXCLUDED.appointments_booked,
                    appointments_held = EXCLUDED.appointments_held,
                    sales = EXCLUDED.sales,
                    commission = EXCLUDED.commission,
                    notes = EXCLUDED.notes
            """), values)


def get_activity() -> list[dict]:
    with engine().connect() as conn:
        rows = conn.execute(text("SELECT * FROM daily_activity ORDER BY activity_date ASC")).mappings().all()
        return [dict(row) for row in rows]


def totals() -> dict:
    with engine().connect() as conn:
        row = conn.execute(text("""
            SELECT
                COALESCE(SUM(outreach_attempts),0) AS outreach_attempts,
                COALESCE(SUM(conversations),0) AS conversations,
                COALESCE(SUM(appointments_booked),0) AS appointments_booked,
                COALESCE(SUM(appointments_held),0) AS appointments_held,
                COALESCE(SUM(sales),0) AS sales,
                COALESCE(SUM(commission),0) AS commission
            FROM daily_activity
        """)).mappings().one()
        return dict(row)
