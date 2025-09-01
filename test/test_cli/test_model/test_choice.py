from unittest import TestCase

from pyham40k.cli.model import Cli_Choice


class Test_Cli_Choice(TestCase):

    def test_str(self):
        choice = Cli_Choice(
            "Test option",
            ("1", "Y")
        )

        self.assertEqual(
            str(choice),
            "( 1 | Y ) Test option"
        )

    def test_validate(self):
        choice = Cli_Choice(
            "Test option",
            ("1", "Y")
        )

        self.assertTrue(
            choice.validate("1")
        )
        self.assertTrue(
            choice.validate("Y")
        )
        self.assertFalse(
            choice.validate("N")
        )

    def test_duplicates(self):
        choice = Cli_Choice(
            "Test option",
            ("1", "Y", "Y", "1", "", "")
        )

        self.assertEqual(
            str(choice),
            "( 1 | Y | default ) Test option"
        )

    def test_upper(self):
        choice = Cli_Choice(
            "Test option",
            ("1", "y", "e", "")
        )

        self.assertEqual(
            str(choice),
            "( 1 | Y | E | default ) Test option"
        )
