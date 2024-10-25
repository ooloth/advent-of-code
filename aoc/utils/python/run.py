import importlib
from typing import Callable

from rich import print

from aoc.utils.python.cli import Day, Part, Year, parse_solve_cli_args
from aoc.utils.python.inputs import read_input_for_day

# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent

Input = list[str]
Answer = int | None
Example = tuple[Input, int]


def get_solution_function(year: Year, day: Day, part: Part) -> Callable:
    try:
        module_name = f"aoc.{year}.python.{day}{part}"
        solution_module = importlib.import_module(module_name)
        solution_function = getattr(solution_module, "solution")
        return solution_function
    except ModuleNotFoundError:
        raise ImportError(f"Module {module_name} not found.")
    except AttributeError:
        raise ImportError(f"Function 'solution' not found in module {module_name}.")


def get_answer(year: Year, day: Day, part: Part) -> Answer:
    """TODO: handle solution module not found, function not found, etc."""

    solution = get_solution_function(year, day, part)
    input = read_input_for_day(year, day)
    return solution(input)


def print_answer(answer: Answer) -> None:
    if not isinstance(answer, int):
        print("🤔 Solution is not an integer. Have you solved this puzzle?")

    print(f"🔍 Answer: {answer}")


def main() -> None:
    args = parse_solve_cli_args()
    answer = get_answer(args.year, args.day, args.part)
    print_answer(answer)


if __name__ == "__main__":
    main()
