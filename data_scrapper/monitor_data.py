from dataclasses import dataclass


@dataclass
class MonitorData:
    overall_balance: float
    overall_profit: float
    overall_profit_percent: float
    week_profit: float
    week_profit_percent: float
