from argparse import ArgumentParser, ArgumentTypeError, Namespace
from dataclasses import dataclass
from typing import Callable, Literal, cast

Year = Literal[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
Day = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Part = Literal[1, 2]
Language = Literal["python", "rust", "typescript"]


def validated_year(value: str) -> Year:
    year = int(value)
    if year not in range(2015, 2025):
        raise ArgumentTypeError(f"Year must be between 2015 and 2024, got {year}")
    return cast(Year, year)


def validated_day(value: str) -> Day:
    day = int(value)
    if day not in range(1, 26):
        raise ArgumentTypeError(f"Day must be between 1 and 25, got {day}")
    return cast(Day, day)


def validated_part(value: str) -> Part:
    part = int(value)
    if part not in [1, 2]:
        raise ArgumentTypeError(f"Part must be 1 or 2, got {part}")
    return cast(Part, part)


@dataclass
class CliOption:
    flag: str
    type: Callable
    help: str


def parse_scaffold_cli_args() -> Namespace:
    parser = ArgumentParser(description="Download puzzle and generate solution files.")

    options: list[CliOption] = [
        CliOption(flag="--year", type=validated_year, help="Year (2015 or later)"),
        CliOption(flag="--day", type=validated_day, help="Day (1-25)"),
        CliOption(flag="--part", type=validated_part, help="Part (1 or 2)"),
    ]

    for option in options:
        parser.add_argument(
            option.flag, type=option.type, required=True, help=option.help
        )

    return parser.parse_args()


def parse_solve_cli_args() -> Namespace:
    parser = ArgumentParser(description="Run a solution and optionally submit it.")

    options: list[CliOption] = [
        CliOption(flag="--year", type=validated_year, help="Year (2015 or later)"),
        CliOption(flag="--day", type=validated_day, help="Day (1-25)"),
        CliOption(flag="--part", type=validated_part, help="Part (1 or 2)"),
    ]

    for option in options:
        parser.add_argument(
            option.flag, type=option.type, required=True, help=option.help
        )

    return parser.parse_args()
