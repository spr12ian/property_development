from enum import Enum, auto


class SDLT_BuyerTypes(Enum):
    FIRST_TIME_BUYER = auto()
    NON_FIRST_TIME_BUYER = auto()
    SECOND_HOME_BUYER = auto()
    CORPORATE_BUYER = auto()


class SDLTCalculator:
    SDLT_Rates = {
        SDLT_BuyerTypes.FIRST_TIME_BUYER: {
            "rates": {
                "band_1": {"limit": 300000, "rate": 0},
                "band_2": {"limit": 500000, "rate": 5},
            },
        },
        SDLT_BuyerTypes.NON_FIRST_TIME_BUYER: {
            "rates": {
                "band_1": {"limit": 125000, "rate": 0},
                "band_2": {"limit": 250000, "rate": 2},
                "band_3": {"limit": 925000, "rate": 5},
                "band_4": {"limit": 1500000, "rate": 10},
                "band_5": {"limit": 50000000, "rate": 12},
            },
        },
        SDLT_BuyerTypes.SECOND_HOME_BUYER: {
            "rates": {
                "band_1": {"limit": 125000, "rate": 5},
                "band_2": {"limit": 250000, "rate": 7},
                "band_3": {"limit": 925000, "rate": 10},
                "band_4": {"limit": 1500000, "rate": 15},
                "band_5": {"limit": 50000000, "rate": 17},
            },
        },
        SDLT_BuyerTypes.CORPORATE_BUYER: {
            "rates": {
                "band_1": {"limit": 125000, "rate": 0},
                "band_2": {"limit": 250000, "rate": 2},
                "band_3": {"limit": 925000, "rate": 5},
                "band_4": {"limit": 1500000, "rate": 10},
                "band_5": {"limit": 50000000, "rate": 12},
            },
        },
    }
    """
    A class to calculate Stamp Duty Land Tax (SDLT) for property purchases in the UK.
    """

    def __init__(self, buyer_type=SDLT_BuyerTypes.NON_FIRST_TIME_BUYER):
        self.buyer_type = buyer_type

    def calculate_sdlt(self, property_price):
        """
        Calculate the SDLT based on the property price.

        :param property_price: The price of the property
        :return: The amount of SDLT owed
        """
        sdlt = 0
        rates = self.SDLT_Rates[self.buyer_type]["rates"]
        rates = dict(reversed(rates.items()))
        for rate_details in rates.items():
            band = rate_details[1]
            limit = band["limit"]
            if property_price > limit:
                slice = property_price - limit
                print(f"slice: {slice}")
                print(f"Band limit: {band['limit']}")
                print(f"Band rate: {band['rate']}")
                rate = band["rate"]
                sdlt += slice * (rate / 100)
                print(f"SDLT so far: {sdlt}")
                property_price = limit

        return sdlt

    def set_price(self, price):
        """
        Set the property price.

        :param price: The price of the property
        """
        self.price = price

    def get_price(self):
        """
        Get the property price.
        :return: The price of the property
        """
        return self.price

    def print_calculations(self, price):
        """
        Print the SDLT calculations for the given price.

        :param price: The price of the property
        :return: The SDLT amount
        """
        for buyer_type in SDLT_BuyerTypes:
            print(f"Calculating SDLT for {buyer_type.name.replace('_', ' ').title()}")
            self.buyer_type = buyer_type
            self.set_price(price)
            sdlt = self.calculate_sdlt(price)
            print(f"SDLT for a property worth £{price:,}: £{sdlt:,.2f}")


# Example usage
price = 280000
sdlt_calculator = SDLTCalculator()
sdlt = sdlt_calculator.print_calculations(price)
