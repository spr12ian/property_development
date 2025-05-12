from cls_dwelling import Dwelling
from lots import lots

dwellings: dict[str, Dwelling] = {
    "SE5 5HG": Dwelling(
        address="22 Malcolm Road, London",
        description="Too far from us",
        postcode="SE5 5HG",
    ),
    "SW8 3ST": Dwelling(
        address="11 Tennyson Street, Battersea, London",
        description="VACANT - Leasehold Self Contained Ground Floor Flat",
        postcode="SW8 3ST",
        lot=lots["2025_05_22_allsop_34"],
    ),
    "SW17 0SR": Dwelling(
        address="Glenburnie Lodge, 1 Springfield Drive, London",
        description="A beautiful property located in a prime area.",
        postcode="SW17 0SR",
    ),
}
