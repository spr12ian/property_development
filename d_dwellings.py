from cls_dwelling import Dwelling
from cls_dwelling_types import DwellingTypes
from cls_ownership_types import OwnershipTypes
from d_lots import lots

dwellings: dict[str, Dwelling] = {
    "SE5 5HG": Dwelling(
        address="22 Malcolm Road, London",
        description="Too far from us",
        dwelling_type=DwellingTypes.HOUSE,
        lot=lots["2025_04_08_savills_46"],
        ownership=OwnershipTypes.FREEHOLD,
        postcode="SE5 5HG",
    ),
    "SW8 3ST": Dwelling(
        address="11 Tennyson Street, Battersea, London",
        dwelling_type=DwellingTypes.APARTMENT,
        lot=lots["2025_05_22_allsop_34"],
        ownership=OwnershipTypes.LEASEHOLD,
        postcode="SW8 3ST",
    ),
    "SW17 0SR": Dwelling(
        address="Glenburnie Lodge, 1 Springfield Drive, London",
        bathrooms=2,
        bedrooms=3,
        description="A beautiful property located in a prime area.",
        dwelling_type=DwellingTypes.HOUSE,
        garden=True,
        ownership=OwnershipTypes.FREEHOLD,
        parking=True,
        postcode="SW17 0SR",
    ),
    "SW17 7QW": Dwelling(
        address="Flat B, 47 Hosack Road, Balham, London",
        bathrooms=2,
        bedrooms=2,
        description="First floor flat. No parking. No garden.",
        dwelling_type=DwellingTypes.APARTMENT,
        garden=False,
        ownership=OwnershipTypes.LEASEHOLD,
        parking=False,
        postcode="SW17 7QW",
    ),
    "SW19 1BS": Dwelling(
        address="32a Hotham Road, London",
        bathrooms=1,
        bedrooms=3,
        dwelling_type=DwellingTypes.APARTMENT,
        garden=True,
        ownership=OwnershipTypes.LEASEHOLD,
        leasehold_years_remaining=100,
        lot=lots["2025_05_28_savills_597"],
        parking=False,
        postcode="SW19 1BS",
    ),
}
