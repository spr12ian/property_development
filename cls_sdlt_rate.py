from typing import Optional
from cls_gbp import GBP
from cls_sdlt_band import SDLT_Band
from dataclasses import dataclass

@dataclass(frozen=True)
class SDLT_Rate:
    bands: list[SDLT_Band]
    max_price: Optional[GBP] = None
    zero_due_price: Optional[GBP] = None

    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of this SDLT_Rate.
        """
        sub_indent = indentation + "  "
        lines = []
        if self.zero_due_price:
            lines.append(f"{sub_indent}If price is under {str(self.zero_due_price)} no stamp duty is due. Otherwise:")
        for band in self.bands:
            lines.append(f"{sub_indent}{band}")  # Assumes SDLT_Band has __str__ or similar

        if self.max_price:
            lines.append(f"{sub_indent}Max price: {str(self.max_price)}")

        return "\n".join(lines)
