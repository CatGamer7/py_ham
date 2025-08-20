from unittest import TestCase

from core.model import Format_Exception, Reroll
from core.model.value import Simple_Value, Non_Positive_Value, Random_Value
from core.parser import Simple_Parser


class Test_Simple_Parser(TestCase):

    def test_parse_value(self):
        parser = Simple_Parser()

        simple = parser.parse_value("1 +1 r1")
        self.assertEqual(
            simple,
            Simple_Value(1, 1, Reroll.ONES)
        )

        non_positive = parser.parse_value("-4")
        self.assertEqual(
            non_positive,
            Non_Positive_Value(-4, 0, Reroll.NO)
        )

        random = parser.parse_value("d6 -1 r")
        self.assertEqual(
            random,
            Random_Value(6, -1, Reroll.FULL)
        )
