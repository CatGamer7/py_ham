from .base_value import Base_Value
from .non_positive_value import Non_Positive_Value
from .random_value import Random_Value
from .positive_value import Positive_Value

from core.model.reroll import Reroll


class Value_Flyweight:

    randoms: dict[int, Random_Value] = {}
    simples: dict[int, Positive_Value] = {}

    def get_non_positive_value(
        self,
        in_value: int,
        in_modifier: int = 0,
        in_reroll: Reroll = Reroll.NO
    ) -> Non_Positive_Value:
        key = hash((in_value, in_modifier, in_reroll))

        return Value_Flyweight.__get_or_create_value(
            self.simples,
            key,
            Non_Positive_Value,
            in_value = in_value,
            in_modifier = in_modifier,
            in_reroll = in_reroll
        )
        
    def get_positive_value(
        self,
        in_value: int,
        in_modifier: int = 0,
        in_reroll: Reroll = Reroll.NO
    ) -> Positive_Value:
        key = hash((in_value, in_modifier, in_reroll))

        return Value_Flyweight.__get_or_create_value(
            self.simples,
            key,
            Positive_Value,
            in_value = in_value,
            in_modifier = in_modifier,
            in_reroll = in_reroll
        )

    def get_random_value(
        self,
        in_die_size: int,
        in_modifier: int = 0,
        in_reroll: Reroll = Reroll.NO
    ) -> Random_Value:
        key = hash((in_die_size, in_modifier, in_reroll))

        return Value_Flyweight.__get_or_create_value(
            self.randoms,
            key,
            Random_Value,
            in_die_size = in_die_size,
            in_modifier = in_modifier,
            in_reroll = in_reroll
        )
    
    @staticmethod
    def __get_or_create_value(
        lookup_dict: dict,
        lookup_obj: int,
        obj_class: type[Base_Value],
        **kw_args
    ) -> Base_Value:
        "Helper for object lookup. kw_args are passed to constructor"

        cached = lookup_dict.get(lookup_obj)

        if cached:
            return cached
        
        else:
            new_object = obj_class(**kw_args)
            lookup_dict[lookup_obj] = new_object

            return new_object
