from unittest import TestCase

from pyham40k.cli.model import Cli_Prompt, Cli_Choice
from test.mock import Mock_Console


class Test_Cli_Prompt(TestCase):

    def test_collect(self):
        prompt = Cli_Prompt(
            "Test prompt",
            (
                Cli_Choice("choice 1", ("1", "Y")),
                Cli_Choice("choice 2", ("2", "N")),
            )
        )

        self.assertEqual(
            prompt._collect_inputs(),
            ["1", "Y", "2", "N"]
        )

    def test_options_str(self):
        prompt = Cli_Prompt(
            "Test prompt",
            (
                Cli_Choice("choice 1", ("1", "Y")),
                Cli_Choice("choice 2", ("2", "N")),
            )
        )

        self.assertEqual(
            prompt.get_options_str(),
            "( 1 | Y ) choice 1\n( 2 | N ) choice 2"
        )

    def test_options_str_collisions(self):
        with self.assertRaises(AttributeError):
            Cli_Prompt(
                "Test prompt",
                (
                    Cli_Choice("choice 1", ("1", "Y", "")),
                    Cli_Choice("choice 2", ("2", "N", "")),
                )
            )

        with self.assertRaises(AttributeError):
            Cli_Prompt(
                "Test prompt",
                (
                    Cli_Choice("choice 1", ("1",)),
                    Cli_Choice("choice 2", ("1",)),
                )
            )

    def test_ask(self):
        def input_generator():
            yield "e" # invalid choice
            yield "y"

        console = Mock_Console(input_generator())

        choice_1 = Cli_Choice("choice 1", ("1", "Y"))
        choice_2 = Cli_Choice("choice 2", ("2", "N"))
        prompt = Cli_Prompt(
            "Test prompt",
            (
                choice_1,
                choice_2,
            )
        )
        choice = prompt.ask(console)
        self.assertEqual(
            choice,
            choice_1
        )

        output = console.interpret_escape_sequences()
        self.assertEqual(
            output,
            "\n".join(
                (
                    prompt.prompt,
                    prompt.get_options_str(),
                    "Ok > y\n"
                )
            )
        )

