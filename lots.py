from auctions import auctions
from cls_lot import Lot
from cls_gbp import GBP


lots: dict[str, Lot] = {
    "2025_05_22_allsop_34": Lot(
        auction=auctions["2025-05-22 allsop"],
        description="VACANT - Leasehold Self Contained Ground Floor Flat",
        guide_price=GBP(215000),
        lot_number=34,
        url="https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250521-091",
    ),
}
