from d_auctions import auctions
from cls_lot import Lot
from cls_gbp import GBP


lots: dict[str, Lot] = {
    "2025_04_08_savills_46": Lot(
        auction=auctions["2025-04-08 savills"],
        description="A three bedroom terraced house, in need of modernisation. Benefitting from a rear garden. Well located for the amenities of Woodside Green and the centre of Croydon. Vacant.",
        guide_price=GBP(280000),
        hammer_price=GBP(345000),
        lot_number=46,
        url="https://auctions.savills.co.uk/auctions/8-april-2025-185/22-malcolm-road-south-norwood-london-se25-5hg-15765",
    ),
    "2025_05_22_allsop_34": Lot(
        auction=auctions["2025-05-22 allsop"],
        description="VACANT - Leasehold Self Contained Ground Floor Flat",
        guide_price=GBP(215000),
        lot_number=34,
        url="https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-ground-floor-flat-in-london/r250521-091",
    ),
    "2025_05_22_allsop_49": Lot(
        auction=auctions["2025-05-22 allsop"],
        description="VACANT - Leasehold Self Contained First Floor Flat",
        guide_price=GBP(295000),
        lot_number=49,
        url="https://www.allsop.co.uk/lot-overview/vacant-leasehold-self-contained-first-floor-flat-in-london/r250521-101?searchid=8sRMVfIgRoRo8pYpgeu7ms1vFL3BdUAmXxMZU5DOO3U%3D&idx=47",
    ),
    "2025_05_28_savills_597": Lot(
        auction=auctions["2025-05-28 savills"],
        description="Of interest to occupiers and investors. A long leasehold first floor self contained three bedroom maisonette with a private rear garden. Popular residential area. Vacant",
        guide_price=GBP(400000),
        lot_number=597,
        url="https://auctions.savills.co.uk/auctions/28-may-2025-188/32a-hotham-road-wimbledon-london-sw19-1bs-16739",
    ),
}
