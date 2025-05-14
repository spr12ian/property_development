from buyers import buyers
from cls_development import Development
from cls_development_expense import DevelopmentExpense
from cls_expense_types import ExpenseTypes
from decimal import Decimal
from cls_gbp import GBP
from cls_percentage import Percentage
from dwellings import dwellings


developments = {
    "2021-05-10 Charlie": Development(
        aiming_to_sell_for=GBP(1100000),
        buyer=buyers["Charlie"],
        comments="Charlie paid 2nd home SDLT £36,200 and received a refund of £22,990.56",
        estate_agent_percentage=Percentage(2),
        expenses=(
            DevelopmentExpense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400) * 4,
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(765000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(860600) - GBP(765000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.STAMP_DUTY,
                cost=GBP(36200) - GBP(22990.56),
            ),
        ),
        dwelling=dwellings["SW17 0SR"],
    ),
    # "2025-04-08 CB Property Development": Development(
    #     aiming_to_sell_for= GBP(480000),
    #     buyer= buyers["CB Developments"],
    #     expenses= [
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.ACCOUNTANT,
    #             cost=GBP(12 * 89 * 1.2),
    #         ),
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
    #             cost=GBP(1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4),
    #         ),
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
    #             cost=GBP(2500),
    #         ),
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.INSURANCE,
    #             cost=GBP(400) * 4,
    #         ),
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
    #             cost=GBP(765000),
    #         ),
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.RENOVATION_COST,
    #             cost=GBP(860600) - GBP(765000),
    #         ),
    #         DevelopmentExpense(
    #             expense_type=ExpenseTypes.STAMP_DUTY,
    #             cost=GBP(36200) - GBP(22990.56),
    #         ),
    #     ],
    #     expense_auction= GBP(1900),
    #     expense_buy_property= GBP(354000),
    #     expense_conveyancing_fee_buy= GBP(2500),
    #     expense_conveyancing_fee_sell= GBP(2500),
    #     expense_insurance= GBP(400),
    #     expense_renovation= GBP(50000),
    #     property= dwellings["SE5 5HG"], # "22 Malcolm Road, London, SE25 5HG",
    # ),
    # "2025-04-08 Ian B & Ian S": Development(
    #     aiming_to_sell_for= GBP(480000),
    #     buyer= buyers["Charlie"],
    #     expense_auction= GBP(1900),
    #     expense_buy_property= GBP(354000),
    #     expense_conveyancing_fee_buy= GBP(2500),
    #     expense_conveyancing_fee_sell= GBP(2500),
    #     expense_insurance= GBP(400),
    #     expense_renovation= GBP(50000),
    #     property= dwellings["SE5 5HG"], # "22 Malcolm Road, London, SE25 5HG",
    # ),
    # "2025-04-08 Josh": Development(
    #     aiming_to_sell_for= GBP(475000),
    #     buyer= buyers["Josh"],
    #     comments= "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
    #     estate_agent_percentage= int(2),
    #     expense_auction= GBP(1900),
    #     expense_buy_property= GBP(354000),
    #     expense_conveyancing_fee_buy= GBP(2500),
    #     expense_conveyancing_fee_sell= GBP(2500),
    #     expense_insurance= GBP(400),
    #     expense_renovation= GBP(50000),
    #     property= dwellings["SE5 5HG"], # "22 Malcolm Road, London, SE25 5HG",
    #     url= "https://auctions.savills.co.uk/auctions/8-april-2025-185/22-malcolm-road-south-norwood-london-se25-5hg-15765",
    # ),
    # "2025-09-01 Josh": Development(
    #     buyer= buyers["Josh (his own property)"],
    #     expense_auction= GBP(1900),
    #     expense_buy_property= GBP(400000),
    #     expense_conveyancing_fee_buy= GBP(2500),
    #     expense_conveyancing_fee_sell= GBP(2500),
    #     expense_insurance= GBP(400),
    #     expense_renovation= GBP(0),
    #     property= dwellings["SW15 3SA"], # "Somewhere near work, London, SW15 3SA",
    # ),
    # "2025-09-02 Josh": Development(
    #     buyer= buyers["Josh"],
    #     comments= "£10,000 stamp duty paid by Charlie & Ians",
    #     expense_auction= GBP(1900),
    #     expense_buy_property= GBP(400000),
    #     expense_conveyancing_fee_buy= GBP(2500),
    #     expense_conveyancing_fee_sell= GBP(2500),
    #     expense_insurance= GBP(400),
    #     expense_renovation= GBP(0),
    #     property= dwellings["SW15 3SA"], # "Somewhere near work, London, SW15 3SA",
    # ),
    # "2025-04-16 Josh": Development(
    #     aiming_to_sell_for= GBP(800000),
    #     buyer= buyers["Josh"],
    #     comments= "Pay £10,000 stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
    #     estate_agent_percentage= int(2),
    #     expense_auction= GBP(1750),
    #     expense_buy_property= GBP(300000),
    #     expense_conveyancing_fee_buy= GBP(3000),
    #     expense_conveyancing_fee_sell= GBP(2500),
    #     expense_insurance= GBP(400),
    #     expense_renovation= GBP(100000),
    #     property= dwellings["SW12 8SQ"], # "Flat A, 23 Airedale Road, Balham, London, SW12 8SQ"
    #     url= "https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250415-088",
    # ),
    "2025-05-22 Josh": Development(
        aiming_to_sell_for=GBP(582000),
        buyer=buyers["Josh"],
        comments="Pay stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        estate_agent_percentage=Percentage(2),
        expenses=(
            DevelopmentExpense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(3000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(1.8 * 215000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(100000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.STAMP_DUTY,
                cost=GBP(36200) - GBP(22990.56),
            ),
        ),
        dwelling=dwellings["SW8 3ST"],
    ),
    "2025-05-28 Charlie": Development(
        aiming_to_sell_for=GBP(582000),
        buyer=buyers["Charlie"],
        comments="Check stamp duty",
        estate_agent_percentage=Percentage(2),
        expenses=(
            DevelopmentExpense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(3000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(450000),
            ),
            DevelopmentExpense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(50000),
            ),
        ),
        dwelling=dwellings["SW19 1BS"],
    ),
}


def format(value):
    """
    Pretty print the value.
    """
    if isinstance(value, GBP):
        return f"£{value:,.2f}"
    elif isinstance(value, Percentage):
        return f"{value}%"
    elif isinstance(value, str):
        return value
    else:
        return value
