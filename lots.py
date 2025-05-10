from auctions import allsop_2025_05_22
from cls_lot import Lot
from gbp import GBP


allsop_2025_05_22_34 = Lot(
    "11 Tennyson Street, Battersea, London",
    allsop_2025_05_22,
    "VACANT - Leasehold Self Contained Ground Floor Flat",
    GBP(215000),
    34,
    "SW8 3ST",
    "https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250521-091",
)


lots: dict[str, Lot] = {
    "allsop_2025_05_22_34": allsop_2025_05_22_34,
}
