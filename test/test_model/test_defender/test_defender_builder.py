from unittest import TestCase

from core.model.defender import Defender, Defender_Builder
from core.model.value import Positive_Value, Not_Assigned_Value


class Test_Defender_Builder(TestCase):
    
    def test_build(self):
        defender = Defender(
            Positive_Value(5),
            Positive_Value(2),
            Positive_Value(4),
            Not_Assigned_Value()
        )

        builder = Defender_Builder()

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            defender.toughness
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            defender.save
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            defender.invulnerable
        )
        self.assertFalse(res)

        with self.assertRaises(AttributeError):
            builder.build()
        res = builder.build_step(
            defender.feel_no_pain
        )
        self.assertTrue(res)

        with self.assertRaises(AttributeError):
            builder.build_step(
                defender.toughness
            )

        defender_built = builder.build()

        self.assertEqual(
            defender,
            defender_built
        )
