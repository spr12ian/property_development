import re


class ExpenseOccurence:

    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def sort_index(self) -> int:
        return _OCCURRENCE_ORDER[self]


class PrePurchase(ExpenseOccurence):
    pass


class AtPurchase(ExpenseOccurence):
    pass


class AfterPurchase(ExpenseOccurence):
    pass


class PreSale(ExpenseOccurence):
    pass


class AtSale(ExpenseOccurence):
    pass


class AfterSale(ExpenseOccurence):
    pass


class ExpenseOccurences:
    PRE_PURCHASE = PrePurchase()
    AT_PURCHASE = AtPurchase()
    AFTER_PURCHASE = AfterPurchase()
    PRE_SALE = PreSale()
    AT_SALE = AtSale()
    AFTER_SALE = AfterSale()

    @classmethod
    def all(cls):
        return [
            cls.PRE_PURCHASE,
            cls.AT_PURCHASE,
            cls.AFTER_PURCHASE,
            cls.PRE_SALE,
            cls.AT_SALE,
            cls.AFTER_SALE,
        ]


_OCCURRENCE_ORDER = {occ: i for i, occ in enumerate(ExpenseOccurences.all())}
