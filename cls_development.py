from __future__ import annotations
from cls_buyers import Buyer, Buyers
from cls_development_expense import DevelopmentExpense
from cls_development_stages import DevelopmentStage, DevelopmentStages
from cls_expense_types import ExpenseTypes
from cls_gbp import GBP
from cls_percentage import Percentage
from cls_dwelling import Dwelling
from dataclasses import dataclass, field
from typing import Optional, Tuple


@dataclass(frozen=True)
class Development:
    aiming_to_sell_for: GBP
    estate_agent_percentage: Percentage
    dwelling: Dwelling
    buyer: Buyer = Buyers.CB_DEVELOPMENTS
    comments: str = ""
    expenses: Tuple[DevelopmentExpense, ...] = field(default_factory=tuple)
    stage: DevelopmentStage = DevelopmentStages.UNDER_CONSIDERATION

    def __str__(self) -> str:
        return f"{self.dwelling} {self.buyer}"

    def __post_init__(self):
        if not isinstance(self.expenses, tuple):
            object.__setattr__(self, "expenses", tuple(self.expenses))

    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of the development.
        """
        sub_indent = indentation + "  "

        lines = [
            f"Development Details:",
            f"{sub_indent}{self.dwelling.details(sub_indent)}",
            f"{sub_indent}Buyer: {self.buyer}",
        ]

        if comments := self.comments:
            lines.append(f"{sub_indent}Comments: {comments}")

        self.append_expenses(lines, sub_indent)

        self.stage.append_details(self, lines, sub_indent)

        if aiming_to_sell_for := self.aiming_to_sell_for:

            lines.append(
                f"{self.fixed_location(aiming_to_sell_for, 'Aiming to sell for', sub_indent)}"
            )

            net_profit_or_loss = self.net_profit_or_loss()

            profit_split = net_profit_or_loss / 2

            lines.append(
                f"{self.fixed_location(net_profit_or_loss,'Net profit/loss', sub_indent)}"
            )

            lines.append(
                f"{self.fixed_location(profit_split,'50/50 split', sub_indent)}"
            )

        return "\n".join(lines) + "\n"

    def append_expenses(
        self, lines: Optional[list[str]] = None, sub_indent: str = ""
    ) -> None:
        if lines is None:
            lines = []

        lines.append(
            f"{sub_indent}{'Expense                                     Cost'}"
        )
        lines.append(f"{sub_indent}{'-' * 48}")

        calculated_expenses = self.get_calculated_expenses()
        prefix = f"{sub_indent}  "
        for expense in calculated_expenses:
            lines.append(
                f"{self.fixed_location(expense.cost,expense.expense_type.label,prefix)}"
            )

        total_expenses = sum(
            (expense.cost for expense in calculated_expenses), start=GBP(0)
        )

        prefix = f"{sub_indent}  - "
        lines.append(
            f"{self.fixed_location(total_expenses,'Total expenses',sub_indent)}"
        )

    @property
    def estate_agent_fee(self) -> GBP:
        return self.estate_agent_percentage.of(self.aiming_to_sell_for)

    def fixed_location(self, amount: GBP, label: str = "", prefix: str = "") -> str:
        """
        Returns the amount in a fixed location.
        Ensures the amount is right-aligned to a fixed column.
        """
        LABEL_WIDTH = 25
        AMOUNT_COLUMN = 50  # total characters from start of line to where £xxx.xx ends

        amount_str = f"£{amount:,.2f}"
        label_with_colon = f"{label}:" if label else ""
        left_part = f"{prefix}{label_with_colon:<{LABEL_WIDTH}}"
        padding = max(0, AMOUNT_COLUMN - len(left_part) - len(amount_str))
        output = f"{left_part}{' ' * padding}{amount_str}"
        return output

    def get_calculated_expenses(self) -> Tuple[DevelopmentExpense, ...]:
        """
        Returns a tuple of calculated expenses.
        """
        calculated_expenses: list[DevelopmentExpense] = []
        for expense in self.expenses:
            expense_type = expense.expense_type
            expense_cost = expense.cost
            calculated_expenses.append(
                DevelopmentExpense(
                    expense_type=expense_type,
                    cost=expense_cost,
                )
            )

        # Add the estate agent fee to the expenses
        calculated_expenses.append(
            DevelopmentExpense(
                expense_type=ExpenseTypes.ESTATE_AGENT_FEE,
                cost=self.estate_agent_fee,
            )
        )
        return tuple(calculated_expenses)

    def net_profit_or_loss(self) -> GBP:
        total_outgoings = self.total_outgoings
        return self.aiming_to_sell_for - total_outgoings

    @property
    def maximum_bid(self) -> GBP:
        minimum_acceptable_profit = GBP(60000)
        conservative_sale_price = Percentage(90).of(self.aiming_to_sell_for)
        maximum_expenses = conservative_sale_price - minimum_acceptable_profit
        conservative_profit = max(
            GBP(0), conservative_sale_price - self.total_outgoings
        )

        if conservative_profit < minimum_acceptable_profit:
            return GBP(0)
        else:
            return max(GBP(0), self.aiming_to_sell_for - conservative_profit)

    @property
    def total_outgoings(self) -> GBP:
        total_expenses = sum((e.cost for e in self.expenses), start=GBP(0))
        agent_fee = self.estate_agent_fee
        total_outgoings = total_expenses + agent_fee
        return total_outgoings
