from cls_buyer_types import BuyerTypes
from cls_sdlt_rates import SDLT_Rates
from decimal import Decimal

# https://www.tax.service.gov.uk/calculate-stamp-duty-land-tax/


class SDLT_Calculator:
    """
    A class to calculate Stamp Duty Land Tax (SDLT) for property purchases in the UK.
    """

    def __init__(self) -> None:
        pass

    def calculate_sdlt(self, buyer_type, property_price) -> Decimal:
        """
        Calculate the SDLT based on the property price.

        :param property_price: The price of the property
        :return: The amount of SDLT owed
        """
        if not isinstance(buyer_type, BuyerTypes):
            raise ValueError(f"Invalid buyer type: {buyer_type}")
        sdlt_rates = SDLT_Rates(buyer_type)
        rates = sdlt_rates.get_rates()
        if not rates:
            raise ValueError(f"No rates found for buyer type: {buyer_type}")
        if not isinstance(property_price, (int, float, Decimal)):
            raise ValueError(f"Invalid property price: {property_price}")
        if property_price < Decimal(250000):
            raise ValueError(f"Property price too low: {property_price}")
        
        if buyer_type is BuyerTypes.FIRST_TIME_BUYER:
            if property_price > sdlt_rates.get_max_price():
                # If the property price exceeds the max price for first-time buyers,
                # calculate SDLT as a non-first-time buyer
                return self.calculate_sdlt(
                    BuyerTypes.NON_FIRST_TIME_BUYER, property_price
                )

        if buyer_type is BuyerTypes.LIMITED_COMPANY:
            if property_price < sdlt_rates.get_zero_due_price():
                # If the property price is below the zero due price for limited companies,
                # SDLT is zero
                return Decimal(0)

        sdlt = Decimal(0)
        lower_bound = Decimal(0)

        # Sort bands by upper_bound (ascending order)
        sorted_bands = sorted(rates.values(), key=lambda x: x["upper_bound"])

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

    def print_calculations(self, price) -> None:
        """
        Print the SDLT calculations for the given price.

        :param price: The price of the property
        :return: The SDLT amount
        """
        print(f"Price: £{price:,}")
        for buyer_type in BuyerTypes:
            title = buyer_type
            sdlt = self.calculate_sdlt(buyer_type, price)
            print(f"SDLT: £{sdlt:>10,.2f} for a {title}")
