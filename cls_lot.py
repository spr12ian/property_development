from cls_auction import Auction
from dataclasses import dataclass
from gbp import GBP


@dataclass(frozen=True)
class Lot:
    address: str
    auction: Auction
    description: str
    guide_price: GBP
    lot_number: int
    post_code: str
    url: str | None = None
