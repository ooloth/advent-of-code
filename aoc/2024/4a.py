"""Advent of Code 2024, Puzzle 4a: https://adventofcode.com/2024/day/4"""

from expression import pipe

WordSearch = str
Row = list[str]
Grid = list[Row]
XmasOccurrences = int


def parse_grid(input: WordSearch) -> Grid:
    """Parse word search multiline string into a 2D grid of characters."""
    return [[char for char in line] for line in input.splitlines()]


def spells_xmas(grid: Grid, x: int, y: int, dx: int, dy: int) -> bool:
    """Check if 'XMAS' occurs starting from (x, y) in the direction (dx, dy)."""
    s_would_be_outside_grid_horizontally = x + dx * 3 < 0 or x + dx * 3 >= len(grid[0])
    s_would_be_outside_grid_vertically = y + dy * 3 < 0 or y + dy * 3 >= len(grid)

    if s_would_be_outside_grid_horizontally or s_would_be_outside_grid_vertically:
        return False

    return (
        grid[y][x] == "X"
        and grid[y + dy][x + dx] == "M"
        and grid[y + dy * 2][x + dx * 2] == "A"
        and grid[y + dy * 3][x + dx * 3] == "S"
    )


def count_xmas_occurrences(grid: Grid) -> XmasOccurrences:
    """Count the number of times 'XMAS' occurs in a 2D grid of characters."""

    # Define directions as (dx, dy) tuples
    directions = [
        (0, -1),  # Up
        (1, -1),  # Up-right
        (1, 0),  # Right
        (1, 1),  # Down-right
        (0, 1),  # Down
        (-1, 1),  # Down-left
        (-1, 0),  # Left
        (-1, -1),  # Up-left
    ]

    row_count = len(grid)
    col_count = len(grid[0])
    xmas_count = 0

    for y in range(row_count):
        for x in range(col_count):
            if grid[y][x] == "X":
                for dx, dy in directions:
                    if spells_xmas(grid, x, y, dx, dy):
                        xmas_count += 1

    return xmas_count


def solution(input: WordSearch) -> XmasOccurrences:
    return pipe(
        input,
        parse_grid,
        count_xmas_occurrences,
    )


def test_solution() -> None:
    example_input: WordSearch = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    example_answer: XmasOccurrences = 18

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
