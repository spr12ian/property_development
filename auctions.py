from cls_auction import Auction
from auctioneers import auctioneers
from datetime import date

auctions: dict[str, Auction] = {
    "2025-05-22 allsop": Auction(auctioneer=auctioneers["allsop"], auction_date=date(2025, 5, 22)),
}
