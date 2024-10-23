from argparse import ArgumentParser, ArgumentTypeError, Namespace
from typing import Literal, cast

Year = Literal[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
Day = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Part = Literal[1, 2]
Language = Literal["python", "rust", "typescript"]


def valid_year(value: str) -> Year:
    year = int(value)
    if year not in range(2015, 2025):
        raise ArgumentTypeError(f"Year must be between 2015 and 2024, got {year}")
    return cast(Year, year)


def valid_day(value: str) -> Day:
    day = int(value)
    if day not in range(1, 26):
        raise ArgumentTypeError(f"Day must be between 1 and 25, got {day}")
    return cast(Day, day)


def valid_part(value: str) -> Part:
    part = int(value)
    if part not in [1, 2]:
        raise ArgumentTypeError(f"Part must be 1 or 2, got {part}")
    return cast(Part, part)


def parse_scaffold_cli_args() -> Namespace:
    parser = ArgumentParser(description="Download puzzle and generate solution files.")

    parser.add_argument("--year", "-y", type=valid_year, help="Year (2015 or later)", required=True)
    parser.add_argument("--day", "-d", type=valid_day, help="Day (1-25)", required=True)
    parser.add_argument("--part", "-p", type=valid_part, help="Part (1 or 2)", required=True)

    return parser.parse_args()


def parse_solve_cli_args() -> Namespace:
    parser = ArgumentParser(description="Run a solution and optionally submit it.")

    parser.add_argument("--year", "-y", type=valid_year, help="Year (2015 or later)", required=True)
    parser.add_argument("--day", "-d", type=valid_day, help="Day (1-25)", required=True)
    parser.add_argument("--part", "-p", type=valid_part, help="Part (1 or 2)", required=True)
    parser.add_argument("--submit", "-s", action="store_true", help="Submit the solution")

    return parser.parse_args()
