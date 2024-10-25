import subprocess
from pathlib import Path

from rich import print

from aoc.utils.python.cli import Day, Part, Year, parse_solve_cli_args
from aoc.utils.python.run import Answer, get_answer


def submit_answer(year: Year, day: Day, part: Part, answer: Answer) -> None:
    if not isinstance(answer, int):
        print("🤔 Solution is not an integer. Aborting.")
        print(f"🔍 Answer: {answer}")
        return

    aoc_session_cookie_file = Path(".aoc-session-cookie").resolve()

    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#usage-%EF%B8%8F
    command = f"aoc s -y {year} -d {day} -s {aoc_session_cookie_file} {part} {answer}"

    try:
        subprocess.run(command.split(" "), check=True)
    except subprocess.CalledProcessError as e:
        print(f"🛑 Error submitting answer: {e}")
        exit(1)


def main() -> None:
    args = parse_solve_cli_args()
    answer = get_answer(args.year, args.day, args.part)
    submit_answer(args.year, args.day, args.part, answer)


if __name__ == "__main__":
    main()
