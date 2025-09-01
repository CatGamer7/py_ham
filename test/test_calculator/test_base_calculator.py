from unittest import TestCase

from pyham40k.core.calculator.base_calculator_strategy import Base_Calculator_Strategy
from pyham40k.core.model import Reroll


class Test_Base_Calculator(TestCase):

    def test_clamp_mod(self):
        clamp = Base_Calculator_Strategy._clamp_modifier

        self.assertEqual(
            -1,
            clamp(-2)
        )
        self.assertEqual(
            -1,
            clamp(-1)
        )
        self.assertEqual(
            0,
            clamp(0)
        )
        self.assertEqual(
            1,
            clamp(1)
        )
        self.assertEqual(
            1,
            clamp(2)
        )

    def test_clamp_pass(self):
        clamp = Base_Calculator_Strategy._clamp_passing_value
        die = Base_Calculator_Strategy.DIE_SIZE

        self.assertEqual(
            2,
            clamp(2)
        )
        self.assertEqual(
            2,
            clamp(2)
        )
        self.assertEqual(
            die,
            clamp(die)
        )
        self.assertEqual(
            die,
            clamp(die + 1)
        )

    def test_proportion_passed(self):
        prop = Base_Calculator_Strategy._proportion_passed
        die = Base_Calculator_Strategy.DIE_SIZE
    
        self.assertAlmostEqual(
            1 / die,
            prop(die)
        )
        self.assertAlmostEqual(
            1 - (1 / die),
            prop(2)
        )
        self.assertAlmostEqual(
            0.0,
            prop(die + 1)
        )

    def test_proportion_rerolled(self):
        prop_reroll = Base_Calculator_Strategy._proportion_rerolled
        die = Base_Calculator_Strategy.DIE_SIZE
        prop = 1 - (1 / die)

        self.assertAlmostEqual(
            prop,
            prop_reroll(prop, Reroll.NO)
        )
        self.assertAlmostEqual(
            prop + (1 / die) * prop,
            prop_reroll(prop, Reroll.ONES)
        )
        self.assertAlmostEqual(
            prop + (1 - prop) * prop,
            prop_reroll(prop, Reroll.FULL)
        )

    def test_clamp_and_get_proportion_rerolled(self):
        fn = Base_Calculator_Strategy._clamp_and_get_proportion_rerolled
        die = Base_Calculator_Strategy.DIE_SIZE

        self.assertAlmostEqual(
            1 - 1 / (die * die),
            fn(2, Reroll.FULL)
        )
        self.assertAlmostEqual(
            1 / die,
            fn(die, Reroll.NO)
        )
        self.assertAlmostEqual(
            1 / die + 1 / (die * die),
            fn(die+1, Reroll.ONES)
        )
