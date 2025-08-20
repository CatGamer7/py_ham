from abc import ABC, abstractmethod

from core.model.reroll import Reroll


class Base_Value(ABC):

    modifier: int
    reroll: Reroll

    def __init__(self, in_modifier: int = 0, in_reroll: Reroll = Reroll.NO):
        self.modifier = in_modifier
        self.reroll = in_reroll
        super().__init__()

    def __eq__(self, other: "Base_Value"):
        return (self.modifier == other.modifier) and \
            (self.reroll == other.reroll)

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __call__(self) -> int:
        "samples a scalar value"

    @abstractmethod
    def expected_value(self) -> float:
        "returns a scalar - EV of the value"
