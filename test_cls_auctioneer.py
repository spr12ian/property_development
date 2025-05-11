import cls_auctioneer
from cls_helper_auctioneer import AuctioneerHelper


def test_cls_auctioneer(auctioneer):
    print(auctioneer)
    assert auctioneer.buyers_fee.value == BUYERS_FEE
    assert auctioneer.name == NAME
    assert auctioneer.url == URL
    assert str(auctioneer) == auctioneer.name 
    assert auctioneer.buyers_fee == cls_auctioneer.GBP(2000)
    assert auctioneer.buyers_fee != cls_auctioneer.GBP(1000)


def test_cls_helper_auctioneer(auctioneer):
    auctioneer_helper = AuctioneerHelper(auctioneer)
    
    assert auctioneer_helper.get_auctioneer() == auctioneer
    assert auctioneer_helper.get_name() == NAME
    assert auctioneer_helper.get_buyers_fee() == cls_auctioneer.GBP(BUYERS_FEE)
    assert auctioneer_helper.get_url() == URL
    assert auctioneer_helper.get_website() == URL

BUYERS_FEE = 2000
NAME= "Allsop"
URL = "https://www.allsop.co.uk/"

auctioneer = cls_auctioneer.Auctioneer(
    buyers_fee=cls_auctioneer.GBP(BUYERS_FEE),
    name=NAME,
    url=URL,
)

test_cls_auctioneer(auctioneer)
test_cls_helper_auctioneer(auctioneer)
