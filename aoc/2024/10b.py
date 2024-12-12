"""Advent of Code 2024, Puzzle 10b: https://adventofcode.com/2024/day/10"""

from expression import pipe

TrailMap = list[list[int]]
Coordinates = tuple[int, int]
Path = tuple[Coordinates, ...]
SumOfTrailheadRatings = int


def parse_trail_map(input: str) -> TrailMap:
    """Same as 10a."""
    return [[int(num) for num in line] for line in input.splitlines()]


def is_out_of_bounds(x: int, y: int, map: TrailMap) -> bool:
    """Same as 10a."""
    return x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)


def walk_trail(
    map: TrailMap,
    x: int,
    y: int,
    height: int,
    path: Path,
) -> set[Path]:
    """Walk a hiking trail and return the number of distinct paths that can lead to all reachable 9-height points."""
    if is_out_of_bounds(x, y, map):
        return set()

    if map[y][x] != height:
        return set()

    path = path + ((x, y),)

    if height == 9:
        return {path}

    return {
        new_path  # completed path
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]  # each direction
        for new_path in walk_trail(map, x + dx, y + dy, height + 1, path)  # walk the trail
    }


def compute_trailhead_ratings(map: TrailMap) -> set[Path]:
    """Count the number of ways each 9-height position reachable from each 0-height trailhead can be reached."""
    return {
        path  # completed path
        for y in range(len(map))  # each row
        for x in range(len(map[0]))  # each position in the row
        if map[y][x] == 0  # if the position is a trailhead
        for path in walk_trail(map, x, y, 0, ())  # walk the trail
    }


def solution(input: str) -> SumOfTrailheadRatings:
    return pipe(
        input,
        parse_trail_map,
        compute_trailhead_ratings,
        len,
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
    example_answer: SumOfTrailheadRatings = 81

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
