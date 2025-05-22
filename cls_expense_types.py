from enum import Enum, auto


class ExpenseTypes(Enum):
    ACCOUNTANT = auto()
    CONVEYANCING_FEE_BUY = auto()
    CONVEYANCING_FEE_SELL = auto()
    ESTATE_AGENT_FEE = auto()
    INSURANCE = auto()
    LOAN_FROM_JOSH = auto()
    OPPORTUNITY_COST = auto()
    PROPERTY_COST_PRICE = auto()
    RENOVATION_COST = auto()
    STAMP_DUTY = auto()
    # Additional expense types can be added as needed

    @property
    def label(self) -> str:
        return self.name.replace("_", " ").title()
