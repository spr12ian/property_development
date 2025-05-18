from cls_buyer_types import BuyerTypes
from cls_sdlt_band import SDLT_Band
from decimal import Decimal
from enum import Enum
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class SDLT_Rates:
    bands: list[SDLT_Band]
    max_price: Optional[Decimal] = None

    def __init__(self, buyer_type: Enum) -> None:
        if not isinstance(buyer_type, BuyerTypes):
            raise ValueError(f"Invalid buyer type: {buyer_type}")

        buyer_data = self.constants.get(buyer_type, {})
        self.buyer_type = buyer_type
        self.rates = buyer_data.get("rates", {})
        self.max_price = buyer_data.get("max_price")  # Might be None
        self.zero_due_price = buyer_data.get("zero_due_price")  # Might be None

    def get_rates(self):
        return self.rates

    def get_max_price(self):
        return self.max_price

    def get_zero_due_price(self):
        return self.zero_due_price

    def get_buyer_type(self):
        return self.buyer_type

    def get_buyer_type_name(self):
        return self.buyer_type.name.replace("_", " ").title()

    
