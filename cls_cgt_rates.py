from cls_buyer_types import BuyerTypes
from decimal import Decimal

# https://www.gov.uk/stamp-duty-land-tax/residential-property-rates


CGT_Rates = {
    BuyerTypes.FIRST_TIME_BUYER: {
        "rates": {
            "band_1": {"upper_bound": Decimal(300000), "rate": int(0)},
            "band_2": {"upper_bound": Decimal(500000), "rate": int(5)},
        },
        "max_price": Decimal(500000),
    },
    BuyerTypes.NON_FIRST_TIME_BUYER: {
        "rates": {
            "band_1": {"upper_bound": Decimal(125000), "rate": int(0)},
            "band_2": {"upper_bound": Decimal(250000), "rate": int(2)},
            "band_3": {"upper_bound": Decimal(925000), "rate": int(5)},
            "band_4": {"upper_bound": Decimal(1500000), "rate": int(10)},
            "band_5": {"upper_bound": Decimal(9999999), "rate": int(12)},
        },
    },
    BuyerTypes.SECOND_HOME_BUYER: {
        "rates": {
            "band_1": {"upper_bound": Decimal(125000), "rate": int(5)},
            "band_2": {"upper_bound": Decimal(250000), "rate": int(7)},
            "band_3": {"upper_bound": Decimal(925000), "rate": int(10)},
            "band_4": {"upper_bound": Decimal(1500000), "rate": int(12)},
            "band_5": {"upper_bound": Decimal(9999999), "rate": int(17)},
        },
    },
    BuyerTypes.LIMITED_COMPANY: {
        "rates": {
            "band_1": {"upper_bound": Decimal(125000), "rate": int(5)},
            "band_2": {"upper_bound": Decimal(250000), "rate": int(7)},
            "band_3": {"upper_bound": Decimal(925000), "rate": int(10)},
            "band_4": {"upper_bound": Decimal(1500000), "rate": int(12)},
            "band_5": {"upper_bound": Decimal(9999999), "rate": int(17)},
        },
        "zero_due_price": Decimal(40000),
    },
}

cgt_allowance=Decimal(3000)
