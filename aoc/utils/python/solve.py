import importlib
import subprocess
from pathlib import Path
from typing import Callable

from rich import print

from aoc.utils.python.cli import Day, Part, Year, parse_solve_cli_args
from aoc.utils.python.inputs import read_input_for_day

# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/runner.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/benchmarks.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/generate_readme.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/advent

Input = list[str]
Answer = int | None
Example = tuple[Input, int]

aoc_session_cookie_file = Path(".aoc-session-cookie").resolve()


def get_solution_function(year: Year, day: Day, part: Part) -> Callable:
    try:
        module_name = f"aoc.{year}.python.{day}{'a' if part == 1 else 'b'}"
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


def submit_answer(year: Year, day: Day, part: Part, answer: Answer) -> None:
    if not isinstance(answer, int):
        print("🤔 Solution is not an integer. Submission cancelled.")
        print(f"🔍 Answer: {answer}")
        return

    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#usage-%EF%B8%8F
    command = f"aoc s -y {year} -d {day} -s {aoc_session_cookie_file} {part} {answer}"

    try:
        subprocess.run(command.split(" "), check=True)
    except subprocess.CalledProcessError as e:
        print(f"🛑 Error submitting answer: {e}")
        exit(1)


def main() -> None:
    print("Running Python solution")
    args = parse_solve_cli_args()
    answer = get_answer(args.year, args.day, args.part)

    if args.submit:
        submit_answer(args.year, args.day, args.part, answer)
    else:
        print_answer(answer)


if __name__ == "__main__":
    main()
