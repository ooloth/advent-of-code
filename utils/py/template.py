from pathlib import Path


def get_puzzle_input(year: int, day: int) -> str:
    """Used by the python template to automatically pass the input to the solution function."""
    input_file = Path(f"solutions/{year}/inputs/{day}.txt").resolve()

    # TODO: what if the input file is missing?
    with open(input_file) as f:
        return f.read().strip()
