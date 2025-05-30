from cls_buyers import Buyers
from cls_development import Development
from cls_expense import Expense
from cls_development_stages import DevelopmentStages
from cls_expense_types import ExpenseTypes
from cls_gbp import GBP
from cls_percentage import Percentage
from d_dwellings import dwellings


developments = {
    "2021-05-10 SW17 0SR": Development(
        aiming_to_sell_for=GBP(1100000),
        buyer=Buyers.CHARLIE,
        comments="Charlie paid 2nd home SDLT £36,200 and received a refund of £22,990.56",
        estate_agent_percentage=Percentage(2),
        expenses=(
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4),
            ),
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            Expense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400) * 4,
            ),
            Expense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(765000),
            ),
            Expense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(860600) - GBP(765000),
            ),
            Expense(
                expense_type=ExpenseTypes.STAMP_DUTY,
                cost=GBP(36200) - GBP(22990.56),
            ),
        ),
        dwelling=dwellings["SW17 0SR"],
        stage=DevelopmentStages.BOUGHT,
    ),
    # "2025-04-08 CB Property Development": Development(
    #     aiming_to_sell_for= GBP(480000),
    #     buyer= buyers["CB Developments"],
    #     expenses= [
    #         Expense(
    #             expense_type=ExpenseTypes.ACCOUNTANT,
    #             cost=GBP(12 * 89 * 1.2),
    #         ),
    #         Expense(
    #             expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
    #             cost=GBP(1500 + 300 + 275 + 55 + 36 + 220.1 + 540 + 14.4),
    #         ),
    #         Expense(
    #             expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
    #             cost=GBP(2500),
    #         ),
    #         Expense(
    #             expense_type=ExpenseTypes.INSURANCE,
    #             cost=GBP(400) * 4,
    #         ),
    #         Expense(
    #             expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
    #             cost=GBP(765000),
    #         ),
    #         Expense(
    #             expense_type=ExpenseTypes.RENOVATION_COST,
    #             cost=GBP(860600) - GBP(765000),
    #         ),
    #         Expense(
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
    "2025-05-22 SW8 3ST": Development(
        aiming_to_sell_for=GBP(582000),
        buyer=Buyers.JOSH,
        comments="Pay stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        estate_agent_percentage=Percentage(2),
        expenses=(
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(3000),
            ),
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            Expense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400),
            ),
            Expense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(1.8 * 215000),
            ),
            Expense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(100000),
            ),
            Expense(
                expense_type=ExpenseTypes.STAMP_DUTY,
                cost=GBP(36200) - GBP(22990.56),
            ),
        ),
        dwelling=dwellings["SW8 3ST"],
        stage=DevelopmentStages.CONSIDERED,
    ),
    "2025-05-22 SW17 7QW": Development(
        aiming_to_sell_for=GBP(582000),
        buyer=Buyers.JOSH,
        comments="Pay stamp duty cost when Josh buys his own place; to be deducted from the profit shown",
        estate_agent_percentage=Percentage(2),
        expenses=(
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(3000),
            ),
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            Expense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400),
            ),
            Expense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(360000),
            ),
            Expense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(100000),
            ),
            Expense(
                expense_type=ExpenseTypes.STAMP_DUTY,
                cost=GBP(36200) - GBP(22990.56),
            ),
        ),
        dwelling=dwellings["SW17 7QW"],
        stage=DevelopmentStages.CONSIDERED,
    ),
    "2025-05-28 SW19 1BS": Development(
        aiming_to_sell_for=GBP(582000),
        buyer=Buyers.CHARLIE,
        comments="Check stamp duty",
        estate_agent_percentage=Percentage(2),
        expenses=(
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_BUY,
                cost=GBP(3000),
            ),
            Expense(
                expense_type=ExpenseTypes.CONVEYANCING_FEE_SELL,
                cost=GBP(2500),
            ),
            Expense(
                expense_type=ExpenseTypes.INSURANCE,
                cost=GBP(400),
            ),
            Expense(
                expense_type=ExpenseTypes.PROPERTY_COST_PRICE,
                cost=GBP(450000),
            ),
            Expense(
                expense_type=ExpenseTypes.RENOVATION_COST,
                cost=GBP(50000),
            ),
        ),
        dwelling=dwellings["SW19 1BS"],
        stage=DevelopmentStages.UNDER_CONSIDERATION,
    ),
}
