from typing import Generator


class Mock_File:

    def __init__(self, in_parent_console: "Mock_Console"):
        self.parent_console = in_parent_console

    def write(self, in_str: str):
        self.parent_console.buffer += in_str

    def flush(self):
        pass


class Mock_Console:

    buffer: str

    def __init__(self, input_generator: Generator):
        self.input_gen = input_generator
        self.buffer = ""
        self.file = Mock_File(self)

    def input(self):
        self.buffer += "\n"
        return next(self.input_gen)

    def print(self, in_str: str, end: str = "\n"):
        self.buffer += (in_str + end)

    # Interprets a single sequence \x1b[1A\x1b[2K that clears line above
    def interpret_escape_sequences(self) -> str:
        lines = self.buffer.split("\n")

        line_idx_to_drop = set()

        for i, line in enumerate(lines):
            # Check if the line is a drop line
            dropped_lines_count = line.count("\x1b[1A\x1b[2K")

            # Remove non-printable escape sequences
            if dropped_lines_count > 0:
                lines[i] = line.removeprefix(
                    "\x1b[1A\x1b[2K" * dropped_lines_count
                )

            # Drop up to dropped_lines_count lines before
            for j in range(dropped_lines_count):
                if i - j - 1 >= 0:
                    line_idx_to_drop.add(i - j - 1)

        # Construct a new str with only lines that were not dropped
        return "\n".join(
            [
                s for i, s in enumerate(lines) if i not in line_idx_to_drop
            ]
        )
