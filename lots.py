from auctions import auctions
from cls_lot import Lot
from gbp import GBP
from properties import properties


lots: dict[str, Lot] = {
    "2025_05_22_allsop_34": Lot(
        auction=auctions["2025-05-22 allsop"],
        guide_price=GBP(215000),
        lot_number=34,
        property=properties["SW8_3ST"],
        url="https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250521-091",
    ),
}
