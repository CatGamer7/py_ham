from unittest import TestCase

from core.parser.simple_scanner import Simple_Scanner
from core.model import Attacker, Defender
from core.model.value import (
    Random_Value,
    Positive_Value,
    Non_Positive_Value,
    Not_Assigned_Value
)

from .mock_console import Mock_Console


class Test_Simple_Scanner(TestCase):

    def test_scan_attacker(self):
        attacker_actual = Attacker(
            Random_Value(6),
            Not_Assigned_Value(),
            Positive_Value(4),
            Non_Positive_Value(0),
            Positive_Value(1)
        )

        def input_generator():
            yield "d6"
            yield "n/a"
            yield "4"
            yield "0"
            yield "1"

        console = Mock_Console(input_generator())
        scanner = Simple_Scanner(console)

        attacker_scanned = scanner.scan_attacker_input()
        final_output = console.interpret_escape_sequences()
        
        self.assertEqual(
            attacker_actual,
            attacker_scanned
        )
        self.assertEqual(
            "Please, input attacker below:\n\n" + "Status: ok\n" + \
                str(attacker_actual),
            final_output
        )

    def test_scan_attacker_attempts(self):
        attacker_actual = Attacker(
            Positive_Value(4),
            Positive_Value(4),
            Positive_Value(5),
            Non_Positive_Value(0),
            Positive_Value(1)
        )

        def input_generator():
            yield "4"
            yield "d6" # invalid skill
            yield "4"
            yield "5"
            yield "5" # invalid penetration
            yield "0"
            yield "1"

        console = Mock_Console(input_generator())
        scanner = Simple_Scanner(console)

        attacker_scanned = scanner.scan_attacker_input()
        final_output = console.interpret_escape_sequences()
        
        self.assertEqual(
            attacker_actual,
            attacker_scanned
        )
        self.assertEqual(
            "Please, input attacker below:\n\n" + "Status: ok\n" + \
                str(attacker_actual),
            final_output
        )

    def test_scan_defender(self):
        defender_actual = Defender(
            Positive_Value(3),
            Positive_Value(5),
            Not_Assigned_Value(),
            Not_Assigned_Value(),
        )

        def input_generator():
            yield "3"
            yield "5"
            yield ""
            yield "n/a"

        console = Mock_Console(input_generator())
        scanner = Simple_Scanner(console)

        defender_scanned = scanner.scan_defender_input()
        final_output = console.interpret_escape_sequences()
        
        self.assertEqual(
            defender_actual,
            defender_scanned
        )
        self.assertEqual(
            "Please, input defender below:\n\n" + "Status: ok\n" + \
                str(defender_actual),
            final_output
        )

    def test_scan_defender_attempts(self):
        defender_actual = Defender(
            Positive_Value(4),
            Positive_Value(3),
            Not_Assigned_Value(),
            Not_Assigned_Value(),
        )

        def input_generator():
            yield "d6" # wrong toughness
            yield "4"
            yield "3"
            yield ""
            yield "-5" # wrong feel_no_pain
            yield ""

        console = Mock_Console(input_generator())
        scanner = Simple_Scanner(console)

        defender_scanned = scanner.scan_defender_input()
        final_output = console.interpret_escape_sequences()
        
        self.assertEqual(
            defender_actual,
            defender_scanned
        )
        self.assertEqual(
            "Please, input defender below:\n\n" + "Status: ok\n" + \
                str(defender_actual),
            final_output
        )
