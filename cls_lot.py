from cls_auction import Auction
from cls_property import Property
from dataclasses import dataclass
from gbp import GBP


@dataclass(frozen=True)
class Lot:
    auction: Auction
    guide_price: GBP
    lot_number: int
    property: Property
    url: str
