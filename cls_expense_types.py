import re


class ExpenseType:

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
    ACCOUNTANT = Accountant()
    CONVEYANCING_FEE_BUY = ConveyancingFeeBuy()
    CONVEYANCING_FEE_SELL = ConveyancingFeeSell()
    ESTATE_AGENT_FEE = EstateAgentFee()
    INSURANCE = Insurance()
    LOAN_FROM_JOSH = LoanFromJosh()
    OPPORTUNITY_COST = OpportunityCost()
    PROPERTY_COST_PRICE = PropertyCostPrice()
    RENOVATION_COST = RenovationCost()
    STAMP_DUTY = StampDuty()
    SURVEYOR_FEE = SurveyorFee()
    UTILITIES = Utilities()

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
            cls.UTILITIES,
        ]
