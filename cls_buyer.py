from cls_buyer_types import BuyerTypes
from dataclasses import dataclass


@dataclass(frozen=True)
class Buyer:
    buyer_type: BuyerTypes
    name: str

    def __str__(self) -> str:
        return f"{self.name} {self.buyer_type}"
