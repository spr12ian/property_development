from cls_auction import Auction
from auctioneers import allsop, savills
from datetime import date

allsop_2025_05_22 = Auction(allsop, date(2025, 5, 22))
savills_2025_05_22 = Auction(savills, auction_date=date(2023, 10, 1))

auctions: dict[str, Auction] = {
    "2025-05-22 allsop": allsop_2025_05_22,
    "2025-05-22 savills": savills_2025_05_22,
}
