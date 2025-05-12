from enum import Enum, auto


class DwellingTypes(Enum):
    APARTMENT = auto()
    HOUSE = auto()
    # Additional Dwelling types can be added as needed

    @property
    def label(self) -> str:
        return self.name.replace("_", " ").title()

    def __str__(self) -> str:
        """
        Return the user-friendly string representation of the DwellingTypes.
        """
        return self.label

    def __repr__(self) -> str:
        """
        Return the developer-friendly representation of the DwellingTypes.
        """
        return f"DwellingTypes.{self.name}"
