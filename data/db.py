from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

SQLITE_PATH = Path(__file__).resolve().parent / "nyl_command_center.db"

_ENGINE: Engine | None = None
_BACKEND = "Not initialized"
_STORAGE_ERROR = ""


def _secret_database_url() -> str:
    """Read DATABASE_URL from Streamlit secrets when deployed, without requiring it locally."""
    try:
        import streamlit as st

        value = st.secrets.get("DATABASE_URL", "")
        return str(value).strip() if value else ""
    except Exception:
        return ""


def _configured_database_url() -> str:
    url = os.getenv("DATABASE_URL", "").strip() or _secret_database_url()
    if url.startswith("postgres://"):
        url = "postgresql://" + url[len("postgres://"):]
    return url


def _sqlite_engine() -> Engine:
    return create_engine(f"sqlite:///{SQLITE_PATH}", pool_pre_ping=True, future=True)


def engine() -> Engine:
    """Use PostgreSQL when reachable; otherwise keep the app online with SQLite fallback."""
    global _ENGINE, _BACKEND, _STORAGE_ERROR

    if _ENGINE is not None:
        return _ENGINE

    configured_url = _configured_database_url()
    if configured_url:
        candidate = create_engine(configured_url, pool_pre_ping=True, future=True)
        try:
            with candidate.connect() as conn:
                conn.execute(text("SELECT 1"))
            _ENGINE = candidate
            _BACKEND = "PostgreSQL (persistent)"
            _STORAGE_ERROR = ""
            return _ENGINE
        except SQLAlchemyError as exc:
            candidate.dispose()
            _STORAGE_ERROR = str(exc).splitlines()[0]
            _BACKEND = "SQLite fallback (database connection failed)"

    _ENGINE = _sqlite_engine()
    if not configured_url:
        _BACKEND = "SQLite (temporary on Streamlit Cloud)"
    return _ENGINE


def storage_backend() -> str:
    engine()
    return _BACKEND


def storage_error() -> str:
    engine()
    return _STORAGE_ERROR


def persistent_storage_enabled() -> bool:
    engine()
    return _BACKEND == "PostgreSQL (persistent)"


def _using_sqlite() -> bool:
    return engine().dialect.name == "sqlite"


def init_db() -> None:
    with engine().begin() as conn:
        if _using_sqlite():
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
        if _using_sqlite():
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
