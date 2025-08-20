from unittest import TestCase

from core.model import Format_Exception, Reroll
from core.model.value import Base_Value


class Test_Base_Value(TestCase):

    def test_base_value_from_str(self):
        with self.assertRaises(Format_Exception):
            Base_Value._from_str_partial("")
            
        with self.assertRaises(Format_Exception):
            Base_Value._from_str_partial("1 +1 r1 r1")

        tup = Base_Value._from_str_partial("1 +1 r1")
        self.assertEqual(
            tup,
            ("1", 1, Reroll.ONES)
        )

        tup = Base_Value._from_str_partial("1 +1")
        self.assertEqual(
            tup,
            ("1", 1, Reroll.NO)
        )
        
        tup = Base_Value._from_str_partial("1 r1")
        self.assertEqual(
            tup,
            ("1", 0, Reroll.ONES)
        )

    def test_parse_modifier(self):
        mod = Base_Value._parse_modifier("+1")
        self.assertEqual(mod, 1)
        
        mod = Base_Value._parse_modifier("1")
        self.assertEqual(mod, 1)

        mod = Base_Value._parse_modifier("-1")
        self.assertEqual(mod, -1)

        with self.assertRaises(Format_Exception):
            Base_Value._parse_modifier("d6")
