"""Advent of Code 2024, Puzzle 6b: https://adventofcode.com/2024/day/6"""

from typing import Literal, cast

from expression import pipe

Map = str
Grid = list[list[str]]
Obstruction = "#"
Position = tuple[int, int]
ObstructionOptionCount = int

Up = Literal["^"]
Right = Literal[">"]
Down = Literal["v"]
Left = Literal["<"]
Direction = Up | Right | Down | Left


def parse_map(input: Map) -> Grid:
    """Same as 6a."""
    return [[char for char in line] for line in input.splitlines()]


def find_starting_position(grid: Grid) -> Position:
    """Same as 6a."""
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in "^>v<":
                return x, y
    raise ValueError("Guard not found in map")


def get_starting_direction(x: int, y: int, grid: Grid) -> Direction:
    """Same as 6a."""
    return cast(Direction, grid[y][x])


def is_out_of_bounds(x: int, y: int, grid: Grid) -> bool:
    """Same as 6a."""
    return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)


def is_obstruction(x: int, y: int, grid: Grid) -> bool:
    """Same as 6a."""
    return grid[y][x] == "#"


def move(x: int, y: int, direction: Direction) -> Position:
    """Same as 6a."""
    return {
        "^": (x, y - 1),
        ">": (x + 1, y),
        "v": (x, y + 1),
        "<": (x - 1, y),
    }[direction]


def turn_right(direction: Direction) -> Direction:
    """Same as 6a."""
    new_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}[direction]
    return cast(Direction, new_direction)


def detect_infinite_loop(grid: Grid) -> bool:
    """Detect if the guard is caught in an infinite loop."""
    x, y = find_starting_position(grid)
    direction = get_starting_direction(x, y, grid)
    visited: set[tuple[Position, Direction]] = set()

    while True:
        # If the guard has visited this position and direction before, he's in an infinite loop
        if ((x, y), direction) in visited:
            return True

        visited.add(((x, y), direction))

        # If the guard will escape the grid on his next move, he's not in an infinite loop
        if is_out_of_bounds(*move(x, y, direction), grid):
            return False

        if is_obstruction(*move(x, y, direction), grid):
            direction = turn_right(direction)
            continue

        x, y = move(x, y, direction)


def count_obstructions_that_create_an_infinite_loop(grid: Grid) -> ObstructionOptionCount:
    """Count the number of positions where adding an obstruction causes the guard to be in an infinite loop."""
    infinite_loop_count = 0

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == ".":
                grid[y][x] = "#"
                if detect_infinite_loop(grid):
                    infinite_loop_count += 1
                grid[y][x] = "."

    return infinite_loop_count


def solution(input: Map) -> ObstructionOptionCount:
    return pipe(
        input,
        parse_map,
        count_obstructions_that_create_an_infinite_loop,
    )


def test_solution() -> None:
    example_input: Map = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    example_answer: ObstructionOptionCount = 6

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
