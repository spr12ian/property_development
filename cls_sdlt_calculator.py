from cls_buyer_types import BuyerTypes
from d_sdlt_rates import sdlt_rates
from cls_gbp import GBP


class SDLT_Calculator:
    """
    A class to calculate Stamp Duty Land Tax (SDLT) for property purchases in the UK.
    """

    def __init__(self) -> None:
        pass

    def calculate_sdlt(self, buyer_type: BuyerTypes, property_price: GBP) -> GBP:
        if not isinstance(buyer_type, BuyerTypes):
            raise ValueError(f"Invalid buyer type: {buyer_type}")
        if not isinstance(property_price, GBP):
            raise ValueError(f"Invalid property price: {property_price}")

        rates = sdlt_rates.get(buyer_type.label)
        if not rates:
            raise ValueError(f"No rates found for buyer type: {buyer_type.label}")

        if buyer_type == BuyerTypes.FIRST_TIME_BUYER:
            if rates.max_price and property_price > rates.max_price:
                # Use standard rate instead
                return self.calculate_sdlt(BuyerTypes.NON_FIRST_TIME_BUYER, property_price)

        if buyer_type == BuyerTypes.LIMITED_COMPANY:
            if rates.zero_due_price and property_price < rates.zero_due_price:
                return GBP(0)

        sdlt = GBP(0)
        lower_bound = GBP(0)

        for band in rates.bands:
            upper_bound = band.upper_bound
            if property_price > lower_bound:
                taxable_amount = min(property_price, upper_bound) - lower_bound
                sdlt += band.rate.of(taxable_amount)
            lower_bound = upper_bound

        return sdlt

    def print_calculations(self, price: GBP) -> None:
        print(f"Price: {price}")
        for buyer_type in BuyerTypes:
            try:
                sdlt = self.calculate_sdlt(buyer_type, price)
                print(f"SDLT: {sdlt} for a {buyer_type.label}")
            except ValueError as e:
                print(f"Error for {buyer_type.label}: {e}")
