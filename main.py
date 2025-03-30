from cls_sdlt_calculator import SDLT_Calculator
from properties import properties, pprint
from cls_buyer_types import get_buyer_type_name, BuyerTypes
from decimal import Decimal
from cls_sdlt_rates import SDLT_Rates
from cls_cgt_calculator import CGT_Calculator
from cls_cgt_rates import CGT_Rates


sdlt_calculator = SDLT_Calculator()

for key, value in properties.items():
    pprint(key)

    (
        address,
        buyer_type,
        comments,
        estate_agent_percentage,
        expense_accountant,
        expense_auction,
        expense_buy_property,
        expense_conveyancing_buy,
        expense_conveyancing_sell,
        expense_renovation,
        expense_stamp_duty,
        income_sell_property,
    ) = (
        value["address"],
        value["buyer_type"],
        value.get("comments", ""),
        value.get("estate_agent_percentage", None),
        value.get("expense_accountant", Decimal(0)),
        value.get("expense_auction", Decimal(0)),
        value["expense_buy_property"],
        value.get("expense_conveyancing_buy", Decimal(0)),
        value.get("expense_conveyancing_sell", Decimal(0)),
        value.get("expense_renovation", Decimal(0)),
        value.get("expense_stamp_duty", None),
        value["income_sell_property"],
    )

    if "estate_agent_percentage" in value:
        expense_estate_agent = (
            income_sell_property * estate_agent_percentage / Decimal(100)
        )
        print(f"Expense estate agent: £{expense_estate_agent:>9,.2f}")
    else:
        expense_estate_agent = Decimal(0)

    if not "expense_stamp_duty" in value:
        expense_stamp_duty = sdlt_calculator.calculate_sdlt(
            buyer_type, expense_buy_property
        )
        print(f"Expense stamp duty: £{expense_stamp_duty:>9,.2f}")

    total_expenses = (
        expense_accountant
        + expense_auction
        + expense_buy_property
        + expense_conveyancing_buy
        + expense_conveyancing_sell
        + expense_estate_agent
        + expense_renovation
        + expense_stamp_duty
    )
    print(f"Total expenses: £{total_expenses:>9,.2f}")

    pre_tax_profit = income_sell_property - total_expenses
    print(f"Pre-tax profit: £{pre_tax_profit:>9,.2f}")

    if buyer_type is not BuyerTypes.SECOND_HOME_BUYER:
        capital_gains_tax = Decimal(0)
    else:
        capital_gain = income_sell_property - total_expenses
        print(f"Capital gain: £{capital_gain:>9,.2f}")

        cgt_allowance = Decimal(3000)
        if capital_gain > cgt_allowance:
            capital_gain = capital_gain - cgt_allowance
        else:
            capital_gain = Decimal(0)
        print(f"Capital gain after allowance: £{capital_gain:>9,.2f}")
        if capital_gain < 0:
            capital_gain = Decimal(0)

        capital_gains_tax = capital_gain * Decimal(0.25)
        print(f"Capital gains tax: £{capital_gains_tax:>9,.2f}")

    print(f"Net profit: £{pre_tax_profit - capital_gains_tax:>9,.2f}")

    print("=" * 40)

SDLT_Rates.print_rates()
