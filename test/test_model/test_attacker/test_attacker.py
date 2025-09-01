from unittest import TestCase

from pyham40k.core.model import Attacker, Format_Exception
from pyham40k.core.model.value import (
    Non_Positive_Value,
    Random_Value,
    Positive_Value,
    Not_Assigned_Value
)


class Test_Attacker(TestCase):

    def test_attacker(self):
        ang = Attacker(
            Random_Value(3),
            Not_Assigned_Value(),
            Positive_Value(9),
            Non_Positive_Value(-4),
            Random_Value(6, 6)
        )

        self.assertEqual(
            str(ang),
            "     A     |     H     |     S     |     P     |     D     \n" + \
            "    d3     |    n/a    |     9     |    -4     |   d6 +6   "
        )

    def test_invalid(self):
        with self.assertRaises(Format_Exception):
            Attacker(
                Not_Assigned_Value(),
                Not_Assigned_Value(),
                Positive_Value(9),
                Non_Positive_Value(-4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                Random_Value(3),
                Positive_Value(9),
                Non_Positive_Value(-4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                Not_Assigned_Value(),
                Random_Value(9),
                Non_Positive_Value(-4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                Not_Assigned_Value(),
                Positive_Value(9),
                Positive_Value(4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                Not_Assigned_Value(),
                Positive_Value(9),
                Non_Positive_Value(-4),
                Not_Assigned_Value()
            )
