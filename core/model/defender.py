from .value import Simple_Value


class Defender:

    toughness: Simple_Value
    save: Simple_Value
    invulnerable: Simple_Value | None
    feel_no_pain: Simple_Value | None
    
    def __init__(
        self, in_toughness: Simple_Value, in_save: Simple_Value,
        in_invulnerable: Simple_Value | None,
        in_feel_no_pain: Simple_Value | None
    ):
        self.toughness = in_toughness
        self.save = in_save
        self.invulnerable = in_invulnerable
        self.feel_no_pain = in_feel_no_pain

    def __str__(self):
        return " | ".join(
            (
                f"T: {self.toughness}",
                f"S: {self.save}",
                f"I: {self.invulnerable if self.invulnerable else "n/a"}",
                f"F: {self.feel_no_pain if self.feel_no_pain else "n/a"}"
            )
        )
