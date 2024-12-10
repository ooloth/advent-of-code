"""Advent of Code 2024, Puzzle 8b: https://adventofcode.com/2024/day/8"""

from itertools import combinations

from expression import pipe

AntennaMap = list[list[str]]
Coordinates = tuple[int, int]
UniqueAntinodeLocationCount = int


def parse_map(input: str) -> AntennaMap:
    """Same as 8a."""
    return [[char for char in line] for line in input.splitlines()]


def find_locations_of_each_char(map: AntennaMap) -> dict[str, set[Coordinates]]:
    """Same as 8a."""
    char_coordinates: dict[str, set[Coordinates]] = {}

    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char != ".":
                char_coordinates.setdefault(str(char), set()).add((x, y))

    return char_coordinates


def is_out_of_bounds(x: int, y: int, map: AntennaMap) -> bool:
    """Same as 8a."""
    return x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)


def find_locations_of_each_antinode(char_locations: dict[str, set[Coordinates]], map: AntennaMap) -> set[Coordinates]:
    """Identify the coordinates of all antinodes in the map."""
    antinode_locations: set[Coordinates] = set()

    def repeat_until_out_of_bounds(x: int, y: int, dx: int, dy: int) -> set[Coordinates]:
        """Repeat a step until the next step is out of bounds."""
        coordinates: set[Coordinates] = set()

        while not is_out_of_bounds(x, y, map):
            x += dx
            y += dy
            coordinates.add((x - dx, y - dy))

        return coordinates

    for coordinates in char_locations.values():
        for (x1, y1), (x2, y2) in combinations(coordinates, 2):
            new_antinodes: list[Coordinates] = [
                (x1, y1),
                (x2, y2),
                *repeat_until_out_of_bounds(x1, y1, x1 - x2, y1 - y2),
                *repeat_until_out_of_bounds(x2, y2, x2 - x1, y2 - y1),
            ]

            for antinode in new_antinodes:
                x, y = antinode
                if not is_out_of_bounds(x, y, map):
                    antinode_locations.add(antinode)

    return antinode_locations


def locate_antinodes(map: AntennaMap) -> set[Coordinates]:
    """Same as 8a."""
    char_locations = find_locations_of_each_char(map)
    return find_locations_of_each_antinode(char_locations, map)


def solution(input: str) -> UniqueAntinodeLocationCount:
    return pipe(
        input,
        parse_map,
        locate_antinodes,
        len,
    )


def test_solution() -> None:
    example_input: str = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    example_answer: UniqueAntinodeLocationCount = 34

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
