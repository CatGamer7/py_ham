from .non_positive_value import Non_Positive_Value
from .random_value import Random_Value
from .simple_value import Simple_Value


class Value_Flyweight:

    non_positives: dict[int, Non_Positive_Value] = {}
    randoms: dict[int, dict[int, Random_Value]] = {}
    simples: dict[int, Simple_Value] = {}

    def get_non_positive_value(self, value: int) -> Non_Positive_Value:
        return Value_Flyweight.__get_or_create_simple_value(
            self.non_positives,
            value,
            Non_Positive_Value
        )
        
    def get_simple_value(self, value: int) -> Simple_Value:
        return Value_Flyweight.__get_or_create_simple_value(
            self.simples,
            value,
            Simple_Value
        )

    def get_random_value(
        self,
        die_size: int,
        modifier: int = 0
    ) -> Random_Value:
        cached_die_size = self.randoms.get(die_size)

        if cached_die_size:        
            cached_modifier = cached_die_size.get(modifier)

            if cached_modifier:
                return cached_modifier
            
            else:
                new_object = Random_Value(die_size, modifier)
                cached_die_size[modifier] = new_object

                return new_object
        
        else:
            new_object = Random_Value(die_size, modifier)
            modifier_dict = {
                modifier: new_object
            }
            self.randoms[die_size] = modifier_dict

            return new_object
    
    @staticmethod
    def __get_or_create_simple_value(
        lookup_dict: dict,
        lookup_obj: int,
        obj_class: type[Simple_Value],
    ) -> Simple_Value:
        "Helper for object lookup. kw_args are passed to object creation"

        cached = lookup_dict.get(lookup_obj)

        if cached:
            return cached
        
        else:
            new_object = obj_class(lookup_obj)
            lookup_dict[lookup_obj] = new_object

            return new_object
