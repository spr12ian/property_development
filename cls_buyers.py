from cls_buyer_types import BuyerType, BuyerTypes
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Buyer:
    buyer_type: BuyerType

    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

class CB_Developments(Buyer):
    pass

class Charlie(Buyer):
    pass

class IanAndIan(Buyer):
    pass

class Josh(Buyer):
    pass

class Buyers:
    """
    A collection of buyers.
    """
    CB_DEVELOPMENTS = CB_Developments(buyer_type=BuyerTypes.LIMITED_COMPANY)
    CHARLIE = Charlie(buyer_type=BuyerTypes.NON_FIRST_TIME_BUYER)
    IAN_AND_IAN = IanAndIan(buyer_type=BuyerTypes.NON_FIRST_TIME_BUYER)
    JOSH = Josh(buyer_type=BuyerTypes.FIRST_TIME_BUYER)

    @classmethod
    def all(cls):
        return [cls.CB_DEVELOPMENTS, cls.CHARLIE, cls.IAN_AND_IAN, cls.JOSH]