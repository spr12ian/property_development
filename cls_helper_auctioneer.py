from cls_auctioneer import Auctioneer

class AuctioneerHelper:
    def __init__(self, auctioneer:Auctioneer):
        self.auctioneer = auctioneer

    def get_auctioneer(self):
        return self.auctioneer
    def get_name(self):
        return self.auctioneer.name
    def get_buyers_fee(self):
        return self.auctioneer.buyers_fee
    def get_url(self):
        return self.auctioneer.url
    def get_website(self):
        return self.get_url()
    
