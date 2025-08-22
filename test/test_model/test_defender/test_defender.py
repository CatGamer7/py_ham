from unittest import TestCase

from core.model import Defender, Format_Exception
from core.model.value import Positive_Value, Random_Value


class Test_Defender(TestCase):

    def test_defender(self):
        de = Defender(
            Positive_Value(5),
            Positive_Value(3),
            Positive_Value(4),
            None
        )
        
        self.assertEqual(
            str(de),
            "    T    |    S    |    I    |    F    \n" + \
            "    5    |    3    |    4    |   n/a   "
        )

    def test_invalid(self):            
        with self.assertRaises(Format_Exception):
            Defender(
                Random_Value(5),
                Positive_Value(3),
                Positive_Value(4),
                None,
            )
            
        with self.assertRaises(Format_Exception):
            Defender(
                Positive_Value(5),
                Random_Value(3),
                Positive_Value(4),
                None,
            )
            
        with self.assertRaises(Format_Exception):
            Defender(
                Positive_Value(5),
                Positive_Value(3),
                Random_Value(4),
                None,
            )
            
        with self.assertRaises(Format_Exception):
            Defender(
                Positive_Value(5),
                Positive_Value(3),
                Positive_Value(4),
                Random_Value(6),
            )
