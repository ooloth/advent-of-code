from pathlib import Path


def get_puzzle_input(year: int, day: int) -> str:
    input_file = f"{Path(__file__).cwd()}/solutions/{year}/inputs/{day}.txt"

    # TODO: if file is missing, create it?
    with open(input_file) as f:
        return f.read().strip()
