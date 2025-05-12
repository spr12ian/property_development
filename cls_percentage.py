from decimal import Decimal
from cls_gbp import GBP

class Percentage:
    """
    Helper class for percentage related operations.
    """

    def __init__(self, value):
        """
        Initialize the percentage class.
        """
        self.value = Decimal(value)

    def __str__(self):
        """
        Return the string representation of the percentage value.
        """
        return f"{self.value:,.2f}%"
    
    def of(self, gbp: GBP) -> GBP:
        return GBP(gbp.amount * (self.value / 100))