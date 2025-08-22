from unittest import TestCase

from core.model.attacker import Attacker, Attacker_Builder
from core.model.value import Non_Positive_Value, Random_Value, Positive_Value


class Test_Attacker_Builder(TestCase):

    def test_build(self):
        attacker = Attacker(
            Random_Value(6),
            None,
            Positive_Value(4),
            Non_Positive_Value(-1),
            Positive_Value(1)
        )

        builder = Attacker_Builder()

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            attacker.attacks
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            attacker.skill
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            attacker.strength
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            attacker.penetration
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            attacker.damage
        )
        self.assertTrue(res)

        with self.assertRaises(AttributeError):
            builder.build_step(
                attacker.attacks
            )

        attacker_built = builder.build()

        self.assertEqual(
            attacker,
            attacker_built
        )
