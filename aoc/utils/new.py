import subprocess
from dataclasses import dataclass
from pathlib import Path

from rich import print

from aoc.utils.cli import Day, Part, Year, parse_new_puzzle_cli_args

# TODO: https://github.com/marcelblijleven/adventofcode/blob/master/src/adventofcode/scripts/add_day.py
# TODO: https://github.com/xavdid/advent-of-code-python-template/blob/main/start
# TODO: https://github.com/alvesvaren/AoC-template/blob/main/aoc/_api.py
# TODO: https://github.com/AlexeSimon/adventofcode/blob/master/init.py
# TODO: https://github.com/Bogdanp/awesome-advent-of-code?tab=readme-ov-file#python
# TODO: https://chatgpt.com/c/670df45e-5354-800a-a1f9-d2be7d49f4ca
# TODO: https://github.com/caderek/aocrunner/blob/main/src/io/api.ts


aoc_session_cookie_file = Path(".aoc-session-cookie").resolve()


def download_puzzle_instructions(year: Year, day: Day) -> None:
    rel_path = f"aoc/{year}/puzzles/{day}.md"
    abs_path = Path(rel_path).resolve()

    if abs_path.exists():
        print(f"🎅 Found puzzle at '{rel_path}'")
        return

    # Ensure the file's parent directories exist
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle puzzle to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#usage-%EF%B8%8F
    command = f"aoc d -y {year} -d {day} -P -p {rel_path} -s {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
        print(f"🎅 Saved puzzle to '{rel_path}'")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading puzzle: {e}")
        exit(1)


# TODO: make custom API request instead of using aoc-cli?
# TODO: attach my email address to the User-Agent header?
def download_puzzle_input(year: Year, day: Day) -> None:
    rel_path = f"aoc/{year}/inputs/{day}.txt"
    abs_path = Path(rel_path).resolve()

    if abs_path.exists():
        print(f"🎅 Found input at '{rel_path}'")
        return

    # Ensure the file's parent directories exist
    abs_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the puzzle input to the new file
    # see: https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#more-examples
    command = f"aoc d -y {year} -d {day} -I -i {rel_path} -s {aoc_session_cookie_file}"

    try:
        subprocess.run(command.split(" "), check=True)
        print(f"🎅 Saved input to '{rel_path}'")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading input: {e}")
        exit(1)


@dataclass
class Template:
    path: str
    lang: str
    ext: str


def create_solution_files(year: Year, day: Day, part: Part) -> None:
    templates = [
        Template(path="templates/python.txt", lang="python", ext="py"),
        Template(path="templates/rust.txt", lang="rust", ext="rs"),
        Template(path="templates/typescript.txt", lang="typescript", ext="ts"),
    ]

    for template in templates:
        abs_path_to_template = Path(template.path).resolve()

        if not abs_path_to_template.exists():
            print(f"No template found at '{template.path}'")
            continue

        with open(abs_path_to_template, "r") as file:
            content = file.read()

        # Replace placeholders with their values
        placeholders_and_values = {"{year}": year, "{day}": day, "{part}": part}
        for placeholder, value in placeholders_and_values.items():
            content = content.replace(placeholder, str(value))

        rel_path_to_solution = f"aoc/{year}/{template.lang}/{day}{"a" if part == 1 else "b"}.{template.ext}"
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
    args = parse_new_puzzle_cli_args()
    download_puzzle_instructions(args.year, args.day)
    download_puzzle_input(args.year, args.day)
    create_solution_files(args.year, args.day, args.part)


if __name__ == "__main__":
    main()
