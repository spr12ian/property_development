import re


class DwellingType:

    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Apartment(DwellingType):
    pass


class House(DwellingType):
    pass


class DwellingTypes:
    APARTMENT = Apartment()
    HOUSE = House()

    @classmethod
    def all(cls):
        return [cls.APARTMENT, cls.HOUSE]
