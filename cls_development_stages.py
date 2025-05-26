from __future__ import annotations
import re
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from cls_development import Development  # Only for type checking, no runtime import


class DevelopmentStage(ABC):
    # lines must always be passed in and is not optional
    @abstractmethod
    def append_details(
        self, development: Development, lines: list[str], sub_indent: str = ""
    ) -> None:
        pass

    @property
    def label(self) -> str:
        # Convert CamelCase class name to "Camel Case"
        return re.sub(r"(?<!^)(?=[A-Z])", " ", self.__class__.__name__)

    def __str__(self) -> str:
        return self.label

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"


class Bought(DevelopmentStage):
    def append_details(
        self, development: Development, lines: list[str], sub_indent: str = ""
    ) -> None:
        pass


class Considered(DevelopmentStage):
    def append_details(
        self, development: Development, lines: list[str], sub_indent: str = ""
    ) -> None:
        pass


class Sold(DevelopmentStage):
    def append_details(
        self, development: Development, lines: list[str], sub_indent: str = ""
    ) -> None:
        pass


class UnderConsideration(DevelopmentStage):
    def append_details(
        self, development: Development, lines: list[str], sub_indent: str = ""
    ) -> None:
        lines.append(
            f"{development.fixed_location(development.maximum_bid, 'Maximum bid', sub_indent)}"
        )


class DevelopmentStages:
    """
    A collection of development stages.
    """

    BOUGHT = Bought()
    CONSIDERED = Considered()
    SOLD = Sold()
    UNDER_CONSIDERATION = UnderConsideration()

    @classmethod
    def all(cls):
        return [cls.BOUGHT, cls.CONSIDERED, cls.SOLD, cls.UNDER_CONSIDERATION]
