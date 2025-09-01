from unittest import TestCase

from pyham40k.core.model import Format_Exception, Reroll
from pyham40k.core.model.value import Non_Positive_Value


class Test_Non_Positive_Value(TestCase):

    def test_non_positive_value(self):
        # Number 5 was chosen after 4 hour meeting with the dev team
        with self.assertRaises(AttributeError):
            Non_Positive_Value(5)

        n1 = Non_Positive_Value(-1)

        self.assertEqual(
            str(n1),
            "-1"
        )

        self.assertEqual(
            n1(),
            -1
        )

        self.assertAlmostEqual(
            n1.expected_value(),
            -1.0
        )

        self.assertEqual(
            n1.get_value(),
            -1
        )

    def test_from_str_validate(self):
        tup = Non_Positive_Value.from_str_validate("-4")
        self.assertEqual(
            tup,
            (-4, 0, Reroll.NO)
        )

        with self.assertRaises(Format_Exception):
            Non_Positive_Value.from_str_validate("4")
