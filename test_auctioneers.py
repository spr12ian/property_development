import d_auctioneers

class TestAuctioneerHelper:
    def test_get_auctioneer(self):
        auctioneer = d_auctioneers.auctioneers["allsop"]
        auctioneer_helper = d_auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer() == auctioneer

    def test_get_auctioneer_name(self):
        auctioneer = d_auctioneers.auctioneers["allsop"]
        auctioneer_helper = d_auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer_name() == "Allsops"

    def test_get_auctioneer_url(self):
        auctioneer = d_auctioneers.auctioneers["allsop"]
        auctioneer_helper = d_auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer_url() == "https://www.allsop.co.uk/"

    def test_get_auctioneer_website(self):
        auctioneer = d_auctioneers.auctioneers["allsop"]
        auctioneer_helper = d_auctioneers.AuctioneerHelper(auctioneer)
        assert auctioneer_helper.get_auctioneer_website() == "https://www.allsop.co.uk/"

for auctioneer in d_auctioneers:
    auctioneer_helper = AuctioneerHelper(auctioneer)
    print(f"Auctioneer: {auctioneer_helper.get_auctioneer_name()}")
    print(f"Buyers fee: {auctioneer_helper.get_buyers_fee()}")