# TODO: https://github.com/wimglenn/advent-of-code-data
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/start
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/get_inputs.py
# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/add_day.py
# TODO: https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py
# TODO: https://github.com/AlexeSimon/adventofcode/blob/master/init.py
# TODO: https://github.com/Bogdanp/awesome-advent-of-code?tab=readme-ov-file#python
# TODO: https://chatgpt.com/c/670df45e-5354-800a-a1f9-d2be7d49f4ca
# TODO: https://github.com/caderek/aocrunner/blob/main/src/io/api.ts


import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path

aoc_session_cookie_file = Path(".aoc-session-cookie").resolve()


# def download_puzzle_data(
#     year: int,
#     day: int,
#     data_type: str,
#     session_file: Path = aoc_session_cookie_file,
# ) -> None:
#     if data_type not in ["puzzle", "input"]:
#         raise ValueError("data_type must be either 'puzzle' or 'input'")

#     file_extension = "md" if data_type == "puzzle" else "txt"
#     rel_path = f"solutions/{year}/{data_type}s/{day}.{file_extension}"
#     abs_path = Path(rel_path).resolve()

#     if abs_path.exists():
#         print(
#             f"🎅 Puzzle{f" {data_type}" if data_type == "input" else ""} found at '{rel_path}'"
#         )
#         return

#     # Ensure the file's parent directories exist
#     abs_path.parent.mkdir(parents=True, exist_ok=True)

#     # Construct the command based on the data type
#     command = f"aoc download --year {year} --day {day} --{data_type}-only --{data_type}-file {rel_path} --session-file {session_file}"

#     try:
#         subprocess.run(command.split(" "), check=True)
#         print(f"🎅 Saved {data_type} to '{rel_path}'")
#     except subprocess.CalledProcessError as e:
#         print(f"Error downloading {data_type}: {e}")
#         exit(1)


def download_puzzle_instructions(year: int, day: int) -> None:
    rel_path = f"solutions/{year}/puzzles/{day}.md"
    abs_path = Path(rel_path).resolve()

    if abs_path.exists():
        print(f"🎅 Found puzzle at '{rel_path}'")
        return

    # Ensure the file's parent directories exist
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle puzzle to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#usage-%EF%B8%8F
    command = f"aoc download --year {year} --day {day} --puzzle-only --puzzle-file {rel_path} --session-file {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
        print(f"🎅 Saved puzzle to '{rel_path}'")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading puzzle: {e}")
        exit(1)


def download_puzzle_input(year: int, day: int) -> None:
    rel_path = f"solutions/{year}/inputs/{day}.txt"
    abs_path = Path(rel_path).resolve()

    if abs_path.exists():
        print(f"🎅 Found input at '{rel_path}'")
        return

    # Ensure the file's parent directories exist
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle input to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#more-examples
    command = f"aoc download --year {year} --day {day} --input-only --input-file {rel_path} --session-file {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
        print(f"🎅 Saved input to '{rel_path}'")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading input: {e}")
        exit(1)


@dataclass
class Template:
    path: str
    extension: str


def create_solution_files(year: int, day: int, part: int) -> None:
    templates = [
        Template(path="templates/python.txt", extension="py"),
        Template(path="templates/rust.txt", extension="rs"),
        Template(path="templates/typescript.txt", extension="ts"),
    ]

    for template in templates:
        abs_path = Path(template.path).resolve()

        if not abs_path.exists():
            print(f"No template found at '{template.path}'")
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
            print(f"🎅 Found solution at '{rel_path_to_solution}'")
            continue

        # Ensure the file's parent directories exist
        abs_path_to_solution.parent.mkdir(parents=True, exist_ok=True)

        with open(abs_path_to_solution, "w") as file:
            file.write(content)

        print(f"🎅 Created solution file at '{rel_path_to_solution}'")


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

    # download_puzzle_data(args.year, args.day, "puzzle")
    # download_puzzle_data(args.year, args.day, "input")
    download_puzzle_instructions(args.year, args.day)
    download_puzzle_input(args.year, args.day)

    create_solution_files(args.year, args.day, args.part)


if __name__ == "__main__":
    main()
