from cls_expense_types import ExpenseType
from dataclasses import dataclass
from cls_gbp import GBP


@dataclass(frozen=True)
class Expense:
    expense_type: ExpenseType
    cost: GBP

    def __post_init__(self):
        if self.cost < GBP(0):
            raise ValueError("Amount cannot be negative")

    def __eq__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return self.expense_type == other.expense_type and self.cost == other.cost

    def __hash__(self):
        return hash((self.expense_type, self.cost))

    def __lt__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented

        self_key = (
            self.expense_type.occurence.sort_index(),
            self.expense_type.label,
            self.cost,
        )
        other_key = (
            other.expense_type.occurence.sort_index(),
            other.expense_type.label,
            other.cost,
        )

        return self_key < other_key


    def __le__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return not self <= other

    def __ge__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return not self < other

    def __ne__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return not self == other

    def __repr__(self) -> str:
        return f"Expense(expense_type={self.expense_type!r}, cost={self.cost!r})"

    def __str__(self) -> str:
        return f"{self.expense_type!s} {self.cost!s}"
