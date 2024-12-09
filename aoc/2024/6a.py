"""Advent of Code 2024, Puzzle 6a: https://adventofcode.com/2024/day/6"""

from typing import Literal, cast

from expression import pipe

Map = str
Grid = list[list[str]]
Obstruction = "#"
Position = tuple[int, int]
VisitedPositionsCount = int

Up = Literal["^"]
Right = Literal[">"]
Down = Literal["v"]
Left = Literal["<"]
Direction = Up | Right | Down | Left


def parse_map(input: Map) -> Grid:
    """Parse multiline string map into a 2D grid of positions."""
    return [[char for char in line] for line in input.splitlines()]


def find_starting_position(grid: Grid) -> Position:
    """Find the starting position of the guard indicated by a Direction character."""
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in "^>v<":
                return x, y
    raise ValueError("Guard not found in map")


def get_starting_direction(x: int, y: int, grid: Grid) -> Direction:
    """Get the starting direction of the guard."""
    return cast(Direction, grid[y][x])


def is_out_of_bounds(x: int, y: int, grid: Grid) -> bool:
    """Check if a position is outside the grid."""
    return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)


def is_obstruction(x: int, y: int, grid: Grid) -> bool:
    """Check if a position is an obstruction."""
    return grid[y][x] == "#"


def move(x: int, y: int, direction: Direction) -> Position:
    """Move one step in the given direction and return the new position."""
    return {
        "^": (x, y - 1),
        ">": (x + 1, y),
        "v": (x, y + 1),
        "<": (x - 1, y),
    }[direction]


def turn_right(direction: Direction) -> Direction:
    """Turn right from the given direction."""
    new_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}[direction]
    return cast(Direction, new_direction)


def walk_map_and_track_positions_visited(grid: Grid) -> set[Position]:
    """Walk the map and return the positions that were visited."""
    x, y = find_starting_position(grid)
    direction = get_starting_direction(x, y, grid)
    visited: set[Position] = set()

    while True:
        visited.add((x, y))

        next_position = move(x, y, direction)

        if is_out_of_bounds(*next_position, grid):
            break

        if is_obstruction(*next_position, grid):
            direction = turn_right(direction)
            continue

        x, y = move(x, y, direction)

    return visited


def solution(input: Map) -> VisitedPositionsCount:
    return pipe(
        input,
        parse_map,
        walk_map_and_track_positions_visited,
        len,
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
    example_answer: VisitedPositionsCount = 41

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
