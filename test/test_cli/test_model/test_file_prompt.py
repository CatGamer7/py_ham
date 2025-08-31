from unittest import TestCase

from cli.model import Cli_File_Prompt
from test.mock import Mock_Console


class Test_Cli_File_Prompt(TestCase):

    def test_ask(self):
        def input_generator():
            yield "lascannon.txt"

        console = Mock_Console(input_generator())

        prompt = Cli_File_Prompt()
        file_path = prompt.ask(console)
        self.assertEqual(
            file_path,
            "lascannon.txt"
        )

        output = console.interpret_escape_sequences()
        self.assertEqual(
            output,
            "Enter file path > \n" # Filename is absent due to the way 
            # file path input functions: retries are handled in Cli_cController
        )
