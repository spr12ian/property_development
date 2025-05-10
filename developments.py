from auctioneers import allsop, savills
from buyers import cb_developments, charlie, ian_and_ian, josh, josh2
from gbp import GBP
from lots import allsop_2025_05_22_34
import properties

developments = {
    "2021-05-10 Charlie": {
        "aiming_to_sell_for": GBP(1100000),
        "buyer": charlie,
        "comments": "Charlie paid 2nd home SDLT £36,200 and received a refund of £22,990.56",
        "estate_agent_percentage": int(2),
        "expense_buy_property": GBP(765000),
        "expense_conveyancing_buy": GBP(
            1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4
        ),
        "expense_conveyancing_sell": GBP(2500),
        "expense_insurance": GBP(400 * 4),
        "expense_renovation": GBP(860600 - 765000),
        "expense_stamp_duty": GBP(36200) - GBP(22990.56),
        "property": properties.SW17_0SR,
    },
    "2025-04-08 CB Property Development": {
        "property": "22 Malcolm Road, London, SE25 5HG",
        "aiming_to_sell_for": GBP(480000),
        "buyer": cb_developments,
        "expense_accountant": GBP(12 * 89 * 1.2),
        "expense_auction": GBP(1900),
        "expense_buy_property": GBP(354000),
        "expense_conveyancing_fee_buy": GBP(2500),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(50000),
    },
    "2025-04-08 Ian B & Ian S": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "aiming_to_sell_for": GBP(480000),
        "buyer": charlie,
        "expense_auction": GBP(1900),
        "expense_buy_property": GBP(354000),
        "expense_conveyancing_fee_buy": GBP(2500),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(50000),
    },
    "2025-04-08 Josh": {
        "address": "22 Malcolm Road, London, SE25 5HG",
        "aiming_to_sell_for": GBP(475000),
        "buyer": josh,
        "comments": "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        "estate_agent_percentage": int(2),
        "expense_auction": GBP(1900),
        "expense_buy_property": GBP(354000),
        "expense_conveyancing_fee_buy": GBP(2500),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(50000),
        "url": "https://auctions.savills.co.uk/auctions/8-april-2025-185/22-malcolm-road-south-norwood-london-se25-5hg-15765",
    },
    "2025-09-01 Josh": {
        "address": "Somewhere near work, London, SW15 3SA",
        "buyer": josh2,
        "expense_auction": GBP(1900),
        "expense_buy_property": GBP(400000),
        "expense_conveyancing_fee_buy": GBP(2500),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(0),
    },
    "2025-09-02 Josh": {
        "address": "Somewhere near work, London, SW15 3SA",
        "buyer": josh,
        "comments": "£10,000 stamp duty paid by Charlie & Ians",
        "expense_auction": GBP(1900),
        "expense_buy_property": GBP(400000),
        "expense_conveyancing_fee_buy": GBP(2500),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(0),
    },
    "2025-04-16 Josh": {
        "address": "Flat A, 23 Airedale Road, Balham, London, SW12 8SQ",
        "aiming_to_sell_for": GBP(800000),
        "buyer": josh,
        "comments": "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        "estate_agent_percentage": int(2),
        "expense_auction": GBP(1750),
        "expense_buy_property": GBP(300000),
        "expense_conveyancing_fee_buy": GBP(3000),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(100000),
        "url": "https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250415-088",
    },
    "2025-05-22 Josh": {
        "aiming_to_sell_for": GBP(582000),
        "buyer": josh,
        "comments": "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        "estate_agent_percentage": int(2),
        "expense_buy_property": GBP(1.5 * 215000),
        "expense_conveyancing_fee_buy": GBP(3000),
        "expense_conveyancing_fee_sell": GBP(2500),
        "expense_insurance": GBP(400),
        "expense_renovation": GBP(100000),
        "lot": allsop_2025_05_22_34,
    },
}


def format(value):
    """
    Pretty print the value.
    """
    if isinstance(value, GBP):
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
    for k, v in developments[key].items():
        if k == "buyer_type":
            title = get_buyer_type_name(v)
            print(f"{k.replace('_', ' ').title()}: {title}")
        else:
            print(f"{k.replace('_', ' ').title()}: {format(v)}")
