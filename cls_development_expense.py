from cls_expense_types import ExpenseType
from dataclasses import dataclass
from cls_gbp import GBP


@dataclass(frozen=True)
class DevelopmentExpense:
    expense_type: ExpenseType
    cost: GBP

    def __post_init__(self):
        if self.cost < GBP(0):
            raise ValueError("Amount cannot be negative")

    def __eq__(self, other):
        if not isinstance(other, DevelopmentExpense):
            return NotImplemented
        return self.expense_type == other.expense_type and self.cost == other.cost

    def __hash__(self):
        return hash((self.expense_type, self.cost))

    def __lt__(self, other):
        if not isinstance(other, DevelopmentExpense):
            return NotImplemented
        return self.expense_type < other.expense_type or (
            self.expense_type == other.expense_type and self.cost < other.cost
        )

    def __le__(self, other):
        if not isinstance(other, DevelopmentExpense):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, DevelopmentExpense):
            return NotImplemented
        return not self <= other

    def __ge__(self, other):
        if not isinstance(other, DevelopmentExpense):
            return NotImplemented
        return not self < other

    def __ne__(self, other):
        if not isinstance(other, DevelopmentExpense):
            return NotImplemented
        return not self == other

    def __repr__(self) -> str:
        return f"DevelopmentExpense(expense_type={self.expense_type}, cost={self.cost})"

    def __str__(self) -> str:
        return f"{self.expense_type} {self.cost}"
