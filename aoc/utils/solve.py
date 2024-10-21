# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/benchmarks.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/generate_readme.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent


import importlib

from aoc.utils.parse_cli_args import parse_cli_args


def run_solution(year: int, day: int, part: int, language: str) -> None:
    # Import the solution module
    # from solutions.{year}.{language}.{day}{"a" if part == 1 else "b"} import solution

    module = importlib.import_module(
        f"aoc.{year}.{language}.{day}{"a" if part == 1 else "b"}"
    )

    # Download the puzzle input
    from aoc.utils.py.template import get_puzzle_input

    input = get_puzzle_input(year, day)
    answer = module.solution(input)
    print(f"Answer: {answer}")


def main() -> None:
    args = parse_cli_args()

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
