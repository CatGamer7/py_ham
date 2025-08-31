from unittest import TestCase

from cli import Cli_Controller
from cli.constants import WELCOME_MESSAGE, QUICK_REFERENCE, Cli_Prompt_Enum
from cli.model import Cli_Prompt
from test.mock import Mock_Console


class Test_Cli_Controller(TestCase):

    def test_run(self):
        def input_generator():
            yield "2" # print quick reference
            yield "e" # Invalid choice for calculator
            yield "2" # choose real calculator
            yield "n" # interactive attacker

            yield "12" # interactive attacker
            yield "3 r1" # interactive attacker
            yield "6" # interactive attacker
            yield "-1 +1" # interactive attacker
            yield "d6" # interactive attacker
            
            yield "2" # dont save
            yield "3" # load GEQ
            yield "n" # dont save

        console = Mock_Console(input_generator())

        ctr = Cli_Controller(console)
        ctr.startup()
        ctr.run_calculation_once()

        output = console.interpret_escape_sequences()
        self.assertEqual(
            output,
            WELCOME_MESSAGE + "\n\n" + \
            Test_Cli_Controller._prompt_enum_value_to_str(
                Cli_Prompt_Enum.STARTUP.value, "2"
            ) + \
            QUICK_REFERENCE + "\n\n" + \
            Test_Cli_Controller._prompt_enum_value_to_str(
                Cli_Prompt_Enum.CALCULATOR.value, "2"
            ) + "\n" + \
            Test_Cli_Controller._prompt_enum_value_to_str(
                Cli_Prompt_Enum.LOAD_ATKR.value, "n"
            ) + \
            "Please, input attacker below:\n\nStatus: ok\n" + \
            "     A     |     H     |     S     |     P     |     D     \n" + \
            "    12     |   3 r1    |     6     |   -1 +1   |    d6     \n" + \
            Test_Cli_Controller._prompt_enum_value_to_str(
                Cli_Prompt_Enum.SAVE.value, "2"
            ) + "\n" + \
            Test_Cli_Controller._prompt_enum_value_to_str(
                Cli_Prompt_Enum.LOAD_DEF.value, "3"
            ) + \
            "     T     |     S     |     I     |     F     \n" + \
            "     3     |     5     |    n/a    |    n/a    \n\n" + \
            Test_Cli_Controller._prompt_enum_value_to_str(
                Cli_Prompt_Enum.SAVE.value, "n"
            ) + "\n" + \
            "Expected number of wounds is: 27.222222\n\n"
        )

    @staticmethod
    def _prompt_enum_value_to_str(val: Cli_Prompt, ask_result: str) -> str:
        return val.prompt + "\n" + val.get_options_str() + \
        "\n" + "Ok > " + ask_result + "\n"
