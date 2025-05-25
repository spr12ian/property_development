from cls_dwelling_types import DwellingType
from cls_lot import Lot
from cls_ownership_types import OwnershipType
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Dwelling:
    address: str
    postcode: str
    dwelling_type: DwellingType
    ownership: OwnershipType
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    description: Optional[str] = None
    garden: Optional[bool] = None
    leasehold_years_remaining: Optional[int] = None
    lot: Optional[Lot] = None
    parking: Optional[bool] = None

    def __str__(self) -> str:
        """
        User-friendly string representation with optional lot information.
        """
        lot_info = f", {self.lot}" if self.lot else ""
        return f"{self.address}, {self.postcode}{lot_info}"

    def __repr__(self) -> str:
        """
        Developer-friendly string representation.
        """
        return (
            f"Property(address={self.address!r}, "
            f"description={self.description!r}, "
            f"postcode={self.postcode!r}, "
            f"lot={self.lot!r})"
        )

    def details(self, indentation: str = "") -> str:
        """
        Returns a detailed string representation of the dwelling.
        """
        sub_indent = indentation + "  "

        lines = [
            f"Property Details:",
            f"{sub_indent}Property type: {self.dwelling_type}",
            f"{sub_indent}Address: {self.address}, {self.postcode}",
            f"{sub_indent}Ownership: {self.ownership}",
        ]

        if self.leasehold_years_remaining and self.leasehold_years_remaining > 0:
            lines.append(
                f"{sub_indent}Leasehold years remaining: {self.leasehold_years_remaining}"
            )

        if self.description:
            lines.append(f"{sub_indent}Description: {self.description}")

        if self.bedrooms and self.bedrooms > 0:
            lines.append(f"{sub_indent}Bedrooms: {self.bedrooms}")

        if self.bathrooms and self.bathrooms > 0:
            lines.append(f"{sub_indent}Bathrooms: {self.bathrooms}")

        if self.garden is not None:
            lines.append(f"{sub_indent}Garden: {'Yes' if self.garden else 'No'}")

        if self.lot:
            lot_details = self.lot.details(sub_indent)
            lines.append(f"{sub_indent}{lot_details.strip()}")

        if self.parking is not None:
            lines.append(f"{sub_indent}Parking: {'Yes' if self.parking else 'No'}")

        return "\n".join(lines) + "\n"
