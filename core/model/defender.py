from .value import Simple_Value


class Defender:

    toughness: Simple_Value
    save: Simple_Value
    invulnerable: Simple_Value | None
    feel_no_pain: Simple_Value | None
    
    STAT_HEADER = "    T    |    S    |    I    |    F    "
    STAT_COL_WIDTH = 9

    def __init__(
        self, in_toughness: Simple_Value, in_save: Simple_Value,
        in_invulnerable: Simple_Value | None = None,
        in_feel_no_pain: Simple_Value | None = None
    ):
        self.toughness = in_toughness
        self.save = in_save
        self.invulnerable = in_invulnerable
        self.feel_no_pain = in_feel_no_pain

    def __str__(self):        
        return Defender.STAT_HEADER + "\n" + "|".join(
            (
                f"{str(self.toughness):^{Defender.STAT_COL_WIDTH}}",
                f"{str(self.save):^{Defender.STAT_COL_WIDTH}}",
                f"{f"{str(self.invulnerable):^{Defender.STAT_COL_WIDTH}}" \
                   if self.invulnerable else "   n/a   "}",
                f"{f"{str(self.feel_no_pain):^{Defender.STAT_COL_WIDTH}}" \
                   if self.feel_no_pain else "   n/a   "}"
            )
        )
