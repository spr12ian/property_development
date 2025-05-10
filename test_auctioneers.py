import auctioneers

class TestAuctioneerHelper:
    def test_get_auctioneer(self):
        auctioneer = auctioneers.auctioneers["allsop"]
        auctioneer_helper = auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer() == auctioneer

    def test_get_auctioneer_name(self):
        auctioneer = auctioneers.auctioneers["allsop"]
        auctioneer_helper = auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer_name() == "Allsops"

    def test_get_auctioneer_url(self):
        auctioneer = auctioneers.auctioneers["allsop"]
        auctioneer_helper = auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer_url() == "https://www.allsop.co.uk/"

    def test_get_auctioneer_website(self):
        auctioneer = auctioneers.auctioneers["allsop"]
        auctioneer_helper = auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer_website() == "https://www.allsop.co.uk/"

for auctioneer in auctioneers:
    auctioneer_helper = AuctioneerHelper(auctioneer)
    print(f"Auctioneer: {auctioneer_helper.get_auctioneer_name()}")
    print(f"Buyers fee: {auctioneer_helper.get_buyers_fee()}")