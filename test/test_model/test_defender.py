from unittest import TestCase

from core.model import Defender
from core.model.value import Simple_Value


class Test_Defender(TestCase):

    def test_defender(self):
        de = Defender(
            Simple_Value(5),
            Simple_Value(3),
            Simple_Value(4),
            None
        )
        
        self.assertEqual(
            str(de),
            "    T    |    S    |    I    |    F    \n" + \
            "    5    |    3    |    4    |   n/a   "
        )
