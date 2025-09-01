from unittest import TestCase

from pyham40k.core.model import Format_Exception, Reroll
from pyham40k.core.model.value import Positive_Value


class Test_Positive_Value(TestCase):

    def test_positive_value(self):
        with self.assertRaises(AttributeError):
            Positive_Value(0)

        p1 = Positive_Value(1)

        self.assertEqual(
            str(p1),
            "1"
        )

        self.assertEqual(
            p1(),
            1
        )

        self.assertAlmostEqual(
            p1.expected_value(),
            1.0
        )

        self.assertEqual(
            p1.get_value(),
            1
        )

    def test_from_str_validate(self):
        tup = Positive_Value.from_str_validate("9")
        self.assertEqual(
            tup,
            (9, 0, Reroll.NO)
        )

        with self.assertRaises(Format_Exception):
            Positive_Value.from_str_validate("0")
