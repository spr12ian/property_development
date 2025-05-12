from cls_buyer_types import BuyerTypes
from dataclasses import dataclass

@dataclass(frozen=True)
class Buyer:
    buyer_type: BuyerTypes
    name: str

    def __str__(self) -> str:
        """
        User-friendly string showing name and buyer type.
        """
        return f"{self.name} ({self.buyer_type})"

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """
        return f"Buyer(name={self.name!r}, buyer_type={self.buyer_type!r})"
