from cls_property import Property

SW17_0SR = Property(
    address="Glenburnie Lodge, 1 Springfield Drive, London, SW17 0SR",
    description="A beautiful property located in a prime area.",
    postcode="SW17 0SR",
)

properties: dict[str, Property] = {
    "SW17_0SR": SW17_0SR,
}