from dataclasses import dataclass
from cls_gbp import GBP

@dataclass(frozen=True)
class Auctioneer:
    buyers_fee: GBP
    name: str
    url: str

    def __str__(self) -> str:
        """
        User-friendly string output.
        """
        return f"{self.name}"

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """
        return (
            f"Auctioneer(name={self.name!r}, "
            f"buyers_fee={self.buyers_fee!r}, "
            f"url={self.url!r})"
        )

    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of the auctioneer.
        The first line is prefixed with `indentation`, and subsequent lines
        are indented further by two additional spaces.
        """
        sub_indent = indentation + "  "

        lines = [
            "Auctioneer Details:",
            f"{sub_indent}Auctioneer: {self.name}",
            f"{sub_indent}Buyer's fee: {str(self.buyers_fee)}",
            f"{sub_indent}Website: {self.url}",
        ]

        return "\n".join(lines) + "\n"
