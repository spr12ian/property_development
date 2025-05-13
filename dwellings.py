from cls_dwelling import Dwelling
from cls_dwelling_types import DwellingTypes
from cls_ownership_types import OwnershipTypes
from lots import lots

dwellings: dict[str, Dwelling] = {
    "SE5 5HG": Dwelling(
        address="22 Malcolm Road, London",
        description="Too far from us",
        dwelling_type=DwellingTypes.HOUSE,
        ownership=OwnershipTypes.FREEHOLD,
        postcode="SE5 5HG",
    ),
    "SW8 3ST": Dwelling(
        address="11 Tennyson Street, Battersea, London",
        description="VACANT - Leasehold Self Contained Ground Floor Flat",
        dwelling_type=DwellingTypes.APARTMENT,
        ownership=OwnershipTypes.LEASEHOLD,
        postcode="SW8 3ST",
        lot=lots["2025_05_22_allsop_34"],
    ),
    "SW17 0SR": Dwelling(
        address="Glenburnie Lodge, 1 Springfield Drive, London",
        bathrooms=2,
        bedrooms=3,
        description="A beautiful property located in a prime area.",
        dwelling_type=DwellingTypes.HOUSE,
        ownership=OwnershipTypes.FREEHOLD,
        postcode="SW17 0SR",
    ),
}
