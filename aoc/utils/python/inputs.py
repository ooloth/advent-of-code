from pathlib import Path

from aoc.utils.cli import Day, Year


def read_input_for_day(year: Year, day: Day) -> list[str]:
    """
    Gets the input for the day from a local file and returns it as a list of strings.
    Any trailing characters (e.g. newlines) are stripped from each line.
    """
    input_file = Path(f"aoc/{year}/inputs/{day}.txt").resolve()

    with input_file.open() as file:
        return [line.rstrip() for line in file]
