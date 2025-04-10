from abc import ABC, abstractmethod


class Base_Value(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __call__(self) -> int:
        "samples a scalar value"

    @abstractmethod
    def expected_value(self) -> float:
        "returns a scalar - EV of the value"
