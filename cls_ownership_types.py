from enum import Enum, auto


class OwnershipTypes(Enum):
    COMMONHOLD = auto()
    FREEHOLD = auto()
    LEASEHOLD = auto()
    SHARE_OF_FREEHOLD = auto()
    # Additional Ownership types can be added as needed

    @property
    def label(self) -> str:
        return self.name.replace("_", " ").title()

    def __str__(self) -> str:
        """
        Return the user-friendly string representation of the OwnershipTypes.
        """
        return self.label

    def __repr__(self) -> str:
        """
        Return the developer-friendly representation of the OwnershipTypes.
        """
        return f"OwnershipTypes.{self.name}"
