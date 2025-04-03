from cls_buyer_types import get_buyer_type_name, BuyerTypes as BuyerTypes
from decimal import Decimal

properties = {
    "2021-05-10 Charlie": {
        "address": "Glenburnie Lodge, 1 Springfield Drive, London, SW17 0SR",
        "aiming_to_sell_for": Decimal(1000000),
        "buyer_type": BuyerTypes.NON_FIRST_TIME_BUYER,
        "comments": "Charlie paid 2nd home SDLT £36,200 and received a refund of £22,990.56",
        "estate_agent_percentage": int(2),
        "expense_buy_property": Decimal(765000),
        "expense_conveyancing_buy": Decimal(
            1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4
        ),
        "expense_conveyancing_sell": Decimal(2500),
        "expense_insurance": Decimal(400 * 4),
        "expense_renovation": Decimal(860600 - 765000),
        "expense_stamp_duty": Decimal(36200) - Decimal(22990.56),
    },
    "2025-04-08 CB Property Development": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "aiming_to_sell_for": Decimal(480000),
        "buyer_type": BuyerTypes.LIMITED_COMPANY,
        "expense_accountant": Decimal(12 * 89 * 1.2),
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(330000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_insurance": Decimal(400),
        "expense_renovation": Decimal(50000),
    },
    "2025-04-08 Ian B & Ian S": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "aiming_to_sell_for": Decimal(480000),
        "buyer_type": BuyerTypes.SECOND_HOME_BUYER,
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(350000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_insurance": Decimal(400),
        "expense_renovation": Decimal(50000),
    },
    "2025-04-08 Josh": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "aiming_to_sell_for": Decimal(475000),
        "buyer_type": BuyerTypes.FIRST_TIME_BUYER,
        "comments": "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        "estate_agent_percentage": int(2),
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(330000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_insurance": Decimal(400),
        "expense_renovation": Decimal(50000),
        "url": "https://auctions.savills.co.uk/auctions/8-april-2025-185/22-malcolm-road-south-norwood-london-se25-5hg-15765",
    },
    "2025-09-01 Josh": {
        "address": "Somewhere near work, London, SW15 3SA",
        "buyer_type": BuyerTypes.FIRST_TIME_BUYER,
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(400000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_insurance": Decimal(400),
        "expense_renovation": Decimal(0),
    },
    "2025-09-02 Josh": {
        "address": "Somewhere near work, London, SW15 3SA",
        "buyer_type": BuyerTypes.NON_FIRST_TIME_BUYER,
        "comments": "£10,000 stamp duty paid by Charlie & Ians",
        "expense_auction": Decimal(1900),
        "expense_buy_property": Decimal(400000),
        "expense_conveyancing_fee_buy": Decimal(2500),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_insurance": Decimal(400),
        "expense_renovation": Decimal(0),
    },
    "2025-04-16 Josh": {
        "address": "Flat A, 23 Airedale Road, Balham, London, SW12 8SQ",
        "aiming_to_sell_for": Decimal(800000),
        "buyer_type": BuyerTypes.FIRST_TIME_BUYER,
        "comments": "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        "estate_agent_percentage": int(2),
        "expense_auction": Decimal(1750),
        "expense_buy_property": Decimal(300000),
        "expense_conveyancing_fee_buy": Decimal(3000),
        "expense_conveyancing_fee_sell": Decimal(2500),
        "expense_insurance": Decimal(400),
        "expense_renovation": Decimal(100000),
        "url": "https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250415-088",
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
