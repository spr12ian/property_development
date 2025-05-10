from auctioneers import auctioneers

class AuctioneerHelper:
    def __init__(self, auctioneer):
        self.auctioneer = auctioneer

    def get_auctioneer(self):
        return self.auctioneer
    def get_auctioneer_name(self):
        return self.auctioneer["name"]
    def get_auctioneer_url(self):
        return self.auctioneer.get_url()
    def get_auctioneer_website(self):
        return self.auctioneer.get_website()
    def get_auctioneer_email(self):
        return self.auctioneer.get_email()
    def get_auctioneer_phone(self):
        return self.auctioneer.get_phone()
    def get_buyers_fee(self):
        return self.auctioneer["buyers_fee"]
    
