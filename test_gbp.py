from cls_gbp import GBP

def test_gbp():
    # Test GBP class
    gbp = GBP(1000)
    assert gbp.value == 1000
    assert str(gbp) == "£1,000.00"
    
    # Test addition
    gbp2 = GBP(500)
    assert (gbp + gbp2).value == 1500
    
    # Test subtraction
    assert (gbp - gbp2).value == 500
    
    # Test multiplication
    assert (gbp * 2).value == 2000
    
    # Test division
    assert (gbp / 2).value == 500
    
    # Test comparison
    assert gbp > gbp2
    assert gbp < GBP(2000)
    
    # Test string representation
    assert str(gbp) == "£1,000.00"
    assert str(gbp2) == "£500.00"
    assert str(gbp + gbp2) == "£1,500.00"
    assert str(gbp - gbp2) == "£500.00"
    assert str(gbp * 2) == "£2,000.00"
    assert str(gbp / 2) == "£500.00"
    assert str(gbp + GBP(0)) == "£1,000.00"
    assert str(gbp - GBP(0)) == "£1,000.00"
    assert str(gbp * 1) == "£1,000.00"
    assert str(gbp / 1) == "£1,000.00"

test_gbp()