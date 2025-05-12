from cls_dwelling_types import DwellingTypes
from cls_lot import Lot
from cls_ownership_types import OwnershipTypes
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Dwelling:
    address: str
    description: str
    postcode: str
    dwelling_type: DwellingTypes
    ownership: OwnershipTypes
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    lot: Optional[Lot] = None

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
        return (
            f"Property Details:\n"
            f"  Property type: {self.dwelling_type}\n"
            f"  Address: {self.address}\n"
            f"  Description: {self.description}\n"
            f"  Ownership: {self.ownership}\n"
            f"  Postcode: {self.postcode}\n"
            f"  Lot: {self.lot if self.lot else 'No lot information'}"
        )
        

        print(f"  - Bedrooms: {dwelling.bedrooms}")
        print(f"  - Bathrooms: {dwelling.bathrooms}")
        print(f"  - Garden: {dwelling.garden.label}")
        print(f"  - Parking: {dwelling.parking.label}")
        print(f"  - Garage: {dwelling.garage.label}")
        print(
            f"  - Leasehold years remaining: {dwelling.leasehold_years_remaining}"
        )

