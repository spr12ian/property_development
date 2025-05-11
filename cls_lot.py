from cls_auction import Auction
from dataclasses import dataclass
from cls_gbp import GBP


@dataclass(frozen=True)
class Lot:
    auction: Auction
    guide_price: GBP
    lot_number: int
    url: str
