from cls_auctioneer import Auctioneer
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Auction:
    auctioneer: Auctioneer
    auction_date: date

