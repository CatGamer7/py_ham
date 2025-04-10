from unittest import TestCase

from core.model.value import Random_Value


class Test_Random_Value(TestCase):

    def test_random_value(self):
        d3 = Random_Value(3)
        d6 = Random_Value(6)
        d6_6 = Random_Value(6, 6)

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
            "d6+6"
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
