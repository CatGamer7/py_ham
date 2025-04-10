from unittest import TestCase

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
