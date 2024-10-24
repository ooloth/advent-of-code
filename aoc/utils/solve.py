import importlib
from typing import Callable

from rich import print

from aoc.utils.cli import Day, Language, Part, Year, parse_solve_cli_args
from aoc.utils.inputs import read_input_for_day

# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/benchmarks.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/generate_readme.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent

Input = list[str]
Answer = int | None
Example = tuple[Input, int]


def get_solution_function(year: Year, day: Day, part: Part, language: Language) -> Callable:
    try:
        module_name = f"aoc.{year}.{language}.{day}{'a' if part == 1 else 'b'}"
        solution_module = importlib.import_module(module_name)
        solution_function = getattr(solution_module, "solution")
        return solution_function
    except ModuleNotFoundError:
        raise ImportError(f"Module {module_name} not found.")
    except AttributeError:
        raise ImportError(f"Function 'solution' not found in module {module_name}.")


def calculate_answer(year: Year, day: Day, part: Part, language: Language) -> Answer:
    """TODO: handle solution module not found, function not found, etc."""
    solution = get_solution_function(year, day, part, language)
    input = read_input_for_day(year, day)
    # print(input)
    answer = solution(input)
    return answer


def print_answer(answer: Answer) -> None:
    if not isinstance(answer, int):
        print("Solution not yet implemented.")

    print(f"Answer: {answer}")


def submit_answer(answer: Answer) -> None:
    if not isinstance(answer, int):
        print("Solution not yet implemented. Submission cancelled.")
        print(f"Answer: {answer}")
        return

    print(f"Submitting answer: {answer}")
    print("TODO: Implement submit_answer")


def main() -> None:
    args = parse_solve_cli_args()
    answer = calculate_answer(args.year, args.day, args.part, "python")

    if args.submit:
        submit_answer(answer)
    else:
        print_answer(answer)


if __name__ == "__main__":
    main()
