from unittest import TestCase

from pyham40k.core.calculator import Real_Calculator
from pyham40k.core.parser import Simple_Parser


class Test_Real_Calculator(TestCase):

    def test_total_wounds(self):
        prsr = Simple_Parser()

        atkr = prsr.parse_attacker(
            " d6 +1 r1 | 4 | 14 | -3 | d6 "
        )
        defr = prsr.parse_defender(
            " 5 | 4 | n/a | n/a "
        )

        calc = Real_Calculator(atkr, defr)

        attacks = calc.get_attacks()
        self.assertAlmostEqual(
            59 / 12,
            attacks
        )

        hits = calc.get_hit_proportion()
        self.assertAlmostEqual(
            1 / 2,
            hits
        )

        wounds = calc.get_wound_proportion()
        self.assertAlmostEqual(
            5 / 6,
            wounds
        )
        
        non_saves = calc.get_unsaved_proportion()
        self.assertAlmostEqual(
            1.0,
            non_saves
        )

        damage = calc.get_damage()
        self.assertAlmostEqual(
            7 / 2,
            damage 
        )

        felt = calc.get_felt_proprtion()
        self.assertAlmostEqual(
            1.0,
            felt
        )

        total = calc.calculate_total_unsvaed_wounds()
        self.assertAlmostEqual(
            (59 / 12) * (35 / 24),
            total
        )
