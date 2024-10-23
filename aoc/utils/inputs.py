from pathlib import Path


def _parse_input_file(path: Path) -> list[str]:
    """
    Strips trailing characters (e.g. newlines) from input file and returns it as list of strings.
    """
    with path.open() as file:
        # TODO: what if the input file is missing?
        return [line.rstrip() for line in file]


def get_input_for_day(year: int, day: int) -> list[str]:
    """
    Gets the input for the day from a local file and returns it as a list of strings.
    """
    input_file = Path(f"aoc/{year}/inputs/{day}.txt").resolve()
    return _parse_input_file(input_file)
