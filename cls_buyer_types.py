import re


class BuyerType:
    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class FirstTimeBuyer(BuyerType):
    pass


class NonFirstTimeBuyer(BuyerType):
    pass


class SecondHomeBuyer(BuyerType):
    pass


class LimitedCompany(BuyerType):
    pass


class BuyerTypes:
    FIRST_TIME_BUYER = FirstTimeBuyer()
    NON_FIRST_TIME_BUYER = NonFirstTimeBuyer()
    SECOND_HOME_BUYER = SecondHomeBuyer()
    LIMITED_COMPANY = LimitedCompany()

    @classmethod
    def all(cls):
        return [
            cls.FIRST_TIME_BUYER,
            cls.NON_FIRST_TIME_BUYER,
            cls.SECOND_HOME_BUYER,
            cls.LIMITED_COMPANY,
        ]
