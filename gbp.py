from decimal import Decimal

class GBP:
    """
    Helper class for GBP (Great British Pound) related operations.
    """

    def __init__(self, amount):
        """
        Initialize the GBP_Helper class.
        """
        self.amount = Decimal(amount)

    def __str__(self):
        """
        Return the string representation of the GBP amount.
        """
        return f"£{self.amount:,.2f}"

    def __add__(self, other):
        """
        Add another GBP object or a numeric value to this GBP object.
        :param other: The value to add.
        :return: A new GBP object with the result.
        """
        if isinstance(other, (int, float, Decimal)):
            return GBP(self.amount + Decimal(other))
        elif isinstance(other, GBP):
            return GBP(self.amount + other.amount)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'GBP' and '{type(other).__name__}'")

    def __sub__(self, other):
        """
        Subject another GBP object or a numeric value from this GBP object.
        :param other: The value to subtract.
        :return: A new GBP object with the result.
        """
        if isinstance(other, (int, float, Decimal)):
            return GBP(self.amount - Decimal(other))
        elif isinstance(other, GBP):
            return GBP(self.amount - other.amount)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'GBP' and '{type(other).__name__}'")

    @staticmethod
    def to_gbp(value):
        """
        Convert a value to GBP format.
        :param value: The value to convert.
        :return: The value formatted as GBP.
        """
        return f"£{value:,.2f}" if isinstance(value, Decimal) else f"£{value:.2f}"
    

    @staticmethod
    def from_gbp(value):
        """
        Convert a GBP formatted string to a Decimal.
        :param value: The GBP formatted string.
        :return: The value as a Decimal.
        """
        return Decimal(value.replace("£", "").replace(",", ""))
    

a = GBP(1000)
print(a)
b = a - 4
print(b)