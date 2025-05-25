import cls_ownership_types
from cls_ownership_types import (
    OwnershipTypes,
    Commonhold,
    Freehold,
    Leasehold,
    ShareOfFreehold,
)
import pytest
from typing import List
from pytest import raises
from pytest import mark
from pytest import fixture
from pytest import param

for ownership_type in OwnershipTypes.all():
    ownership_type_name = ownership_type.label

    @mark.parametrize("ownership_type", [ownership_type])
    def test_ownership_type_str(ownership_type: OwnershipTypes):
        assert str(ownership_type) == ownership_type_name

    @mark.parametrize("ownership_type", [ownership_type])
    def test_ownership_type_repr(ownership_type: OwnershipTypes):
        assert repr(ownership_type) == f"{ownership_type.__class__.__name__}()"

    @mark.parametrize("ownership_type", [ownership_type])
    def test_ownership_type_label(ownership_type: OwnershipTypes):
        assert ownership_type.label == ownership_type_name

    
# Usage
s=ShareOfFreehold()
print(s)

for ot in OwnershipTypes.all():
    print(ot, repr(ot))
