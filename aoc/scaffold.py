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
from pathlib import Path

cwd = Path(__file__).cwd()

aoc_session_cookie_file = f"{cwd}/.aoc-session-cookie"
python_template_path = f"{cwd}/templates/python.txt"


def download_puzzle_input(year: int, day: int) -> None:
    input_file = f"{cwd}/solutions/{year}/inputs/{day}.txt"

    if Path(input_file).exists():
        print(f"Puzzle input for day {day} of {year} already exists at {input_file}.")
        return

    # Ensure the file's parent directories exist
    Path(input_file).parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle input to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#more-examples
    command = f"aoc download --year {year} --day {day} --input-only --input-file {input_file} --session-file {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading puzzle input: {e}")
        exit(1)


# TODO: repeat for rust and ts
def create_solution_file(year: int, day: int, part: int) -> None:
    with open(python_template_path, "r") as file:
        content = file.read()

    content = content.replace("{year}", str(year))
    content = content.replace("{day}", str(day))
    content = content.replace("{part}", str(part))

    output_file_path = f"{cwd}/solutions/{year}/{day}{'a' if part == 1 else 'b'}.py"
    with open(output_file_path, "w") as file:
        file.write(content)

    print(f"Solution file created at {output_file_path}")


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

    download_puzzle_input(args.year, args.day)
    create_solution_file(args.year, args.day, args.part)


if __name__ == "__main__":
    main()
