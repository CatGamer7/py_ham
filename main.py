from rich.console import Console

from core.parser.simple_scanner import Simple_Scanner

console = Console(highlight=False)
scanner = Simple_Scanner(console)
atkr = scanner.scan_defender_input()
pass
