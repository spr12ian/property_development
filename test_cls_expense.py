from cls_expense import Expense
from cls_expense_types import ExpenseTypes
from cls_gbp import GBP


def test_expense():

    expense = Expense(expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY, cost=GBP(1000))
    assert expense.expense_type == ExpenseTypes.CONVEYANCING_FEE_BUY
    assert expense.cost == GBP(1000)
    #print(str(expense))
    assert str(expense) == "Conveyancing Fee Buy £1,000.00"
    #print(repr(expense))
    assert (
        repr(expense)
        == "Expense(expense_type=ConveyancingFeeBuy(), cost=GBP(1000))"
    )

test_expense()

expenses = (
    Expense(expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY, cost=GBP(1000)),
    Expense(expense_type=ExpenseTypes.RENOVATION_COST, cost=GBP(3000)),
    Expense(expense_type=ExpenseTypes.STAMP_DUTY, cost=GBP(2000)),
)

for expense in sorted(expenses):
    print(f"{expense.expense_type.occurence}: {expense}")


