from cls_buyer_types import get_buyer_type_name, BuyerTypes as BuyerTypes
from decimal import Decimal

properties = {
    "Charlie": {
        "address": "Glenburnie Lodge, 1 Springfield Drive, London, SW17 0SR",
        "buyer_type": BuyerTypes.NON_FIRST_TIME_BUYER,
        "comments": "Charlie paid 2nd home SDLT £36,200 and received a refund of £22,990.56",
        "estate_agent_percentage": int(2),
        "expense_buy_property": Decimal(765000),
        "expense_conveyancing_buy": Decimal(
            1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4
        ),
        "expense_conveyancing_sell": Decimal(2500),
        "expense_renovation": Decimal(850000 - 765000),
        "expense_stamp_duty": Decimal(36200) - Decimal(22990.56),
        "income_sell_property": Decimal(1000000),
    },
    "CB Property Development": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "buyer_type": BuyerTypes.LIMITED_COMPANY,
        "expense_accountant": Decimal(12 * 89 * 1.2),
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(350000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_renovation": Decimal(100000),
        "income_sell_property": Decimal(450000),
    },
    "Ian S": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "buyer_type": BuyerTypes.SECOND_HOME_BUYER,
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(350000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_renovation": Decimal(100000),
        "income_sell_property": Decimal(450000),
    },
}


def format(value):
    """
    Pretty print the value.
    """
    if isinstance(value, Decimal):
        return f"£{value:,.2f}"
    elif isinstance(value, int):
        return f"{value}%"
    elif isinstance(value, str):
        return value
    else:
        return value


def pprint(key):
    """
    Pretty print the property details.
    """
    print(f"Buyer: {key}")
    for k, v in properties[key].items():
        if k == "buyer_type":
            title = get_buyer_type_name(v)
            print(f"{k.replace('_', ' ').title()}: {title}")
        else:
            print(f"{k.replace('_', ' ').title()}: {format(v)}")
