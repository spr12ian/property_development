from cls_buyer_types import BuyerTypes
from cls_cgt_rates import CGT_Rates
from decimal import Decimal

# https://www.tax.service.gov.uk/calculate-stamp-duty-land-tax/


class CGT_Calculator:
    """
    A class to calculate Stamp Duty Land Tax (SDLT) for property purchases in the UK.
    """

    def __init__(self, buyer_type=BuyerTypes.NON_FIRST_TIME_BUYER):
        self.buyer_type = buyer_type

    def calculate_sdlt(self, buyer_type, property_price):
        """
        Calculate the SDLT based on the property price.

        :param property_price: The price of the property
        :return: The amount of SDLT owed
        """

        if buyer_type is BuyerTypes.FIRST_TIME_BUYER:
            if property_price > SDLT_Rates[buyer_type]["max_price"]:
                return self.calculate_sdlt(
                    BuyerTypes.NON_FIRST_TIME_BUYER, property_price
                )

        if buyer_type is BuyerTypes.LIMITED_COMPANY:
            if property_price < SDLT_Rates[buyer_type]["zero_due_price"]:
                return 0

        sdlt = 0
        lower_bound = 0
        rates = SDLT_Rates[buyer_type]["rates"]

        # Sort bands by upper_bound (ascending order)
        sorted_bands = sorted(rates.values(), key=lambda x: x["upper_bound"])
        # breakpoint()

        for band in sorted_bands:
            upper_bound = band["upper_bound"]
            rate = band["rate"]
            if property_price > lower_bound:
                # Calculate the taxable amount for this band
                # Ensure we don't go above the property price
                if property_price < upper_bound:
                    upper_bound = property_price
                taxable_amount = upper_bound - lower_bound
                sdlt_due = taxable_amount * (Decimal(rate) / Decimal(100))
                sdlt += sdlt_due
            lower_bound = upper_bound

        return sdlt

    def print_calculations(self, price):
        """
        Print the SDLT calculations for the given price.

        :param price: The price of the property
        :return: The SDLT amount
        """
        print(f"Price: £{price:,}")
        for buyer_type in BuyerTypes:
            title = get_buyer_type_name(buyer_type)
            sdlt = self.calculate_sdlt(buyer_type, price)
            print(f"SDLT: £{sdlt:>10,.2f} for a {title}")

    def print_rates(self):
        for buyer_type in BuyerTypes:
            print(f"\n" + "=" * 40)
            title = f"{buyer_type.name.replace('_', ' ').title()}"
            rates = SDLT_Rates[buyer_type]["rates"]
            sorted_bands = sorted(rates.items(), key=lambda x: x[1]["upper_bound"])
            last_band_index = len(sorted_bands) - 1

            for i, (band, details) in enumerate(sorted_bands):
                # Get the details for the current band
                upper_bound = details["upper_bound"]
                rate = details["rate"]

                if i == 0:
                    print(f"{title} {band}: up to £{upper_bound:,} at {rate}%")
                elif i == last_band_index:
                    print(
                        f"{title} {band}: above £{sorted_bands[i-1][1]['upper_bound']:,} at {rate}% (last band)"
                    )
                    if buyer_type is BuyerTypes.FIRST_TIME_BUYER:
                        max_price = SDLT_Rates[buyer_type]["max_price"]
                        print(
                            f"{title} rates only apply for dwellings up tp £{max_price:,}"
                        )
                else:
                    print(f"{title} {band}: then up to £{upper_bound:,} at {rate}%")

        print("\n" + "=" * 40)
        print(
            "Note: SDLT rates are subject to change. Always check the latest government guidelines."
        )
        print("=" * 40)
