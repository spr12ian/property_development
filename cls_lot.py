from cls_auction import Auction
from dataclasses import dataclass
from cls_gbp import GBP

@dataclass(frozen=True)
class Lot:
    auction: Auction
    guide_price: GBP
    lot_number: int
    url: str

    def __str__(self) -> str:
        """
        User-friendly string representation including auction name.
        """
        return f"{self.auction} – Lot {self.lot_number} (Guide: {self.guide_price})"

    def __repr__(self) -> str:
        """
        Developer-friendly string representation.
        """
        return (
            f"Lot(auction={self.auction!r}, "
            f"guide_price={self.guide_price!r}, "
            f"lot_number={self.lot_number}, "
            f"url={self.url!r})"
        )
