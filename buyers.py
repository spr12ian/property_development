from cls_buyer import Buyer
from cls_buyer_types import BuyerTypes
from gbp import GBP


cb_developments = Buyer(
    BuyerTypes.LIMITED_COMPANY,
    name="CB Developments",
)
charlie = Buyer(
    BuyerTypes.NON_FIRST_TIME_BUYER,
    name="Charlotte Bernard",
)
ian_and_ian = Buyer(
    BuyerTypes.SECOND_HOME_BUYER,
    name="Ian Bernard & Ian Sweeney",
)
josh = Buyer(
    BuyerTypes.FIRST_TIME_BUYER,
    name="Joshua Bernard",  
)
josh2 = Buyer(
    BuyerTypes.NON_FIRST_TIME_BUYER,
    name="Joshua Bernard",  
)


buyers: dict[str, Buyer] = {
    "CB Developments": cb_developments,
    "Charlie": charlie,
    "Ian & Ian": ian_and_ian,
    "Josh": josh,
    "Josh (his own property)": josh2,
}
