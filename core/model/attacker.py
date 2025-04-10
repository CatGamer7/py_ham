from .value import Base_Value, Non_Positive_Value, Simple_Value


class Attacker:

    attacks: Base_Value
    skill: Simple_Value | None
    strength: Simple_Value
    penetration: Non_Positive_Value
    damage: Base_Value

    def __init__(
        self, in_attacks: Base_Value, in_skill: Simple_Value | None,
        in_strength: Simple_Value, in_penetration: Non_Positive_Value,
        in_damage: Base_Value
    ):
        self.attacks = in_attacks
        self.skill = in_skill
        self.strength = in_strength
        self.penetration = in_penetration
        self.damage = in_damage

    def __str__(self):
        return " | ".join(
            (
                f"A: {self.attacks}",
                f"H: {self.skill if self.skill else "n/a"}",
                f"S: {self.strength}",
                f"P: {self.penetration}",
                f"D: {self.damage}"
            )
        )
    
    cool_reference =  "Angreifer"
