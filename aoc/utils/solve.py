import importlib
from typing import Callable

from rich import print

from aoc.utils.cli import Day, Language, Part, Year, parse_solve_cli_args
from aoc.utils.inputs import read_input_for_day

# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/benchmarks.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/generate_readme.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent


def get_solution_function(
    year: Year,
    day: Day,
    part: Part,
    language: Language,
) -> Callable:
    try:
        module_name = f"aoc.{year}.{language}.{day}{'a' if part == 1 else 'b'}"
        solution_module = importlib.import_module(module_name)
        solution_function = getattr(solution_module, "solution")
        return solution_function
    except ModuleNotFoundError:
        raise ImportError(f"Module {module_name} not found.")
    except AttributeError:
        raise ImportError(f"Function 'solution' not found in module {module_name}.")


def get_answer(year: Year, day: Day, part: Part, language: Language) -> int:
    solution_function = get_solution_function(year, day, part, language)
    input = read_input_for_day(year, day)
    # print(input)
    answer = solution_function(input)
    return answer


def main() -> None:
    args = parse_solve_cli_args()
    answer = get_answer(args.year, args.day, args.part, "python")
    print(f"Answer: {answer}")


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
