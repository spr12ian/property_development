from cls_development import Development
from cls_sdlt_calculator import SDLT_Calculator
from developments import developments
from cls_buyer_types import BuyerTypes
from decimal import Decimal
from cls_sdlt_rates import SDLT_Rates


def analyze_development(development: Development) -> None:
    """
    Analyze a development and print the results.
    :param development: The development to analyze.
    """
    print(f"Analyzing development: {development}")
    print("=" * 40)

    # Get the buyer type
    buyer_type = development.buyer.buyer_type
    print(f"Buyer type: {buyer_type.label}")

    # Get the address
    address = development.dwelling.address
    print(f"Address: {address}")

    # Get the comments
    comments = development.comments
    if comments:
        print(f"Comments: {comments}")

    aiming_to_sell_for = development.aiming_to_sell_for
    if aiming_to_sell_for:
        print(f"Aiming to sell for: £{aiming_to_sell_for:>9,.2f}")

    net_profit_or_loss = development.net_profit_or_loss()
    if net_profit_or_loss:
        print(f"Net profit/loss: £{net_profit_or_loss:>9,.2f}")
    # Get the expenses
    expenses = development.expenses
    if expenses:
        print("Expenses:")
        for expense in expenses:
            print(f"  - {expense.expense_type.label}: £{expense.cost:>9,.2f}")
    # Get the estate agent fee
    estate_agent_fee = development.estate_agent_fee
    if estate_agent_fee:
        print(f"  - Estate agent fee: £{estate_agent_fee:>9,.2f}")
    # Get the auctioneer
    auctioneer = development.dwelling.lot.auction.auctioneer
    if auctioneer:
        print(f"Auctioneer: {auctioneer.name}")
        print(f"  - Buyers fee: £{auctioneer.buyers_fee:>9,.2f}")
        print(f"  - URL: {auctioneer.url}")
    # Get the dwelling
    dwelling = development.dwelling
    if dwelling:
        print(f"  - Dwelling type: {dwelling.dwelling_type.label}")
        print(f"  - Bedrooms: {dwelling.bedrooms}")
        print(f"  - Bathrooms: {dwelling.bathrooms}")
        print(f"  - Garden: {dwelling.garden.label}")
        print(f"  - Parking: {dwelling.parking.label}")
        print(f"  - Garage: {dwelling.garage.label}")
        print(f"  - Leasehold: {dwelling.leasehold.label}")
        print(f"  - Freehold: {dwelling.freehold.label}")
        print(f"  - Leasehold years remaining: {dwelling.leasehold_years_remaining}")
        print(f"  - Freehold years remaining: {dwelling.freehold_years_remaining}")


    # Get the URL
    url = development.dwelling.lot.url
    if url:
        print(f"URL: {url}")


sdlt_calculator = SDLT_Calculator()

for key, development in developments.items():

    print(f"key: {key}")
    print(f"development: {development}")
    print("=" * 40)
    analyze_development(development)


for key, value in developments.items():

    (
        address,
        aiming_to_sell_for,
        buyer_type,
        comments,
        estate_agent_percentage,
        expense_accountant,
        expense_auction,
        expense_buy_development,
        expense_conveyancing_buy,
        expense_conveyancing_sell,
        expense_insurance,
        expense_renovation,
        expense_stamp_duty,
    ) = (
        value["address"],
        value.get("aiming_to_sell_for", None),
        value["buyer_type"],
        value.get("comments", ""),
        value.get("estate_agent_percentage", None),
        value.get("expense_accountant", Decimal(0)),
        value.get("expense_auction", Decimal(0)),
        value["expense_buy_development"],
        value.get("expense_conveyancing_buy", Decimal(0)),
        value.get("expense_conveyancing_sell", Decimal(0)),
        value.get("expense_insurance", Decimal(0)),
        value.get("expense_renovation", Decimal(0)),
        value.get("expense_stamp_duty", None),
    )

    if "estate_agent_percentage" in value:
        expense_estate_agent = (
            aiming_to_sell_for * estate_agent_percentage / Decimal(100)
        )
        print(f"Expense Estate Agent: £{expense_estate_agent:>9,.2f}")
    else:
        expense_estate_agent = Decimal(0)

    if not "expense_stamp_duty" in value:
        expense_stamp_duty = sdlt_calculator.calculate_sdlt(
            buyer_type, expense_buy_development
        )
        print(f"Expense Stamp Duty: £{expense_stamp_duty:>9,.2f}")

    total_expenses = (
        expense_accountant
        + expense_auction
        + expense_buy_development
        + expense_conveyancing_buy
        + expense_conveyancing_sell
        + expense_estate_agent
        + expense_insurance
        + expense_renovation
        + expense_stamp_duty
    )
    print(f"Total expenses: £{total_expenses:>9,.2f}")

    if aiming_to_sell_for is not None:
        pre_tax_profit = aiming_to_sell_for - total_expenses
        print(
            f"Pre-tax profit: £{aiming_to_sell_for:>9,.2f} - £{total_expenses:>9,.2f} = £{pre_tax_profit:>9,.2f}"
        )

        if buyer_type is not BuyerTypes.SECOND_HOME_BUYER:
            capital_gains_tax = Decimal(0)
        else:
            capital_gain = aiming_to_sell_for - total_expenses
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
