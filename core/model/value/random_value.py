from random import randint

from .base_value import Base_Value, Reroll


class Random_Value(Base_Value):

    die_size: int

    def __init__(
        self,
        in_die_size: int,
        in_modifier: int = 0,
        in_reroll: Reroll = Reroll.NO
    ):

        if in_die_size < 2:
            raise AttributeError("Dice size nonsensical")

        self.die_size = in_die_size
        super().__init__(in_modifier, in_reroll)

    def __eq__(self, other: "Random_Value"):
        return (self.die_size == other.die_size) and super().__eq__(other)

    def __hash__(self):
        return hash((self.die_size, self.modifier, self.reroll))

    def __str__(self):
        out = f"d{self.die_size}"

        if self.modifier:
            out += f" {self.modifier:+}"

        out += str(self.reroll)

        return out

    def __call__(self) -> int:
        return randint(1, self.die_size) + self.modifier

    def expected_value(self) -> float:
        match self.reroll:
            case Reroll.NO:
                return (self.die_size + 1) / 2 + self.modifier

            case Reroll.ONES:
                # The EV finite sum with a reroll substitutes the
                # first term 1/die_size for a rerolled term EV/die_size.
                # As such, the final EV is computed by adding the difference
                # between sums.

                normal_ev = (self.die_size + 1) / 2
                return normal_ev + (normal_ev - 1) / self.die_size + self.modifier
        
            case Reroll.FULL:
                # The strategy of full reroll is to reroll all the values lower
                # or equal to the ev. Therefore, the finite sum that defines EV
                # can be broken down into 2 peices: 
                # 1) probability of die landing on side that is <= EV, multiplied
                # by the EV of a new roll.
                # 2) part of "normal" EV sum with values > EV.
                # 
                # As such, the algorithm works in the following way:
                # 1. Compute "normal" EV.
                # 2. Compute the number of values <= EV. This is the floor of EV.
                # 3. Compute point 1) of strategy.
                # 4. Compute point 2) of strategy.
                # 5. Sum up the parts and the modifier.

                normal_ev = (self.die_size + 1) / 2
                floored_nat_ev = int(normal_ev)
                lower_rerolled_ev = (floored_nat_ev / self.die_size) * normal_ev
                upper_ev = (floored_nat_ev + 1 + self.die_size) / self.die_size 

                return lower_rerolled_ev + upper_ev + self.modifier
    