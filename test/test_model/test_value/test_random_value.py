from unittest import TestCase

from core.model import Format_Exception, Reroll
from core.model.value import Random_Value


class Test_Random_Value(TestCase):

    def test_random_value(self):
        d3 = Random_Value(3)
        d6 = Random_Value(6)
        d6_6 = Random_Value(6, 6)
        _3d6 = Random_Value(6, in_multiplier=3)

        self.assertEqual(
            str(d3),
            "d3"
        )
        self.assertEqual(
            str(d6),
            "d6"
        )
        self.assertEqual(
            str(d6_6),
            "d6 +6"
        )
        self.assertEqual(
            str(_3d6),
            "3d6"
        )

        self.assertIn(
            d3(),
            range(1, 4)
        )
        self.assertIn(
            d6(),
            range(1, 7)
        )
        self.assertIn(
            d6_6(),
            range(6, 13)
        )
        self.assertIn(
            _3d6(),
            range(3, 18)
        )

        self.assertAlmostEqual(
            d3.expected_value(),
            2.0
        )
        self.assertAlmostEqual(
            d6.expected_value(),
            3.5
        )
        self.assertAlmostEqual(
            d6_6.expected_value(),
            9.5
        )
        self.assertAlmostEqual(
            _3d6.expected_value(),
            10.5
        )

    def test_random_value_str(self):
        d6 = Random_Value(6, 1, Reroll.NO)
        self.assertEqual(
            str(d6),
            "d6 +1"
        )

        d6 = Random_Value(6, -1, Reroll.NO)
        self.assertEqual(
            str(d6),
            "d6 -1"
        )

        d6 = Random_Value(6, 0, Reroll.ONES)
        self.assertEqual(
            str(d6),
            "d6 r1"
        )

        d6 = Random_Value(6, 0, Reroll.FULL)
        self.assertEqual(
            str(d6),
            "d6 r"
        )
        
        d6 = Random_Value(6, 1, Reroll.ONES)
        self.assertEqual(
            str(d6),
            "d6 +1 r1"
        )

        _3d6_1_r1 = Random_Value(6, 1, Reroll.ONES, 3)
        self.assertEqual(
            str(_3d6_1_r1),
            "3d6 +1 r1"
        )

    def test_from_str_validate(self):
        tup = Random_Value.from_str_validate("2d6 +1 r1")
        self.assertEqual(
            tup,
            (6, 1, Reroll.ONES, 2)
        )

        with self.assertRaises(Format_Exception):
            Random_Value.from_str_validate("d1 +1 r1")

        with self.assertRaises(Format_Exception):
            Random_Value.from_str_validate("dd6 +1 r1")

    def test_ev(self):
        d6_r1 = Random_Value(6, 0, Reroll.ONES)
        self.assertAlmostEqual(
            d6_r1.expected_value(),
            47 / 12
        )

        d6_r = Random_Value(6, 0, Reroll.FULL)
        self.assertAlmostEqual(
            d6_r.expected_value(),
            51 / 12
        )

        d6_p1_r1 = Random_Value(6, 1, Reroll.ONES)
        self.assertAlmostEqual(
            d6_p1_r1.expected_value(),
            59 / 12
        )

        d6_p2_r = Random_Value(6, 2, Reroll.FULL)
        self.assertAlmostEqual(
            d6_p2_r.expected_value(),
            75 / 12
        )
        
        _2d6_p1_r1 = Random_Value(6, 1, Reroll.ONES, 2)
        self.assertAlmostEqual(
            _2d6_p1_r1.expected_value(),
            59 / 6
        )
