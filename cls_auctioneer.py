from dataclasses import dataclass
from cls_gbp import GBP


@dataclass(frozen=True)
class Auctioneer:
    buyers_fee: GBP
    name: str
    url: str

    def __str__(self) -> str:
            return f"{self.name}"