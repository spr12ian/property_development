from cls_auctioneer import Auctioneer
from gbp import GBP


allsop = Auctioneer(
    buyers_fee=GBP(2000),
    name="Allsops",
)
savills = Auctioneer(
    buyers_fee=GBP(1750),
    name="Savills",
)


auctioneers: dict[str, Auctioneer] = {
    "allsop": allsop,
    "savills": savills,
}
