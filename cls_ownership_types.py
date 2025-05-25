import re


class OwnershipType():

    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Commonhold(OwnershipType):
    pass


class Freehold(OwnershipType):
    pass


class Leasehold(OwnershipType):
    pass


class ShareOfFreehold(OwnershipType):
    pass


class OwnershipTypes:
    COMMONHOLD = Commonhold()
    FREEHOLD = Freehold()
    LEASEHOLD = Leasehold()
    SHARE_OF_FREEHOLD = ShareOfFreehold()

    @classmethod
    def all(cls):
        return [cls.COMMONHOLD, cls.FREEHOLD, cls.LEASEHOLD, cls.SHARE_OF_FREEHOLD]
