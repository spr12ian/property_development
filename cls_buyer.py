from cls_buyer_types import BuyerTypes
from dataclasses import dataclass

@dataclass(frozen=True)
class Buyer:
    buyer_type: BuyerTypes
    name: str
