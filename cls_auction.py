from cls_auctioneer import Auctioneer
from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Auction:
    auctioneer: Auctioneer
    auction_date: date

    def __str__(self) -> str:
        """
        User-friendly string representation.
        """
        return f"{self.auction_date.strftime('%Y-%m-%d')} {self.auctioneer}"

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """
        return (
            f"Auction(auctioneer={self.auctioneer!r}, "
            f"auction_date={self.auction_date.isoformat()})"
        )
