from gbp import GBP
from dataclasses import dataclass


@dataclass(frozen=True)
class Auctioneer:
    buyers_fee: GBP
    name: str
    url: str
