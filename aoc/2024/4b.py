"""
Advent of Code 2024, Puzzle 4b: https://adventofcode.com/2024/day/4
"""

from expression import pipe

WordSearch = str
Row = list[str]
Grid = list[Row]
CrossedMasOccurrences = int


def parse_grid(input: WordSearch) -> Grid:
    """Same as 4a."""
    return [[char for char in line] for line in input.splitlines()]


def is_mas_cross(grid: Grid, x: int, y: int) -> bool:
    """Check if a crossed 'MAS' occurs starting from an A at (x, y) in the direction (dx, dy)."""
    cross_would_be_outside_grid_horizontally = x == 0 or x == len(grid[0]) - 1
    cross_would_be_outside_grid_vertically = y == 0 or y == len(grid) - 1

    if cross_would_be_outside_grid_horizontally or cross_would_be_outside_grid_vertically:
        return False

    up_left = grid[y - 1][x - 1]
    up_right = grid[y - 1][x + 1]
    down_left = grid[y + 1][x - 1]
    down_right = grid[y + 1][x + 1]

    left_to_right_ms = (up_left == "M" and down_right == "S") or (up_left == "S" and down_right == "M")
    right_to_left_ms = (up_right == "M" and down_left == "S") or (up_right == "S" and down_left == "M")

    return grid[y][x] == "A" and left_to_right_ms and right_to_left_ms


def count_crossed_mas_occurrences(grid: Grid) -> CrossedMasOccurrences:
    """Count the number of times 'MAS' occurs in the shape of an X in a 2D grid of characters."""
    row_count = len(grid)
    col_count = len(grid[0])
    crossed_mas_count = 0

    for y in range(row_count):
        for x in range(col_count):
            if grid[y][x] == "A":
                if is_mas_cross(grid, x, y):
                    crossed_mas_count += 1

    return crossed_mas_count


def solution(input: WordSearch) -> CrossedMasOccurrences:
    return pipe(
        input,
        parse_grid,
        count_crossed_mas_occurrences,
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
    example_answer: CrossedMasOccurrences = 9

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
