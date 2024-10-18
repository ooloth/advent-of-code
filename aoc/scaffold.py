# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/start
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/get_inputs.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/add_day.py
# TODO: https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py
# TODO: https://github.com/AlexeSimon/adventofcode/blob/master/init.py
# TODO: https://github.com/Bogdanp/awesome-advent-of-code?tab=readme-ov-file#python
# TODO: generate solution file for year-day-part (e.g. "1a.py")
# TODO: download puzzle input for year-day (e.g. "inputs/1.py")
# TODO: download example input for year-day-part? (e.g. "examples/1a.py")? Skip this and just copy examples from instructions manually?
# TODO: download puzzle instructions for year-day-part (e.g. "instructions/1.py"). Or prepend to solution file as a comment?
# TODO: don't redownload files if they already exist

import argparse
import subprocess
from pathlib import Path

cwd = Path(__file__).cwd()
python_template_path = f"{cwd}/templates/python.txt"


def download_puzzle_input(year: int, day: int) -> None:
    try:
        subprocess.run(
            ["aoc", "download", "--year", str(year), "--day", str(day)], check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error downloading puzzle input: {e}")
        exit(1)


def create_solution_file(year: int, day: int, part: int) -> None:
    with open(python_template_path, "r") as file:
        content = file.read()

    content = content.replace("{year}", str(year))
    content = content.replace("{day}", str(day))
    content = content.replace("{part}", str(part))

    output_file_path = f"{cwd}/solutions/{year}/{day}{'a' if part == 1 else 'b'}.py"
    with open(output_file_path, "w") as file:
        file.write(content)


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

    # Download the puzzle input
    # download_puzzle_input(args.year, args.day)

    # Generate solution file from template
    create_solution_file(args.year, args.day, args.part)


if __name__ == "__main__":
    main()
