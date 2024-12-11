"""Advent of Code 2024, Puzzle 10a: https://adventofcode.com/2024/day/10"""

from expression import pipe

TrailMap = list[list[int]]
Coordinates = tuple[int, int]
SumOfTrailheadScores = int


def parse_topographic_map(input: str) -> TrailMap:
    """Parse multiline string map into a 2D grid of hiking trails."""
    return [[int(num) for num in line] for line in input.splitlines()]


def is_out_of_bounds(x: int, y: int, map: TrailMap) -> bool:
    """Check if a position is outside the grid."""
    return x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)


def walk_trail(
    map: TrailMap,
    x: int,
    y: int,
    height: int,
    visited: set[Coordinates],
) -> int:
    """Walk a hiking trail and return the number of 9-height positions reachable from the trailhead."""
    if is_out_of_bounds(x, y, map):
        return 0

    if (x, y) in visited:
        return 0

    if map[y][x] != height:
        return 0

    visited.add((x, y))

    if height == 9:
        return 1

    return sum(walk_trail(map, x + dx, y + dy, height + 1, visited) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)])


def compute_trailhead_scores(map: TrailMap) -> list[int]:
    """Count the number of 9-height positions reachable from each 0-height trailhead."""
    return [walk_trail(map, x, y, 0, set()) for y in range(len(map)) for x in range(len(map[0]))]


def solution(input: str) -> SumOfTrailheadScores:
    return pipe(
        input,
        parse_topographic_map,
        compute_trailhead_scores,
        sum,  # type: ignore
    )


def test_solution() -> None:
    example_input: str = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    example_answer: SumOfTrailheadScores = 36

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
