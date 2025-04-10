from unittest import TestCase

from core.model.value import (
    Base_Value,
    Non_Positive_Value,
    Random_Value,
    Simple_Value,
    Value_Flyweight
)


class Test_Value_Flyweight(TestCase):

    def test_flyweight_non_positive(self):
        flyweight = Value_Flyweight()

        n1 = flyweight.get_non_positive_value(-1)
        n2 = flyweight.get_non_positive_value(-4)
        n1a1 = flyweight.get_non_positive_value(-1)

        self.__compare_cahced(n1, n2, n1a1, Non_Positive_Value)
        
    def test_flyweight_random(self):
        flyweight = Value_Flyweight()

        n1 = flyweight.get_random_value(6)
        n2 = flyweight.get_random_value(6, 1)
        n1a1 = flyweight.get_random_value(6)

        self.__compare_cahced(n1, n2, n1a1, Random_Value)

    def test_flyweight_simple(self):
        flyweight = Value_Flyweight()

        n1 = flyweight.get_simple_value(1)
        n2 = flyweight.get_simple_value(2)
        n1a1 = flyweight.get_simple_value(1)

        self.__compare_cahced(n1, n2, n1a1, Simple_Value)

    def __compare_cahced(
        self,
        obj_1: Base_Value,
        obj_2: Base_Value,
        obj_1a1: Base_Value,
        Obj_class: type[Base_Value]
    ) -> None:
        self.assertIsInstance(
            obj_1,
            Obj_class
        )
        self.assertIsInstance(
            obj_2,
            Obj_class
        )
        self.assertIsInstance(
            obj_1a1,
            Obj_class
        )

        self.assertIs(
            obj_1,
            obj_1a1
        )