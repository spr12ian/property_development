from cls_buyer_types import BuyerTypes
from decimal import Decimal
from enum import Enum


class SDLT_Rates:
    constants = {
        BuyerTypes.FIRST_TIME_BUYER: {
            "rates": {
                "band_1": {"upper_bound": Decimal(300000), "rate": 0},
                "band_2": {"upper_bound": Decimal(500000), "rate": 5},
            },
            "max_price": Decimal(500000),
        },
        BuyerTypes.NON_FIRST_TIME_BUYER: {
            "rates": {
                "band_1": {"upper_bound": Decimal(125000), "rate": 0},
                "band_2": {"upper_bound": Decimal(250000), "rate": 2},
                "band_3": {"upper_bound": Decimal(925000), "rate": 5},
                "band_4": {"upper_bound": Decimal(1500000), "rate": 10},
                "band_5": {"upper_bound": Decimal(9999999), "rate": 12},
            },
        },
        BuyerTypes.SECOND_HOME_BUYER: {
            "rates": {
                "band_1": {"upper_bound": Decimal(125000), "rate": 5},
                "band_2": {"upper_bound": Decimal(250000), "rate": 7},
                "band_3": {"upper_bound": Decimal(925000), "rate": 10},
                "band_4": {"upper_bound": Decimal(1500000), "rate": 12},
                "band_5": {"upper_bound": Decimal(9999999), "rate": 17},
            },
        },
        BuyerTypes.LIMITED_COMPANY: {
            "rates": {
                "band_1": {"upper_bound": Decimal(125000), "rate": 5},
                "band_2": {"upper_bound": Decimal(250000), "rate": 7},
                "band_3": {"upper_bound": Decimal(925000), "rate": 10},
                "band_4": {"upper_bound": Decimal(1500000), "rate": 12},
                "band_5": {"upper_bound": Decimal(9999999), "rate": 17},
            },
            "zero_due_price": Decimal(40000),
        },
    }

    def __init__(self, buyer_type: Enum) -> None:
        if not isinstance(buyer_type, BuyerTypes):
            raise ValueError(f"Invalid buyer type: {buyer_type}")

        buyer_data = self.constants.get(buyer_type, {})
        self.buyer_type = buyer_type
        self.rates = buyer_data.get("rates", {})
        self.max_price = buyer_data.get("max_price")  # Might be None
        self.zero_due_price = buyer_data.get("zero_due_price")  # Might be None

    def get_rates(self):
        return self.rates

    def get_max_price(self):
        return self.max_price

    def get_zero_due_price(self):
        return self.zero_due_price

    def get_buyer_type(self):
        return self.buyer_type

    def get_buyer_type_name(self):
        return self.buyer_type.name.replace("_", " ").title()

    @staticmethod
    def print_rates():
        print("SDLT Rates:")
        for buyer_type in BuyerTypes:
            if buyer_type not in SDLT_Rates.constants:
                continue

            print("\n" + "=" * 40)
            title = buyer_type.name.replace("_", " ").title()
            rates = SDLT_Rates.constants[buyer_type]["rates"]
            sorted_bands = sorted(rates.items(), key=lambda x: x[1]["upper_bound"])
            last_band_index = len(sorted_bands) - 1

            for i, (band, details) in enumerate(sorted_bands):
                upper_bound = details["upper_bound"]
                rate = details["rate"]

                if i == 0:
                    print(f"{title} {band}: up to £{upper_bound:,} at {rate}%")
                elif i == last_band_index:
                    print(
                        f"{title} {band}: above £{sorted_bands[i-1][1]['upper_bound']:,} at {rate}% (last band)"
                    )
                    if buyer_type == BuyerTypes.FIRST_TIME_BUYER:
                        max_price = SDLT_Rates.constants[buyer_type]["max_price"]
                        print(
                            f"{title} rates only apply for dwellings up to £{max_price:,}"
                        )
                else:
                    print(f"{title} {band}: then up to £{upper_bound:,} at {rate}%")

        print("\n" + "=" * 40)
        print(
            "Note: SDLT rates are subject to change. Always check the latest government guidelines."
        )
        print("=" * 40)
