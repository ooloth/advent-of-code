# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/benchmarks.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/generate_readme.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent


import argparse
import importlib

from aoc.utils.inputs import get_input_for_day


def parse_solve_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download puzzle and create solution files from their templates."
    )
from rich import print

    parser.add_argument("--year", type=int, required=True, help="Year (2015 or later)")
    parser.add_argument("--day", type=int, required=True, help="Day (1-25)")
    parser.add_argument("--part", type=int, required=True, help="Part (1 or 2)")

    args = parser.parse_args()

    if args.year < 2015:
        raise ValueError("Year must be 2015 or later.")
    if args.day < 1 or args.day > 25:
        raise ValueError("Day must be between 1 and 25.")
    if args.part not in [1, 2]:
        raise ValueError("Part must be 1 or 2.")

    return args


def run_solution(year: int, day: int, part: int, language: str) -> None:
    solution_module = importlib.import_module(
        f"aoc.{year}.{language}.{day}{"a" if part == 1 else "b"}"
    )

    input = get_input_for_day(year, day)
    answer = solution_module.solution(input)
    print(f"Answer: {answer}")


def main() -> None:
    args = parse_solve_cli_args()

    run_solution(args.year, args.day, args.part, "python")


# def submit_solution(year: int, day: int) -> None:
#     # Import the solution module
#     module = importlib.import_module(f"aoc.solutions.y{year}.d{day:02}")
#     solution = module.Solution()

#     # Download the puzzle input
#     solution.download_input()

#     # Solve the puzzle
#     solution.solve()

#     # Submit the solution
#     solution.submit()

if __name__ == "__main__":
    main()
