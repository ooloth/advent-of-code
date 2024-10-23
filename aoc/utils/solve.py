import importlib

from rich import print

from aoc.utils.cli import Day, Language, Part, Year, parse_solve_cli_args
from aoc.utils.inputs import read_input_for_day



def run_solution(year: int, day: int, part: int, language: str) -> None:
    solution_module = importlib.import_module(
        f"aoc.{year}.{language}.{day}{"a" if part == 1 else "b"}"
    )

    input = get_input_for_day(year, day)
    answer = solution_module.solution(input)
    print(f"Answer: {answer}")
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/benchmarks.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/generate_readme.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent


    input = read_input_for_day(year, day)


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
