from cls_auctioneer import Auctioneer
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Auction:
    auctioneer: Auctioneer
    auction_date: date

    def __str__(self) -> str:
            return f"{self.auction_date.strftime('%Y-%m-%d')} {self.auctioneer}"