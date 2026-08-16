from __future__ import annotations

import math
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class FunnelAssumptions:
    avg_commission_per_sale: float = 750.0
    close_rate: float = 0.30
    show_rate: float = 0.75
    booking_rate: float = 0.25
    contact_rate: float = 0.30

    def validate(self) -> None:
        if self.avg_commission_per_sale <= 0:
            raise ValueError("Average commission per sale must be greater than zero.")
        for name in ("close_rate", "show_rate", "booking_rate", "contact_rate"):
            value = getattr(self, name)
            if not 0 < value <= 1:
                raise ValueError(f"{name} must be between 0 and 1.")


@dataclass
class GoalPlan:
    commission_goal: float
    commission_earned: float
    remaining_commission: float
    active_selling_days_remaining: int
    sales_needed: int
    held_appointments_needed: int
    booked_appointments_needed: int
    conversations_needed: int
    outreach_attempts_needed: int
    daily_commission_target: float
    daily_sales_target: float
    daily_held_appointments: float
    daily_booked_appointments: float
    daily_conversations: float
    daily_outreach_attempts: float

    def to_dict(self) -> Dict[str, float | int]:
        return asdict(self)


def build_plan(
    commission_goal: float,
    commission_earned: float,
    active_selling_days_remaining: int,
    assumptions: FunnelAssumptions,
) -> GoalPlan:
    assumptions.validate()
    if commission_goal < 0 or commission_earned < 0:
        raise ValueError("Commission values cannot be negative.")
    if active_selling_days_remaining <= 0:
        raise ValueError("Active selling days remaining must be greater than zero.")

    remaining = max(0.0, commission_goal - commission_earned)
    sales = math.ceil(remaining / assumptions.avg_commission_per_sale) if remaining else 0
    held = math.ceil(sales / assumptions.close_rate) if sales else 0
    booked = math.ceil(held / assumptions.show_rate) if held else 0
    conversations = math.ceil(booked / assumptions.booking_rate) if booked else 0
    outreach = math.ceil(conversations / assumptions.contact_rate) if conversations else 0

    days = active_selling_days_remaining
    return GoalPlan(
        commission_goal=commission_goal,
        commission_earned=commission_earned,
        remaining_commission=remaining,
        active_selling_days_remaining=days,
        sales_needed=sales,
        held_appointments_needed=held,
        booked_appointments_needed=booked,
        conversations_needed=conversations,
        outreach_attempts_needed=outreach,
        daily_commission_target=remaining / days,
        daily_sales_target=sales / days,
        daily_held_appointments=held / days,
        daily_booked_appointments=booked / days,
        daily_conversations=conversations / days,
        daily_outreach_attempts=outreach / days,
    )


def pace_status(goal: float, earned: float, elapsed_days: int, total_days: int = 30) -> Dict[str, float | str]:
    if total_days <= 0:
        raise ValueError("total_days must be greater than zero")
    elapsed = max(0, min(elapsed_days, total_days))
    expected = goal * (elapsed / total_days)
    delta = earned - expected
    pct = (earned / goal * 100.0) if goal > 0 else 100.0
    status = "ahead" if delta > 0.01 else "behind" if delta < -0.01 else "on pace"
    return {
        "expected_commission_to_date": expected,
        "pace_delta": delta,
        "goal_completion_pct": pct,
        "status": status,
    }
