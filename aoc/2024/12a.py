"""Advent of Code 2024, Puzzle 12a: https://adventofcode.com/2024/day/12"""

from expression import pipe

from aoc.utils.logs import log

GardenPlot = str
GardenPlotMap = list[list[GardenPlot]]
TotalPriceOfRegionFences = int


def parse_garden_plot_map(input: str) -> GardenPlotMap:
    """Parse multiline string map into a 2D grid of garden plots."""
    log(f"{input=}")
    return [[plot for plot in line] for line in input.splitlines()]


def is_out_of_bounds(x: int, y: int, map: GardenPlotMap) -> bool:
    """Check if a position is outside the grid."""
    return x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)


def count_fences(map: GardenPlotMap) -> int:
    """Walk the map and count the number of edges where a plot is adjacent to a different plot."""
    log(f"{map=}")
    fence_count = 0

    for y in range(len(map)):
        for x in range(len(map[0])):
            plot = map[y][x]
            if x > 0 and plot != map[y][x - 1]:
                fence_count += 1
            if x < len(map) - 1 and plot != map[y][x + 1]:
                fence_count += 1
            if y > 0 and plot != map[y - 1][x]:
                fence_count += 1
            if y < len(map) - 1 and plot != map[y + 1][x]:
                fence_count += 1
            if x == len(map[0]) - 1 or x == 0:
                fence_count += 1
            if y == len(map) - 1 or y == 0:
                fence_count += 1

    return fence_count


def solution(input: str) -> TotalPriceOfRegionFences:
    return pipe(
        input,
        parse_garden_plot_map,
        count_fences,
        # len,
    )


def test_example_1() -> None:
    example_input_1: str = """AAAA
BBCD
BBCC
EEEC"""

    assert solution(example_input_1) == 140


def test_example_2() -> None:
    example_input_2: str = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

    assert solution(example_input_2) == 722


def test_example_3() -> None:
    example_input_3: str = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

    assert solution(example_input_3) == 1930


if __name__ == "__main__":
    import sys
    import time

    start_time = time.perf_counter()
    # Pass the CLI input string to the solution
    answer = solution(sys.argv[1])
    end_time = time.perf_counter()

    log(f"⏱️  Execution time: {(end_time - start_time) * 1000:.3f} ms")

    # Print the result to stdout for bin/run to capture
    print(answer)
