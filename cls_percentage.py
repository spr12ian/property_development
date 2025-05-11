from decimal import Decimal

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