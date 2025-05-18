from cls_buyer import Buyer
from cls_buyer_types import BuyerTypes


buyers: dict[str, Buyer] = {
    "CB Developments": Buyer(
        buyer_type=BuyerTypes.LIMITED_COMPANY,
        name="CB Developments",
    ),
    "Charlie": Buyer(
        buyer_type=BuyerTypes.NON_FIRST_TIME_BUYER,
        name="Charlotte Bernard",
    ),
    "Ian & Ian": Buyer(
        buyer_type=BuyerTypes.SECOND_HOME_BUYER,
        name="Ian Bernard & Ian Sweeney",
    ),
    "Josh": Buyer(
        buyer_type=BuyerTypes.FIRST_TIME_BUYER,
        name="Joshua Bernard",
    ),
    "Josh (his own property)": Buyer(
        buyer_type=BuyerTypes.NON_FIRST_TIME_BUYER,
        name="Joshua Bernard",
    ),
}
