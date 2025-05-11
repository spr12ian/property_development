from cls_auctioneer import Auctioneer
from cls_gbp import GBP


auctioneers: dict[str, Auctioneer] = {
    "allsop": Auctioneer(
        buyers_fee=GBP(2000),
        name="Allsop",
        url="https://www.allsop.co.uk/",
    ),
    "savills": Auctioneer(
        buyers_fee=GBP(1750),
        name="Savills",
        url="https://www.savills.co.uk/",
    ),
}
