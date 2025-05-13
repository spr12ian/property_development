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

    def analyze(self) -> None:
        """
        Analyze this development and print the results.
        """
        print(f"Analyzing development: {self}")
        print("=" * 40)

        print(f"Property: {self.dwelling}")
        print(self.dwelling.details)
        
        print(f"Buyer: {self.buyer}")

        if comments := self.comments:
            print(f"Comments: {comments}")

        print(f"Aiming to sell for: {str(self.aiming_to_sell_for)}")

        # Get the expenses
        expenses = self.expenses
        if expenses:
            print("Expenses:")
            for expense in expenses:
                print(f"  - {expense.expense_type.label}: £{expense.cost:>9,.2f}")

        # Get the estate agent fee
        if estate_agent_fee := self.estate_agent_fee:           
            print(f"  - Estate agent fee: £{estate_agent_fee:>9,.2f}")

        print(f"Total outgoings: £{self.total_outgoings:>9,.2f}")

        print(f"Net profit/loss: £{self.net_profit_or_loss():>9,.2f}")

        if lot := self.dwelling.lot:
            print(f"Lot: {lot}")
            print(f"  - Auction date: {lot.auction.auction_date}")

            # Get the auctioneer
            auctioneer = self.dwelling.lot.auction.auctioneer
            if auctioneer:
                print(f"Auctioneer: {auctioneer.name}")
                print(f"  - Buyers fee: £{auctioneer.buyers_fee:>9,.2f}")

                # Get the URL
                url = self.dwelling.lot.url
                if url:
                    print(f"URL: {url}")

    @property
    def estate_agent_fee(self) -> GBP:
        return self.estate_agent_percentage.of(self.aiming_to_sell_for)

    def net_profit_or_loss(self) -> GBP:
        total_outgoings = self.total_outgoings
        return self.aiming_to_sell_for - total_outgoings

    @property
    def total_outgoings(self):
        total_expenses = sum((e.cost for e in self.expenses), start=GBP(0))
        agent_fee = self.estate_agent_fee
        total_outgoings = total_expenses + agent_fee
        return total_outgoings
