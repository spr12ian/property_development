from cls_buyer import Buyer
from cls_buyer_types import BuyerTypes
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

        self.print_expenses()

        match (self.buyer.buyer_type):
            case BuyerTypes.FIRST_TIME_BUYER:
                print("Buyer: First time buyer")
            case BuyerTypes.NON_FIRST_TIME_BUYER:
                print("Buyer: Non first time buyer")
            case BuyerTypes.SECOND_HOME_BUYER:
                print("Buyer: Second home buyer")
            case BuyerTypes.LIMITED_COMPANY:
                print("Buyer: Limited company")
            case _:
                raise ValueError(f"Unknown buyer type: {self.buyer.buyer_type}")

        if comments := self.comments:
            print(f"Comments: {comments}")

        if aiming_to_sell_for := self.aiming_to_sell_for:

            print(f"{aiming_to_sell_for.fixed_location('Aiming to sell for')}")

            net_profit_or_loss = self.net_profit_or_loss()

            profit_split = net_profit_or_loss / 2

            print(f"{self.total_outgoings.fixed_location('Total outgoings')}")

            print(f"{self.maximum_bid.fixed_location('Maximum bid')}")

            print(f"{net_profit_or_loss.fixed_location('Net profit/loss')}")

            print(f"{profit_split.fixed_location('50/50 split')}")

        return "\n".join(lines) + "\n"

    @property
    def estate_agent_fee(self) -> GBP:
        return self.estate_agent_percentage.of(self.aiming_to_sell_for)

    def net_profit_or_loss(self) -> GBP:
        total_outgoings = self.total_outgoings
        return self.aiming_to_sell_for - total_outgoings

    def print_expenses(self) -> None:
        """
        Print the expenses for this development.
        """
        print(f"{'Expenses':-<40}")
        print(f"{'Description':<20} {'Cost':>20}")
        print("=" * 40)

        # Get the expenses
        expenses = self.expenses
        if expenses:
            print("Expenses:")
            for expense in expenses:
                print(
                    f"{expense.cost.fixed_location(expense.expense_type.label,'  - ')}"
                )

        # Get the estate agent fee
        if estate_agent_fee := self.estate_agent_fee:
            print(f"{estate_agent_fee.fixed_location('Estate agent fee','  - ')}")

    @property
    def maximum_bid(self) -> GBP:
        minimum_acceptable_profit = GBP(60000)
        conservative_sale_price = Percentage(90).of(self.aiming_to_sell_for)
        maximum_expenses=conservative_sale_price-minimum_acceptable_profit
        conservative_profit = max(GBP(0), conservative_sale_price - self.total_outgoings)
        
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
