from .value import Simple_Value
from .format_exception import Format_Exception


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
        if not isinstance(in_toughness, Simple_Value):
            raise Format_Exception(
                token=str(in_toughness),
                reason="not a valid value for defender's toughness"
            )
        
        if not isinstance(in_save, Simple_Value):
            raise Format_Exception(
                token=str(in_save),
                reason="not a valid value for defender's save"
            )
        
        if not (isinstance(in_invulnerable, Simple_Value) or \
                (in_invulnerable is None)):
            raise Format_Exception(
                token=str(in_invulnerable),
                reason="not a valid value for defender's invulnerable"
            )
        
        if not (isinstance(in_feel_no_pain, Simple_Value) or \
                (in_feel_no_pain is None)):
            raise Format_Exception(
                token=str(in_feel_no_pain),
                reason="not a valid value for defender's feel no pain"
            )

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
