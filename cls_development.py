from cls_buyer import Buyer
from cls_lot import Lot
from cls_property import Property
from dataclasses import dataclass
from decimal import Decimal
from gbp import GBP


@dataclass(frozen=True)
class Development:
    aiming_to_sell_for: GBP
    buyer: Buyer
    comments: str
    estate_agent_percentage: Decimal
    expense_accountant: GBP
    expense_auction: GBP
    expense_buy_property: GBP
    expense_conveyancing_fee_buy: GBP
    expense_conveyancing_fee_sell: GBP
    expense_insurance: GBP
    expense_renovation: GBP
    expense_stamp_duty: GBP
    lot: Lot
    property: Property
