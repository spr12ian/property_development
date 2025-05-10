from dataclasses import dataclass


@dataclass(frozen=True)
class Property:
    address: str
    description: str
    postcode: str
