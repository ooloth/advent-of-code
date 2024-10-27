from argparse import ArgumentParser, Namespace
from typing import Literal, cast

Year = Literal[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
Day = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Part = Literal["a", "b"]


def parse_cli_args() -> Namespace:
    parser = ArgumentParser(description="Download a puzzle description and its input and generate solution files.")

    # NOTE: validation of each arg is done at the shell script level (so it applies to all languages)
    parser.add_argument("year", type=int, help="2015-2024")
    parser.add_argument("day", type=int, help="1-25")
    parser.add_argument("part", type=str, help='"a" or "b"')

    args = parser.parse_args()

    return Namespace(
        year=cast(Year, args.year),
        day=cast(Day, args.day),
        part=cast(Part, args.part),
    )


# def parse_puzzle_input_from_cli_arg() -> str:
#     parser = ArgumentParser(description="Pass puzzle input to a solution file as a string.")

#     # NOTE: validation of each arg is done at the shell script level (so it applies to all languages)
#     parser.add_argument("input", type=str)

#     args = parser.parse_args()

#     return args.input
