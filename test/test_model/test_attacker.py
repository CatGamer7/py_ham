from unittest import TestCase

from core.model import Attacker, Format_Exception
from core.model.value import Non_Positive_Value, Random_Value, Simple_Value


class Test_Attacker(TestCase):

    def test_attacker(self):
        ang = Attacker(
            Random_Value(3),
            None,
            Simple_Value(9),
            Non_Positive_Value(-4),
            Random_Value(6, 6)
        )

        self.assertEqual(
            str(ang),
            "    A    |    H    |    S    |    P    |    D    \n" + \
            "   d3    |   n/a   |    9    |   -4    |  d6 +6  "
        )

    def test_invalid(self):
        with self.assertRaises(Format_Exception):
            Attacker(
                None,
                None,
                Simple_Value(9),
                Non_Positive_Value(-4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                Random_Value(3),
                Simple_Value(9),
                Non_Positive_Value(-4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                None,
                Random_Value(9),
                Non_Positive_Value(-4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                None,
                Simple_Value(9),
                Simple_Value(4),
                Random_Value(6, 6)
            )

        with self.assertRaises(Format_Exception):
            Attacker(
                Random_Value(3),
                None,
                Simple_Value(9),
                Non_Positive_Value(-4),
                None
            )
