from decimal import Decimal

class GBP:
    """
    Helper class for GBP (Great British Pound) related operations.
    """

    def __init__(self, value):
        """
        Initialize the GBP_Helper class.
        """
        self.value = Decimal(value)

    def __str__(self):
        """
        Return the string representation of the GBP value.
        """
        return f"£{self.value:,.2f}"

    def __add__(self, other):
        """
        Add another GBP object or a numeric value to this GBP object.
        :param other: The value to add.
        :return: A new GBP object with the result.
        """
        if isinstance(other, (int, float, Decimal)):
            return GBP(self.value + Decimal(other))
        elif isinstance(other, GBP):
            return GBP(self.value + other.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'GBP' and '{type(other).__name__}'")

    def __sub__(self, other):
        """
        Subject another GBP object or a numeric value from this GBP object.
        :param other: The value to subtract.
        :return: A new GBP object with the result.
        """
        if isinstance(other, (int, float, Decimal)):
            return GBP(self.value - Decimal(other))
        elif isinstance(other, GBP):
            return GBP(self.value - other.value)
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
    

    def __mul__(self, other):
        """
        Multiply this GBP object by a numeric value.
        :param other: The value to multiply by.
        :return: A new GBP object with the result.
        """
        if isinstance(other, (int, float, Decimal)):
            return GBP(self.value * Decimal(other))
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'GBP' and '{type(other).__name__}'")
    def __truediv__(self, other):
        """
        Divide this GBP object by a numeric value.
        :param other: The value to divide by.
        :return: A new GBP object with the result.
        """
        if isinstance(other, (int, float, Decimal)):
            return GBP(self.value / Decimal(other))
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'GBP' and '{type(other).__name__}'")
    def __lt__(self, other):
        """
        Compare this GBP object with another GBP object or a numeric value.
        :param other: The value to compare with.
        :return: True if this GBP object is less than the other, False otherwise.
        """
        if isinstance(other, (int, float, Decimal)):
            return self.value < Decimal(other)
        elif isinstance(other, GBP):
            return self.value < other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for <: 'GBP' and '{type(other).__name__}'")
    def __le__(self, other):
        """
        Compare this GBP object with another GBP object or a numeric value.
        :param other: The value to compare with.
        :return: True if this GBP object is less than or equal to the other, False otherwise.
        """
        if isinstance(other, (int, float, Decimal)):
            return self.value <= Decimal(other)
        elif isinstance(other, GBP):
            return self.value <= other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for <=: 'GBP' and '{type(other).__name__}'")
    def __gt__(self, other):
        """
        Compare this GBP object with another GBP object or a numeric value.
        :param other: The value to compare with.
        :return: True if this GBP object is greater than the other, False otherwise.
        """
        if isinstance(other, (int, float, Decimal)):
            return self.value > Decimal(other)
        elif isinstance(other, GBP):
            return self.value > other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for >: 'GBP' and '{type(other).__name__}'")
    def __ge__(self, other):
        """
        Compare this GBP object with another GBP object or a numeric value.
        :param other: The value to compare with.
        :return: True if this GBP object is greater than or equal to the other, False otherwise.
        """
        if isinstance(other, (int, float, Decimal)):
            return self.value >= Decimal(other)
        elif isinstance(other, GBP):
            return self.value >= other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for >=: 'GBP' and '{type(other).__name__}'")
    def __eq__(self, other):
        """
        Compare this GBP object with another GBP object or a numeric value.
        :param other: The value to compare with.
        :return: True if this GBP object is equal to the other, False otherwise.
        """
        if isinstance(other, (int, float, Decimal)):
            return self.value == Decimal(other)
        elif isinstance(other, GBP):
            return self.value == other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for ==: 'GBP' and '{type(other).__name__}'")
    def __ne__(self, other):
        """
        Compare this GBP object with another GBP object or a numeric value.
        :param other: The value to compare with.
        :return: True if this GBP object is not equal to the other, False otherwise.
        """
        if isinstance(other, (int, float, Decimal)):
            return self.value != Decimal(other)
        elif isinstance(other, GBP):
            return self.value != other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for !=: 'GBP' and '{type(other).__name__}'")
    def __hash__(self):
        """
        Return the hash of the GBP object.
        :return: The hash of the GBP value.
        """
        return hash(self.value)
    def __repr__(self):
        """
        Return the string representation of the GBP object.
        :return: The string representation of the GBP value.
        """
        return f"GBP({self.value})"
    def __bool__(self):
        """
        Return True if the GBP object is not zero, False otherwise.
        :return: True if the GBP value is not zero, False otherwise.
        """
        return self.value != 0
    def __int__(self):
        """
        Return the integer value of the GBP object.
        :return: The integer value of the GBP.
        """
        return int(self.value)
    def __float__(self):
        """
        Return the float value of the GBP object.
        :return: The float value of the GBP.
        """
        return float(self.value)
    def __round__(self, n=0):
        """
        Round the GBP value to the nearest integer.
        :param n: The number of decimal places to round to.
        :return: The rounded GBP value.
        """
        return round(self.value, n)
    def __format__(self, format_spec):
        """
        Format the GBP value according to the given format specification.
        :param format_spec: The format specification.
        :return: The formatted GBP value.
        """
        return format(self.value, format_spec)