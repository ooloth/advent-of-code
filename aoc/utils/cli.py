from argparse import ArgumentParser, ArgumentTypeError, Namespace
from dataclasses import dataclass
from typing import Literal, cast

Year = Literal[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
Day = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Part = Literal[1, 2]
Language = Literal["python", "rust", "typescript"]


@dataclass
class PuzzleId:
    year: Year
    day: Day
    part: Part


def valid_year(value: str) -> Year:
    try:
        year = int(value)
    except ValueError:
        raise ArgumentTypeError(f'Year must be an integer (got "{value}")')
    if year not in range(2015, 2025):
        raise ArgumentTypeError(f'Year must be between 2015 and 2024 (got "{year}")')
    return cast(Year, year)


def valid_day(value: str) -> Day:
    try:
        day = int(value)
    except ValueError:
        raise ArgumentTypeError(f'Day must be an integer (got "{value}")')
    if day not in range(1, 26):
        raise ArgumentTypeError(f'Day must be between 1 and 25 (got "{day}")')
    return cast(Day, day)


def valid_part(value: str) -> Part:
    try:
        part = int(value)
    except ValueError:
        raise ArgumentTypeError(f'Part must be an integer (got "{value}")')
    if part not in [1, 2]:
        raise ArgumentTypeError(f"Part must be 1 or 2 (got {part})")
    return cast(Part, part)


def valid_puzzle_id(value: str) -> PuzzleId:
    """Validate a puzzle ID in the format 'year-day-part' (e.g. '2015-1-1')."""
    year, day, part = value.split("-")

    return PuzzleId(year=valid_year(year), day=valid_day(day), part=valid_part(part))


def parse_new_puzzle_cli_args() -> PuzzleId:
    parser = ArgumentParser(description="Download a puzzle description and its input and generate solution files.")

    parser.add_argument("puzzle_id", type=valid_puzzle_id, help='[YEAR]-[DAY]-[PART]: e.g. "2015-1-1", "2024-25-2"')

    args = parser.parse_args()

    return args.puzzle_id


def parse_solve_cli_args() -> Namespace:
    parser = ArgumentParser(description="Run a solution and optionally submit it.")

    parser.add_argument("puzzle_id", type=valid_puzzle_id, help='[YEAR]-[DAY]-[PART]: e.g. "2015-1-1", "2024-25-2"')
    parser.add_argument("-s", "--submit", action="store_true", help="Submit your answer to adventofcode.com")

    args = parser.parse_args()

    return Namespace(year=args.puzzle_id.year, day=args.puzzle_id.day, part=args.puzzle_id.part, submit=args.submit)
