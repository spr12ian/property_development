from cls_buyer import Buyer
from cls_development_expense import DevelopmentExpense
from cls_gbp import GBP
from cls_percentage import Percentage
from cls_dwelling import Dwelling
from dataclasses import dataclass, field
from typing import Optional, Tuple


@dataclass(frozen=True)
class Development:
    aiming_to_sell_for: GBP
    buyer: Buyer
    comments: str
    estate_agent_percentage: Percentage
    dwelling: Dwelling
    expenses: Tuple[DevelopmentExpense, ...] = field(default_factory=tuple)

    def __str__(self) -> str:
        return f"{self.dwelling} {self.buyer}"

    def __post_init__(self):
        object.__setattr__(self, "expenses", tuple(self.expenses))

    @property
    def estate_agent_fee(self) -> GBP:
        return self.estate_agent_percentage.of(self.aiming_to_sell_for)

    def net_profit_or_loss(self) -> GBP:
        total_expenses = sum((e.cost for e in self.expenses), start=GBP(0))
        agent_fee = self.estate_agent_fee
        total_outgoings = total_expenses + agent_fee
        return self.aiming_to_sell_for - total_outgoings
