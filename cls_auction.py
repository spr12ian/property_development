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

    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of the auction.
        The first line is prefixed with `indentation`, and subsequent lines
        are indented further by two additional spaces.
        """
        sub_indent = indentation + "  "

        lines = [
            "Auction Details:",
            f"{sub_indent}{self.auctioneer.details(sub_indent)}",
            f"{sub_indent}Auction date: {self.auction_date.strftime('%d/%m/%Y')}",
        ]

        return "\n".join(lines) + "\n"
