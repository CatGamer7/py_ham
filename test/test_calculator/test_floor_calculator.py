from unittest import TestCase

from pyham40k.core.calculator import Floor_Calculator
from pyham40k.core.parser import Simple_Parser


class Test_Floor_Calculator(TestCase):

    def test_total_wounds(self):
        prsr = Simple_Parser()

        atkr = prsr.parse_attacker(
            " 3d6 | 4 | 5 | 0 | d6 "
        )
        defr = prsr.parse_defender(
            " 4 | 5 | 5 | n/a "
        )

        calc = Floor_Calculator(atkr, defr)

        attacks = calc.get_attacks()
        self.assertAlmostEqual(
            10.0,
            attacks
        )

        damage = calc.get_damage()
        self.assertAlmostEqual(
            3.0,
            damage 
        )

        total = calc.calculate_total_unsvaed_wounds()
        self.assertAlmostEqual(
            6.0,
            total
        )
