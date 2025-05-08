from enum import Enum, auto

# https://www.gov.uk/stamp-duty-land-tax/residential-property-rates


class BuyerTypes(Enum):
    FIRST_TIME_BUYER = auto()
    NON_FIRST_TIME_BUYER = auto()
    SECOND_HOME_BUYER = auto()
    LIMITED_COMPANY = auto()
    # Additional buyer types can be added as needed
    # BUY_TO_LET = auto()
    # FOREIGN_BUYER = auto()
    # TRUST_BUYER = auto()
    # EXEMPTION = auto()
    # OTHER = auto()
    # UNKNOWN = auto()

def get_buyer_type_name(buyer_type):
    """
    Returns the buyer type as a formatted string.
    """
    if not isinstance(buyer_type, BuyerTypes):
        raise ValueError(f"Invalid buyer type: {buyer_type}")

    return buyer_type.name.replace("_", " ").title()
