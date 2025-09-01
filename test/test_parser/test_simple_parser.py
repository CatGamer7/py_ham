from unittest import TestCase

from pyham40k.core.model import Format_Exception, Reroll
from pyham40k.core.model.value import (
    Simple_Value,
    Non_Positive_Value,
    Random_Value,
    Not_Assigned_Value
)
from pyham40k.core.parser import Simple_Parser


class Test_Simple_Parser(TestCase):

    def test_parse_value(self):
        parser = Simple_Parser()

        simple = parser.parse_value("1 +1 r1")
        self.assertIsInstance(
            simple,
            Simple_Value
        )
        self.assertEqual(
            simple,
            Simple_Value(1, 1, Reroll.ONES)
        )

        non_positive = parser.parse_value("-4")
        self.assertIsInstance(
            non_positive,
            Non_Positive_Value
        )
        self.assertEqual(
            non_positive,
            Non_Positive_Value(-4, 0, Reroll.NO)
        )

        random = parser.parse_value("d6 -1 r")
        self.assertIsInstance(
            random,
            Random_Value
        )
        self.assertEqual(
            random,
            Random_Value(6, -1, Reroll.FULL)
        )

        none = parser.parse_value("")
        self.assertEqual(
            none,
            Not_Assigned_Value()
        )

        na = parser.parse_value("n/a")
        self.assertEqual(
            na,
            Not_Assigned_Value()
        )

    def test_parse_attacker(self):
        parser = Simple_Parser()

        attacker = parser.parse_attacker(
            "   1    |    4    |    9    |   -4    |  d6 +2  "
        )
        self.assertEqual(
            str(attacker),
            "     A     |     H     |     S     |     P     |     D     \n" + \
            "     1     |     4     |     9     |    -4     |   d6 +2   "
        )

        with self.assertRaises(Format_Exception):
            parser.parse_attacker(
                "    4    |    9    |   -4    |  d6 +2  "
            )
        
        with self.assertRaises(Format_Exception):
            parser.parse_attacker(
                "   1    |   1    |    4    |    9    |   -4    |  d6 +2  "
            )
        
        with self.assertRaises(Format_Exception):
            parser.parse_attacker(
                "  n/a   |    4    |    9    |   -4    |  d6 +2  "
            )

    def test_parse_defender(self):
        parser = Simple_Parser()

        defender = parser.parse_defender(
            "    9    |    2    |    5    |    5    "
        )
        self.assertEqual(
            str(defender),
            "     T     |     S     |     I     |     F     \n" + \
            "     9     |     2     |     5     |     5     "
        )

        with self.assertRaises(Format_Exception):
            parser.parse_defender(
                "    9    |    9    |    2    |    5    |    5    "
            )

        with self.assertRaises(Format_Exception):
            parser.parse_defender(
                "    2    |    5    |    5    "
            )

        with self.assertRaises(Format_Exception):
            parser.parse_defender(
                "   n/a   |    2    |    5    |    5    "
            )
