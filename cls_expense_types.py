from cls_expense_occurences import ExpenseOccurence, ExpenseOccurences
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class ExpenseType:
    occurence: ExpenseOccurence

    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Accountant(ExpenseType):
    pass


class ConveyancingFeeBuy(ExpenseType):
    pass


class ConveyancingFeeSell(ExpenseType):
    pass


class EstateAgentFee(ExpenseType):
    pass


class Insurance(ExpenseType):
    pass


class LoanFromJosh(ExpenseType):
    pass


class OpportunityCost(ExpenseType):
    pass


class PropertyCostPrice(ExpenseType):
    pass


class RenovationCost(ExpenseType):
    pass


class StampDuty(ExpenseType):
    pass


class SurveyorFee(ExpenseType):
    pass


class Utilities(ExpenseType):
    pass


class ExpenseTypes:
    """
    A collection of expense types.
    """
    ACCOUNTANT = Accountant(occurence=ExpenseOccurences.PRE_PURCHASE)
    CONVEYANCING_FEE_BUY = ConveyancingFeeBuy(occurence=ExpenseOccurences.AT_PURCHASE)
    CONVEYANCING_FEE_SELL = ConveyancingFeeSell(occurence=ExpenseOccurences.AT_SALE)
    ESTATE_AGENT_FEE = EstateAgentFee(occurence=ExpenseOccurences.AT_SALE)
    INSURANCE = Insurance(occurence=ExpenseOccurences.AFTER_PURCHASE)
    LOAN_FROM_JOSH = LoanFromJosh(occurence=ExpenseOccurences.PRE_PURCHASE)
    OPPORTUNITY_COST = OpportunityCost(occurence=ExpenseOccurences.AFTER_PURCHASE)
    PROPERTY_COST_PRICE = PropertyCostPrice(occurence=ExpenseOccurences.PRE_PURCHASE)
    RENOVATION_COST = RenovationCost(occurence=ExpenseOccurences.AFTER_PURCHASE)
    STAMP_DUTY = StampDuty(occurence=ExpenseOccurences.AT_PURCHASE)
    SURVEYOR_FEE = SurveyorFee(occurence=ExpenseOccurences.PRE_PURCHASE)
    UTILITIES = Utilities(occurence=ExpenseOccurences.AFTER_PURCHASE)

    @classmethod
    def all(cls):
        return [
            cls.ACCOUNTANT,
            cls.CONVEYANCING_FEE_BUY,
            cls.CONVEYANCING_FEE_SELL,
            cls.ESTATE_AGENT_FEE,
            cls.INSURANCE,
            cls.LOAN_FROM_JOSH,
            cls.OPPORTUNITY_COST,
            cls.PROPERTY_COST_PRICE,
            cls.RENOVATION_COST,
            cls.STAMP_DUTY,
            cls.SURVEYOR_FEE,
            cls.UTILITIES
        ]