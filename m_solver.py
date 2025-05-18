from cls_buyer_types import BuyerTypes
from cls_gbp import GBP
from cls_percentage import Percentage
from cls_sdlt_calculator import SDLT_Calculator
from scipy.optimize import fsolve


# Example cost functions
def convey_buy(p: GBP) -> GBP:
    return GBP(3000)


def convey_sell(p: GBP) -> GBP:
    return GBP(2500)


def insurance(p: GBP) -> GBP:
    return GBP(400)


def renovation(p: GBP) -> GBP:
    return GBP(50000)


def stamp_duty(p: GBP) -> GBP:
    sdlt_calculator = SDLT_Calculator()
    return sdlt_calculator.calculate_sdlt(BuyerTypes.FIRST_TIME_BUYER, p)


def estate_agent_fee(t: GBP) -> GBP:
    return Percentage(2).of(t)  # 2%


# Wrapper function returning float for fsolve
def total_cost_eq_float(p_array, min_profit: GBP) -> float:
    p_scalar = float(p_array[0])  # Extract the float from the array
    p = GBP(p_scalar)
    a = convey_buy(p)
    b = convey_sell(p)
    c_ = insurance(p)
    d = renovation(p)
    e = stamp_duty(p)
    t = (p + a + b + c_ + d + e + min_profit) / 0.985
    f = estate_agent_fee(t)
    result = p + a + b + c_ + d + e + f + min_profit - t
    return float(result)  # Convert GBP to float



# Solve for p
min_profit = GBP(60000)
p_guess = 250000.0
result = fsolve(lambda p: total_cost_eq_float(p, min_profit), [p_guess])

# Convert result to GBP
max_bid_price = GBP(result[0])
print(f"Maximum bid price p: {max_bid_price}")
