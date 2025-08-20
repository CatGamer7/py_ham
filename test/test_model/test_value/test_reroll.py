from unittest import TestCase

from core.model.reroll import Reroll


class Test_Reroll(TestCase):

    def test_reroll_str(self):
        no_str = ""
        no_inst = Reroll.from_str(no_str)
        self.assertEqual(no_str, str(no_inst))

        r1_str = "r1"
        r1_inst = Reroll.from_str(r1_str)
        self.assertEqual(r1_str, str(r1_inst))

        r_str = "r"
        r_inst = Reroll.from_str(r_str)
        self.assertEqual(r_str, str(r_inst))
