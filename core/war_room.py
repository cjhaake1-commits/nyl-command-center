from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from typing import Iterable, Mapping

from core.planner import FunnelAssumptions, GoalPlan

DAY_INDEX = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6,
}


@dataclass
class Mission:
    commission: float
    sales: int
    held_appointments: int
    booked_appointments: int
    conversations: int
    outreach_attempts: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class FunnelMetric:
    stage: str
    actual: float | None
    target: float
    sample_size: int
    status: str

    def to_dict(self) -> dict:
        return asdict(self)


def count_selling_days(start: date, end: date, selling_days: Iterable[str]) -> int:
    """Count selected weekdays inclusively between start and end."""
    if end < start:
        return 0
    selected = {DAY_INDEX[d] for d in selling_days if d in DAY_INDEX}
    if not selected:
        return 0

    total = 0
    cursor = start
    while cursor <= end:
        if cursor.weekday() in selected:
            total += 1
        cursor += timedelta(days=1)
    return total


def _blended_rate(successes: float, trials: float, prior: float, prior_weight: float = 10.0) -> float:
    if trials <= 0:
        return prior
    return (successes + prior * prior_weight) / (trials + prior_weight)


def adaptive_assumptions(
    activity_totals: Mapping[str, float | int],
    baseline: FunnelAssumptions,
    prior_rate_weight: float = 10.0,
    prior_sale_weight: float = 3.0,
) -> FunnelAssumptions:
    """Blend observed production with baseline assumptions so early data does not overreact."""
    outreach = float(activity_totals.get("outreach_attempts", 0) or 0)
    conversations = float(activity_totals.get("conversations", 0) or 0)
    booked = float(activity_totals.get("appointments_booked", 0) or 0)
    held = float(activity_totals.get("appointments_held", 0) or 0)
    sales = float(activity_totals.get("sales", 0) or 0)
    commission = float(activity_totals.get("commission", 0) or 0)

    contact_rate = _blended_rate(conversations, outreach, baseline.contact_rate, prior_rate_weight)
    booking_rate = _blended_rate(booked, conversations, baseline.booking_rate, prior_rate_weight)
    show_rate = _blended_rate(held, booked, baseline.show_rate, prior_rate_weight)
    close_rate = _blended_rate(sales, held, baseline.close_rate, prior_rate_weight)

    if sales > 0:
        avg_commission = (
            commission + baseline.avg_commission_per_sale * prior_sale_weight
        ) / (sales + prior_sale_weight)
    else:
        avg_commission = baseline.avg_commission_per_sale

    return FunnelAssumptions(
        avg_commission_per_sale=max(1.0, avg_commission),
        close_rate=min(1.0, max(0.01, close_rate)),
        show_rate=min(1.0, max(0.01, show_rate)),
        booking_rate=min(1.0, max(0.01, booking_rate)),
        contact_rate=min(1.0, max(0.01, contact_rate)),
    )


def funnel_health(
    activity_totals: Mapping[str, float | int], baseline: FunnelAssumptions
) -> list[FunnelMetric]:
    outreach = int(activity_totals.get("outreach_attempts", 0) or 0)
    conversations = int(activity_totals.get("conversations", 0) or 0)
    booked = int(activity_totals.get("appointments_booked", 0) or 0)
    held = int(activity_totals.get("appointments_held", 0) or 0)
    sales = int(activity_totals.get("sales", 0) or 0)
    commission = float(activity_totals.get("commission", 0) or 0)

    raw = [
        ("Contact rate", conversations / outreach if outreach else None, baseline.contact_rate, outreach),
        ("Booking rate", booked / conversations if conversations else None, baseline.booking_rate, conversations),
        ("Show rate", held / booked if booked else None, baseline.show_rate, booked),
        ("Close rate", sales / held if held else None, baseline.close_rate, held),
        (
            "Avg commission / sale",
            commission / sales if sales else None,
            baseline.avg_commission_per_sale,
            sales,
        ),
    ]

    metrics: list[FunnelMetric] = []
    for stage, actual, target, sample in raw:
        if actual is None:
            status = "need data"
        else:
            ratio = actual / target if target else 1.0
            if ratio < 0.9:
                status = "below target"
            elif ratio > 1.1:
                status = "above target"
            else:
                status = "on target"
        metrics.append(FunnelMetric(stage, actual, target, sample, status))
    return metrics


def weakest_link(metrics: Iterable[FunnelMetric]) -> FunnelMetric | None:
    candidates = [m for m in metrics if m.actual is not None and m.target > 0 and m.sample_size > 0]
    if not candidates:
        return None
    return min(candidates, key=lambda m: float(m.actual) / m.target)


def build_daily_mission(plan: GoalPlan, execution_buffer: float = 1.0) -> Mission:
    buffer = max(1.0, execution_buffer)
    return Mission(
        commission=plan.daily_commission_target * buffer,
        sales=math.ceil(plan.daily_sales_target * buffer),
        held_appointments=math.ceil(plan.daily_held_appointments * buffer),
        booked_appointments=math.ceil(plan.daily_booked_appointments * buffer),
        conversations=math.ceil(plan.daily_conversations * buffer),
        outreach_attempts=math.ceil(plan.daily_outreach_attempts * buffer),
    )


def build_weekly_mission(plan: GoalPlan, selling_days_in_week: int, execution_buffer: float = 1.0) -> Mission:
    days = max(0, min(selling_days_in_week, plan.active_selling_days_remaining))
    if days == 0:
        return Mission(0.0, 0, 0, 0, 0, 0)

    fraction = days / plan.active_selling_days_remaining
    buffer = max(1.0, execution_buffer)
    return Mission(
        commission=plan.remaining_commission * fraction * buffer,
        sales=math.ceil(plan.sales_needed * fraction * buffer),
        held_appointments=math.ceil(plan.held_appointments_needed * fraction * buffer),
        booked_appointments=math.ceil(plan.booked_appointments_needed * fraction * buffer),
        conversations=math.ceil(plan.conversations_needed * fraction * buffer),
        outreach_attempts=math.ceil(plan.outreach_attempts_needed * fraction * buffer),
    )
