from dataclasses import dataclass
from decimal import Decimal
from typing import Union

Number = Union[int, float, Decimal, 'GBP']

@dataclass(frozen=True)
class GBP:
    amount: Number

    def __post_init__(self):
        # Ensure amount is always a Decimal
        object.__setattr__(self, 'amount', Decimal(self.amount))

    def __str__(self) -> str:
        return f"£{self.amount:,.2f}"

    def __repr__(self) -> str:
        return f"GBP({self.amount})"

    def __add__(self, other: Number) -> 'GBP':
        if isinstance(other, GBP):
            return GBP(self.amount + other.amount)
        return GBP(self.amount + Decimal(other))

    def __sub__(self, other: Number) -> 'GBP':
        if isinstance(other, GBP):
            return GBP(self.amount - other.amount)
        return GBP(self.amount - Decimal(other))

    def __mul__(self, other: Union[int, float, Decimal]) -> 'GBP':
        return GBP(self.amount * Decimal(other))

    def __truediv__(self, other: Union[int, float, Decimal]) -> 'GBP':
        return GBP(self.amount / Decimal(other))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, GBP):
            return self.amount == other.amount
        elif isinstance(other, (int, float, Decimal)):
            return self.amount == Decimal(other)
        return NotImplemented

    def __lt__(self, other: Number) -> bool:
        return self.amount < (other.amount if isinstance(other, GBP) else Decimal(other))

    def __le__(self, other: Number) -> bool:
        return self.amount <= (other.amount if isinstance(other, GBP) else Decimal(other))

    def __gt__(self, other: Number) -> bool:
        return self.amount > (other.amount if isinstance(other, GBP) else Decimal(other))

    def __ge__(self, other: Number) -> bool:
        return self.amount >= (other.amount if isinstance(other, GBP) else Decimal(other))

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __int__(self) -> int:
        return int(self.amount)

    def __float__(self) -> float:
        return float(self.amount)

    def __round__(self, n=0) -> Decimal:
        return round(self.amount, n)

    def __format__(self, format_spec: str) -> str:
        return format(self.amount, format_spec)

    def __bool__(self) -> bool:
        return self.amount != 0

    @staticmethod
    def to_gbp(amount: Decimal) -> str:
        return f"£{amount:,.2f}"

    @staticmethod
    def from_gbp(amount: str) -> 'GBP':
        return GBP(Decimal(amount.replace("£", "").replace(",", "")))
