from enum import Enum, auto


class ExpenseTypes(Enum):
    ACCOUNTANT = auto()
    CONVEYANCING_FEE_BUY = auto()
    CONVEYANCING_FEE_SELL = auto()
    INSURANCE = auto()
    PROPERTY_COST_PRICE = auto()
    RENOVATION_COST = auto()
    STAMP_DUTY = auto()
    # Additional expense types can be added as needed

    def __str__(self) -> str:
        """
        Returns the expense type as a formatted string.
        """
        return self.name.replace("_", " ").title()
