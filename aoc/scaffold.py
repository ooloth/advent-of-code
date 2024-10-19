# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/start
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/get_inputs.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/add_day.py
# TODO: https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py
# TODO: https://github.com/AlexeSimon/adventofcode/blob/master/init.py
# TODO: https://github.com/Bogdanp/awesome-advent-of-code?tab=readme-ov-file#python
# TODO: download puzzle instructions for year-day-part (e.g. "instructions/1.py"). Or prepend to solution file as a comment?
# TODO: don't redownload files if they already exist

import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path

aoc_session_cookie_file = Path(".aoc-session-cookie").resolve()


def download_puzzle_instructions(year: int, day: int) -> None:
    rel_path = f"solutions/{year}/puzzles/{day}.md"
    abs_path = Path(rel_path).resolve()

    if abs_path.exists():
        print(f"Puzzle instructions already found at '{rel_path}'")
        return

    # Ensure the file's parent directories exist
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle puzzle to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#usage-%EF%B8%8F
    command = f"aoc download --year {year} --day {day} --puzzle-only --puzzle-file {rel_path} --session-file {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading puzzle: {e}")
        exit(1)


def download_puzzle_input(year: int, day: int) -> None:
    rel_path = f"solutions/{year}/inputs/{day}.txt"
    abs_path = Path(rel_path).resolve()

    if abs_path.exists():
        print(f"Puzzle input found at '{rel_path}'")
        return

    # Ensure the file's parent directories exist
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle input to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#more-examples
    command = f"aoc download --year {year} --day {day} --input-only --input-file {rel_path} --session-file {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading input: {e}")
        exit(1)


@dataclass
class Template:
    path: str
    extension: str


# TODO: repeat for rust and ts
def create_solution_files(year: int, day: int, part: int) -> None:
    templates = [
        Template(path="templates/python.txt", extension="py"),
        Template(path="templates/rust.txt", extension="rs"),
        Template(path="templates/typescript.txt", extension="ts"),
    ]

    for template in templates:
        abs_path = Path(template.path).resolve()

        if not abs_path.exists():
            print(f"Template file not found at '{template.path}'")
            continue

        with open(abs_path, "r") as file:
            content = file.read()

        content = content.replace("{year}", str(year))
        content = content.replace("{day}", str(day))
        content = content.replace("{part}", str(part))

        rel_path_to_solution = (
            f"solutions/{year}/{day}{'a' if part == 1 else 'b'}.{template.extension}"
        )
        abs_path_to_solution = Path(rel_path_to_solution).resolve()

        if abs_path_to_solution.exists():
            print(f"Puzzle solution found at '{rel_path_to_solution}'")
            continue

        # Ensure the file's parent directories exist
        abs_path_to_solution.parent.mkdir(parents=True, exist_ok=True)

        with open(abs_path_to_solution, "w") as file:
            file.write(content)

        print(f"Puzzle solution file created at '{rel_path_to_solution}'")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Python file with placeholders replaced."
    )
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

    download_puzzle_instructions(args.year, args.day)
    download_puzzle_input(args.year, args.day)
    create_solution_files(args.year, args.day, args.part)


if __name__ == "__main__":
    main()
