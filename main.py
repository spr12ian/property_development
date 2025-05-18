from cls_helper_sys import SysHelper
from m_developments import print_developments
from m_properties import print_properties
from m_sdlt_rates import print_sdlt_rates


def main():
    sys_helper = SysHelper()

    valid_parameters = ["developments", "properties", "sdlt"]

    if sys_helper.how_many_parameters == 0:
        parameter = "developments"
    else:
        parameter = sys_helper.get_first_parameter()
        if parameter not in valid_parameters:
            print(
                f"Invalid parameter: {parameter}. Valid parameters are: {valid_parameters}"
            )
            exit(1)

    match parameter:
        case "developments":
            print_developments()
        case "properties":
            print_properties()
        case "sdlt":
            print_sdlt_rates()
        case _:
            print(f"Unknown parameter: {parameter}")
            exit(1)


if __name__ == "__main__":
    main()


# for key, value in developments.items():

#     (
#         address,
#         aiming_to_sell_for,
#         buyer_type,
#         comments,
#         estate_agent_percentage,
#         expense_accountant,
#         expense_auction,
#         expense_buy_development,
#         expense_conveyancing_buy,
#         expense_conveyancing_sell,
#         expense_insurance,
#         expense_renovation,
#         expense_stamp_duty,
#     ) = (
#         value["address"],
#         value.get("aiming_to_sell_for", None),
#         value["buyer_type"],
#         value.get("comments", ""),
#         value.get("estate_agent_percentage", None),
#         value.get("expense_accountant", Decimal(0)),
#         value.get("expense_auction", Decimal(0)),
#         value["expense_buy_development"],
#         value.get("expense_conveyancing_buy", Decimal(0)),
#         value.get("expense_conveyancing_sell", Decimal(0)),
#         value.get("expense_insurance", Decimal(0)),
#         value.get("expense_renovation", Decimal(0)),
#         value.get("expense_stamp_duty", None),
#     )

#     if "estate_agent_percentage" in value:
#         expense_estate_agent = (
#             aiming_to_sell_for * estate_agent_percentage / Decimal(100)
#         )
#         print(f"Expense Estate Agent: £{expense_estate_agent:>9,.2f}")
#     else:
#         expense_estate_agent = Decimal(0)

#     if not "expense_stamp_duty" in value:
#         expense_stamp_duty = sdlt_calculator.calculate_sdlt(
#             buyer_type, expense_buy_development
#         )
#         print(f"Expense Stamp Duty: £{expense_stamp_duty:>9,.2f}")

#     total_expenses = (
#         expense_accountant
#         + expense_auction
#         + expense_buy_development
#         + expense_conveyancing_buy
#         + expense_conveyancing_sell
#         + expense_estate_agent
#         + expense_insurance
#         + expense_renovation
#         + expense_stamp_duty
#     )
#     print(f"Total expenses: £{total_expenses:>9,.2f}")

#     if aiming_to_sell_for is not None:
#         pre_tax_profit = aiming_to_sell_for - total_expenses
#         print(
#             f"Pre-tax profit: £{aiming_to_sell_for:>9,.2f} - £{total_expenses:>9,.2f} = £{pre_tax_profit:>9,.2f}"
#         )

#         if buyer_type is not BuyerTypes.SECOND_HOME_BUYER:
#             capital_gains_tax = Decimal(0)
#         else:
#             capital_gain = aiming_to_sell_for - total_expenses
#             print(f"Capital gain: £{capital_gain:>9,.2f}")

#             cgt_allowance = Decimal(3000)
#             if capital_gain > cgt_allowance:
#                 capital_gain = capital_gain - cgt_allowance
#             else:
#                 capital_gain = Decimal(0)
#             print(f"Capital gain after allowance: £{capital_gain:>9,.2f}")
#             if capital_gain < 0:
#                 capital_gain = Decimal(0)

#             capital_gains_tax = capital_gain * Decimal(0.25)
#             print(f"Capital gains tax: £{capital_gains_tax:>9,.2f}")

#         print(f"Net profit: £{pre_tax_profit - capital_gains_tax:>9,.2f}")
