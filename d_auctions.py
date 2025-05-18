from cls_auction import Auction
from d_auctioneers import auctioneers
from datetime import date

auctions: dict[str, Auction] = {
    "2025-04-08 savills": Auction(auctioneer=auctioneers["savills"], auction_date=date(2025, 4, 8)),
    "2025-05-22 allsop": Auction(auctioneer=auctioneers["allsop"], auction_date=date(2025, 5, 22)),
    "2025-05-28 savills": Auction(auctioneer=auctioneers["savills"], auction_date=date(2025, 5, 28)),
}
