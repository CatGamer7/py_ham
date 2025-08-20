from .base_value import Base_Value, Reroll


class Simple_Value(Base_Value):

    value: int

    def __init__(
        self,
        in_value: int,
        in_modifier: int = 0,
        in_reroll: Reroll = Reroll.NO
    ):
        self.value = in_value
        super().__init__(in_modifier, in_reroll)

    def __eq__(self, other: "Simple_Value"):
        return (self.value == other.value) and super().__eq__(other)

    def __hash__(self):
        return hash((self.value, self.modifier, self.reroll))

    def __str__(self):
        out = f"{self.value}"

        if self.modifier:
            out += f" {self.modifier:+}"

        out += str(self.reroll)

        return out
    
    def __call__(self) -> int:
        return self.value

    def expected_value(self) -> float:
        return float(self.value)
    
    def get_value(self) -> int:
        return self.value
    