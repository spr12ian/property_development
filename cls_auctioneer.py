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
