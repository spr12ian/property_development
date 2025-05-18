from cls_gbp import GBP
from cls_percentage import Percentage
from dataclasses import dataclass

@dataclass(frozen=True)
class SDLT_Band:
    """
    Represents a band in the SDLT (Stamp Duty Land Tax) rates.
    """
    label: str
    upper_bound: GBP
    rate: Percentage

    def __str__(self) -> str:
        return f"{self.label}: Up to {str(self.upper_bound)} rate is {self.rate}"
    def __repr__(self) -> str:
        return f"Band(upper_bound={self.upper_bound!r}, rate={self.rate!r})"
    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of the band.
        """
        sub_indent = indentation + "  "
        lines = [
            f"Band Details:",
            f"{sub_indent}{self.label}",
            f"{sub_indent}Upper Bound: {self.upper_bound}",
            f"{sub_indent}Rate: {self.rate}",
        ]
        return "\n".join(lines)
