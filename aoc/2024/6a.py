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


def walk_map(grid: Grid) -> Grid:
    """Walk the map and mark visited positions with 'X'."""
    updated_grid = grid.copy()

    def find_starting_position(grid: Grid) -> Position:
        """Find the starting position of the guard indicated by a Direction character."""
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char in "^>v<":
                    return x, y
        raise ValueError("Guard not found in map")

    def get_starting_direction(x: int, y: int) -> Direction:
        """Get the starting direction of the guard."""
        return cast(Direction, grid[y][x])

    def is_out_of_bounds(x: int, y: int) -> bool:
        """Check if a position is outside the grid."""
        return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

    def is_obstruction(x: int, y: int) -> bool:
        """Check if a position is an obstruction."""
        return grid[y][x] == "#"

    def move(x: int, y: int, direction: Direction) -> Position:
        """Move one step in the given direction and return the new position."""
        match direction:
            case "^":
                return x, y - 1
            case ">":
                return x + 1, y
            case "v":
                return x, y + 1
            case "<":
                return x - 1, y
            case _:
                raise ValueError(f"Invalid direction: {direction}")

    def turn_right(direction: Direction) -> Direction:
        """Rotate the guard 90 degrees to the right."""
        match direction:
            case "^":
                return ">"
            case ">":
                return "v"
            case "v":
                return "<"
            case "<":
                return "^"
            case _:
                raise ValueError(f"Invalid direction: {direction}")

    def mark_visited(x: int, y: int) -> None:
        """Mark a position as visited with an 'X'."""
        grid[y][x] = "X"

    x, y = find_starting_position(grid)
    direction = get_starting_direction(x, y)
    mark_visited(x, y)

    while True:
        if is_out_of_bounds(*move(x, y, direction)):
            break

        if is_obstruction(*move(x, y, direction)):
            direction = turn_right(direction)
            continue

        x, y = move(x, y, direction)
        mark_visited(x, y)

    return updated_grid


def count_x_in_map(grid: Grid) -> VisitedPositionsCount:
    """Count grid cells marked 'X'."""
    return sum(row.count("X") for row in grid)


def solution(input: Map) -> VisitedPositionsCount:
    return pipe(
        input,
        parse_map,
        walk_map,
        count_x_in_map,
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
