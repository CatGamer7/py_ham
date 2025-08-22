from .value import Base_Value, Non_Positive_Value, Simple_Value
from .format_exception import Format_Exception


class Attacker:

    attacks: Base_Value
    skill: Simple_Value | None
    strength: Simple_Value
    penetration: Non_Positive_Value
    damage: Base_Value

    STAT_HEADER = "    A    |    H    |    S    |    P    |    D    "
    STAT_COL_WIDTH = 9

    def __init__(
        self, in_attacks: Base_Value, in_skill: Simple_Value | None,
        in_strength: Simple_Value, in_penetration: Non_Positive_Value,
        in_damage: Base_Value
    ):
        if not isinstance(in_attacks, Base_Value):
            raise Format_Exception(
                token=str(in_attacks),
                reason="not a valid value for attacker's attack"
            )
        
        if not (isinstance(in_skill, Simple_Value) or (in_skill is None)):
            raise Format_Exception(
                token=str(in_skill),
                reason="not a valid value for attacker's skill"
            )
        
        if not isinstance(in_strength, Simple_Value):
            raise Format_Exception(
                token=str(in_strength),
                reason="not a valid value for attacker's strength"
            )

        if not isinstance(in_penetration, Non_Positive_Value):
            raise Format_Exception(
                token=str(in_penetration),
                reason="not a valid value for attacker's penetration"
            )
        
        if not isinstance(in_damage, Base_Value):
            raise Format_Exception(
                token=str(in_damage),
                reason="not a valid value for attacker's damage"
            )
        
        self.attacks = in_attacks
        self.skill = in_skill
        self.strength = in_strength
        self.penetration = in_penetration
        self.damage = in_damage

    def __str__(self):
        return Attacker.STAT_HEADER + "\n" + "|".join(
            (
                f"{str(self.attacks):^{Attacker.STAT_COL_WIDTH}}",
                f"{f"{str(self.skill):^{Attacker.STAT_COL_WIDTH}}" \
                   if self.skill else "   n/a   "}",
                f"{str(self.strength):^{Attacker.STAT_COL_WIDTH}}",
                f"{str(self.penetration):^{Attacker.STAT_COL_WIDTH}}",
                f"{str(self.damage):^{Attacker.STAT_COL_WIDTH}}"
            )
        )
    
    cool_reference =  "Angreifer"
