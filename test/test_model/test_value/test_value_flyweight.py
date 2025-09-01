from unittest import TestCase

from pyham40k.core.model.value import (
    Base_Value,
    Non_Positive_Value,
    Random_Value,
    Simple_Value,
    Value_Flyweight
)


class Test_Value_Flyweight(TestCase):

    def test_flyweight_non_positive(self):
        n1 = Value_Flyweight.get_non_positive_value(-1)
        n2 = Value_Flyweight.get_non_positive_value(-4)
        n1a1 = Value_Flyweight.get_non_positive_value(-1)

        self.__compare_cahced(n1, n2, n1a1, Non_Positive_Value)
        
    def test_flyweight_random(self):
        n1 = Value_Flyweight.get_random_value(6)
        n2 = Value_Flyweight.get_random_value(6, 1)
        n1a1 = Value_Flyweight.get_random_value(6)

        self.__compare_cahced(n1, n2, n1a1, Random_Value)

    def test_flyweight_positive(self):
        n1 = Value_Flyweight.get_positive_value(1)
        n2 = Value_Flyweight.get_positive_value(2)
        n1a1 = Value_Flyweight.get_positive_value(1)

        self.__compare_cahced(n1, n2, n1a1, Simple_Value)

    def test_flyweght_na(self):
        na1 = Value_Flyweight.get_not_assigned_value()
        na2 = Value_Flyweight.get_not_assigned_value()

        self.assertIs(na1, na2)

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

    def test_persistence(self):
        block = lambda: Value_Flyweight.get_positive_value(1)

        o1 = Value_Flyweight.get_positive_value(1)
        o2 = block()

        self.assertIs(o1, o2)
