from core.model import Format_Exception
from core.model.value import (
    Base_Value,
    Non_Positive_Value,
    Simple_Value,
    Random_Value,
    Value_Flyweight
)


class Simple_Parser:

    value_flyweight: Value_Flyweight

    def __init__(self):
        self.value_flyweight = Value_Flyweight()

    def parse_value(self, value_str: str) -> Base_Value:
        trimmed = value_str.strip()

        # Check the first symbol to deduce the type:
        # 1. Non positive starts with "-" or "0".
        # 2. Simple starts with any digit.
        # 3. Random starts with "d".
        if (trimmed[0] == "-") or (trimmed[0] == "0"):
            return self._parse_non_positive(trimmed)
        
        elif trimmed[0].isdigit():
            return self._parse_simple(trimmed)
        
        elif trimmed[0] == "d":
            return self._parse_random(trimmed)
        
        else:
            raise Format_Exception(
                token=trimmed,
                reason="could not parse any value"
            )

    def _parse_non_positive(self, value_str: str) -> Non_Positive_Value:
        value, mod, reroll = Simple_Value.from_str_validate(value_str)

        return self.value_flyweight.get_simple_value(
            value,
            mod,
            reroll
        )
    
    def _parse_simple(self, value_str: str) -> Simple_Value:
        value, mod, reroll = Simple_Value.from_str_validate(value_str)

        return self.value_flyweight.get_simple_value(
            value,
            mod,
            reroll
        )

    def _parse_random(self, value_str: str) -> Random_Value:
        die_size, mod, reroll = Random_Value.from_str_validate(value_str)

        return self.value_flyweight.get_random_value(
            die_size,
            mod,
            reroll
        )
