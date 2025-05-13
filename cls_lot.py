from cls_auction import Auction
from dataclasses import dataclass
from cls_gbp import GBP
from typing import Optional


@dataclass(frozen=True)
class Lot:
    auction: Auction
    guide_price: GBP
    lot_number: int
    url: str
    description: Optional[str] = None

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
            f"description={self.description!r}, "
            f"guide_price={self.guide_price!r}, "
            f"lot_number={self.lot_number}, "
            f"url={self.url!r})"
        )

    @property
    def details(self) -> str:
        """
        Returns a detailed string representation of the lot.
        """
        auction = f"  Auction: {self.auction}\n"
        description = f"  Description: {self.description}\n" if self.description else ""
        guide_price = f"  Guide price: {self.guide_price}\n"
        lot_number = f"  Lot number: {self.lot_number}\n"
        url = f"  Lot number: {self.url}\n"

        return (
            f"Lot Details:\n"
            f"{auction if auction else ''}"
            f"{lot_number if lot_number else ''}"
            f"{guide_price if guide_price else ''}"
            f"{description if description else ''}"
            f"{url if url else ''}"
        )
