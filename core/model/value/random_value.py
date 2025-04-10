from random import randint

from .base_value import Base_Value


class Random_Value(Base_Value):

    die_size: int
    modifier: int | None

    def __init__(self, in_die_size: int, in_modifier: int = 0):
        if in_die_size < 2:
            raise AttributeError("Dice size nonsensical")

        self.die_size = in_die_size
        self.modifier = in_modifier

    def __str__(self):
        if not self.modifier:
            return f"d{self.die_size}"
        else:
            return f"d{self.die_size}+{self.modifier}"
    
    def __call__(self) -> int:
        return randint(1, self.die_size) + self.modifier

    def expected_value(self) -> float:
        return (self.die_size + 1) / 2 + self.modifier
    