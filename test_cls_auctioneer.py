import cls_auctioneer


def test_cls_auctioneer():
    # Test Auctioneer class
    auctioneer = cls_auctioneer.Auctioneer(
        buyers_fee=cls_auctioneer.GBP(2000), name="Allsops"
    )
    print(auctioneer)
    assert auctioneer.buyers_fee.value == 2000
    assert auctioneer.name == "Allsops"
    # assert str(auctioneer) == "Allsops"
    assert auctioneer.buyers_fee == cls_auctioneer.GBP(2000)
    assert auctioneer.buyers_fee != cls_auctioneer.GBP(1000)

test_cls_auctioneer()