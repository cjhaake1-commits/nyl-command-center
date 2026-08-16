from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "nyl_command_center.db"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.execute(
            """
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
            """
        )
        conn.commit()


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
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO daily_activity (
                activity_date, outreach_attempts, conversations,
                appointments_booked, appointments_held, sales, commission, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(activity_date) DO UPDATE SET
                outreach_attempts=excluded.outreach_attempts,
                conversations=excluded.conversations,
                appointments_booked=excluded.appointments_booked,
                appointments_held=excluded.appointments_held,
                sales=excluded.sales,
                commission=excluded.commission,
                notes=excluded.notes
            """,
            (
                activity_date,
                outreach_attempts,
                conversations,
                appointments_booked,
                appointments_held,
                sales,
                commission,
                notes,
            ),
        )
        conn.commit()


def get_activity() -> list[dict]:
    with connect() as conn:
        rows = conn.execute("SELECT * FROM daily_activity ORDER BY activity_date ASC").fetchall()
        return [dict(row) for row in rows]


def totals() -> dict:
    with connect() as conn:
        row = conn.execute(
            """
            SELECT
                COALESCE(SUM(outreach_attempts),0) AS outreach_attempts,
                COALESCE(SUM(conversations),0) AS conversations,
                COALESCE(SUM(appointments_booked),0) AS appointments_booked,
                COALESCE(SUM(appointments_held),0) AS appointments_held,
                COALESCE(SUM(sales),0) AS sales,
                COALESCE(SUM(commission),0) AS commission
            FROM daily_activity
            """
        ).fetchone()
        return dict(row)
