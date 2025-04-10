from unittest import TestCase

from core.model import Attacker
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
            "A: d3 | H: n/a | S: 9 | P: -4 | D: d6+6"
        )
