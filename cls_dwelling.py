from cls_dwelling_types import DwellingTypes
from cls_lot import Lot
from cls_ownership_types import OwnershipTypes
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Dwelling:
    address: str
    postcode: str
    dwelling_type: DwellingTypes
    ownership: OwnershipTypes
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

    @property
    def details(self) -> str:
        """
        Returns a detailed string representation of the dwelling.
        """

        address = f"  Address: {self.address}, {self.postcode}\n"

        bathrooms = (
            f"  Bathrooms: {self.bathrooms}\n"
            if self.bathrooms and self.bathrooms > 0
            else ""
        )

        bedrooms = (
            f"  Bedrooms: {self.bedrooms}\n"
            if self.bedrooms and self.bedrooms > 0
            else ""
        )

        dwelling_type = f"  Property type: {self.dwelling_type}\n"
        

        garden = (
            f"  Garden: {'Yes' if self.garden else 'No'}\n"
            if self.garden is not None
            else ""
        )

        description = (
            f"  Description: {self.description}\n"
            if self.description
            else ""
        )

        leasehold_years_remaining = (
            f"  Leasehold years remaining: {self.leasehold_years_remaining}\n"
            if self.leasehold_years_remaining and self.leasehold_years_remaining > 0
            else ""
        )

        lot = (
            f"{self.lot.details}\n"
            if self.lot
            else ""
        )

        parking = (
            f"  Parking: {'Yes' if self.parking else 'No'}\n"
            if self.parking is not None
            else ""
        )

        return (
            f"Property Details:\n"
            f"{dwelling_type}"
            f"{address}"
            f"  Ownership: {self.ownership}\n"
            f"{leasehold_years_remaining if leasehold_years_remaining else ''}"
            f"{description if description else ''}"
            f"{bedrooms if bedrooms else ''}"
            f"{bathrooms if bathrooms else ''}"
            f"{garden if garden else ''}"
            f"{lot if lot else ''}"
            f"{parking if parking else ''}"
        )

        print(f"  - Leasehold years remaining: {dwelling.leasehold_years_remaining}")
