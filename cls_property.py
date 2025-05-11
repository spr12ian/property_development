from cls_lot import Lot
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Property:
    address: str
    description: str
    postcode: str    
    lot: Optional[Lot] = None
