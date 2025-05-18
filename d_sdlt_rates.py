from cls_buyer_types import BuyerTypes
from cls_gbp import GBP
from cls_percentage import Percentage
from cls_sdlt_band import SDLT_Band
from cls_sdlt_rate import SDLT_Rate
from enum import Enum

sdlt_rates: dict[str, SDLT_Rate] = {
    BuyerTypes.FIRST_TIME_BUYER.label: SDLT_Rate(
        bands=[
            SDLT_Band(
                label="Band 1",
                upper_bound=GBP(300000),
                rate=Percentage(0),
            ),
            SDLT_Band(
                label="Band 2",
                upper_bound=GBP(500000),
                rate=Percentage(5),
            ),
        ],
        max_price=GBP(500000),
    ),
    BuyerTypes.LIMITED_COMPANY.label: SDLT_Rate(
        bands=[
            SDLT_Band(
                label="Band 1",
                upper_bound=GBP(125000),
                rate=Percentage(5),
            ),
            SDLT_Band(
                label="Band 2",
                upper_bound=GBP(250000),
                rate=Percentage(5),
            ),
            SDLT_Band(
                label="Band 3",
                upper_bound=GBP(925000),
                rate=Percentage(10),
            ),
            SDLT_Band(
                label="Band 4",
                upper_bound=GBP(1500000),
                rate=Percentage(15),
            ),
            SDLT_Band(
                label="Band 5",
                upper_bound=GBP(9999999),
                rate=Percentage(17),
            ),
        ],
        zero_due_price=GBP(40000),
    ),
    BuyerTypes.NON_FIRST_TIME_BUYER.label: SDLT_Rate(
        bands=[
            SDLT_Band(
                label="Band 1",
                upper_bound=GBP(125000),
                rate=Percentage(0),
            ),
            SDLT_Band(
                label="Band 2",
                upper_bound=GBP(250000),
                rate=Percentage(2),
            ),
            SDLT_Band(
                label="Band 3",
                upper_bound=GBP(925000),
                rate=Percentage(5),
            ),
            SDLT_Band(
                label="Band 4",
                upper_bound=GBP(1500000),
                rate=Percentage(10),
            ),
            SDLT_Band(
                label="Band 5",
                upper_bound=GBP(9999999),
                rate=Percentage(12),
            ),
        ],
    ),
    BuyerTypes.SECOND_HOME_BUYER.label: SDLT_Rate(
        bands=[
            SDLT_Band(
                label="Band 1",
                upper_bound=GBP(125000),
                rate=Percentage(5),
            ),
            SDLT_Band(
                label="Band 2",
                upper_bound=GBP(250000),
                rate=Percentage(5),
            ),
            SDLT_Band(
                label="Band 3",
                upper_bound=GBP(925000),
                rate=Percentage(10),
            ),
            SDLT_Band(
                label="Band 4",
                upper_bound=GBP(1500000),
                rate=Percentage(15),
            ),
            SDLT_Band(
                label="Band 5",
                upper_bound=GBP(9999999),
                rate=Percentage(17),
            ),
        ],
    ),
}