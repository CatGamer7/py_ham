from unittest import TestCase

from core.model import Format_Exception, Reroll
from core.model.value import Simple_Value


class Test_Simple_Value(TestCase):

    def test_simple_value(self):
        # Number 7 was chosen after 3 hour meeting with the dev team
        i7 = Simple_Value(7)

        self.assertEqual(
            str(i7),
            "7"
        )

        self.assertEqual(
            i7(),
            7
        )

        self.assertAlmostEqual(
            i7.expected_value(),
            7.0
        )

        self.assertEqual(
            i7.get_value(),
            7
        )

    def test_simple_value_str(self):
        i7 = Simple_Value(7, 1, Reroll.NO)
        self.assertEqual(
            str(i7),
            "7 +1"
        )

        i7 = Simple_Value(7, -1, Reroll.NO)
        self.assertEqual(
            str(i7),
            "7 -1"
        )

        i7 = Simple_Value(7, 0, Reroll.ONES)
        self.assertEqual(
            str(i7),
            "7 r1"
        )

        i7 = Simple_Value(7, 0, Reroll.FULL)
        self.assertEqual(
            str(i7),
            "7 r"
        )
        
        i7 = Simple_Value(7, 1, Reroll.ONES)
        self.assertEqual(
            str(i7),
            "7 +1 r1"
        )

    def test_from_str_validate(self):
        tup = Simple_Value.from_str_validate("1 +1 r1")
        self.assertEqual(
            tup,
            (1, 1, Reroll.ONES)
        )

        with self.assertRaises(Format_Exception):
            Simple_Value.from_str_validate("d6 +1 r1")
