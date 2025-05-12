from enum import Enum, auto

class BuyerTypes(Enum):
    FIRST_TIME_BUYER = auto()
    NON_FIRST_TIME_BUYER = auto()
    SECOND_HOME_BUYER = auto()
    LIMITED_COMPANY = auto()
    # Additional buyer types can be added as needed
    
    @property
    def label(self) -> str:
        return self.name.replace("_", " ").title()

    def __str__(self) -> str:
        """
        Return the user-friendly string representation of the BuyerTypes.
        """
        return self.label

    def __repr__(self) -> str:
        """
        Return the developer-friendly representation of the BuyerTypes.
        """
        return f"BuyerTypes.{self.name}"
