from cls_auction import Auction
from dataclasses import dataclass
from cls_gbp import GBP


@dataclass(frozen=True)
class Lot:
    auction: Auction
    guide_price: GBP
    lot_number: int
    url: str
    description: str | None = None
    hammer_price: GBP | None = None

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

    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of the lot.
        The first line is prefixed with `indentation`, and subsequent lines
        are indented further by two additional spaces.
        """
        sub_indent = indentation + "  "

        lines = [
            "Lot Details:",
            f"{sub_indent}{self.auction.details(sub_indent)}",
            f"{sub_indent}Lot number: {self.lot_number}",
            f"{sub_indent}Guide price: {str(self.guide_price)}",
        ]

        if self.hammer_price:
            lines.append(f"{sub_indent}Hammer price: {str(self.hammer_price)}")

        if self.description:
            lines.append(f"{sub_indent}Description: {self.description}")

        lines.append(f"{sub_indent}URL: {self.url}")

        return "\n".join(lines) + "\n"
