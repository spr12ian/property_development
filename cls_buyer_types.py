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
