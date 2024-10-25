import os
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from dataclasses import dataclass
from datetime import datetime
from typing import Literal, cast

Year = Literal[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
Day = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Part = Literal["a", "b"]


@dataclass
class PuzzleId:
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
    if value not in ["a", "b"]:
        raise ArgumentTypeError(f'Part must be "a" or "b" (got "{value}")')
    return cast(Part, value)


def get_default_year() -> Year:
    """Return the most recent AOC year (i.e. the year with the most recent December)."""

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    most_recent_aoc_year = current_year if current_month >= 12 else current_year - 1

    return cast(Year, most_recent_aoc_year)


def get_active_year() -> Year:
    """Return the AOC year explicity set via AOC_YEAR, or the most recent year with puzzles."""

    explicit_year = os.getenv("AOC_YEAR")
    default_year = get_default_year()
    active_year = explicit_year if explicit_year else default_year

    return valid_year(str(active_year))


def valid_puzzle_id(value: str) -> PuzzleId:
    """Validate a puzzle ID in the format '<day><part>' (e.g. '1a')."""

    # Assume the last character represents the part (a or b) and everything before it represents the day (1-25)
    day, part = value[:-1], value[-1]

    return PuzzleId(day=valid_day(day), part=valid_part(part))


def parse_new_puzzle_cli_args() -> Namespace:
    parser = ArgumentParser(description="Download a puzzle description and its input and generate solution files.")

    parser.add_argument("puzzle_id", type=valid_puzzle_id, help='<day><part>: e.g. "1a", "25b"')

    args = parser.parse_args()

    return Namespace(year=get_active_year(), day=args.puzzle_id.day, part=args.puzzle_id.part)


def parse_solve_cli_args() -> Namespace:
    parser = ArgumentParser(description="Run a solution and optionally submit it.")

    parser.add_argument("puzzle_id", type=valid_puzzle_id, help='<day><part>: e.g. "1a", "25b"')

    args = parser.parse_args()

    return Namespace(year=get_active_year(), day=args.puzzle_id.day, part=args.puzzle_id.part)
