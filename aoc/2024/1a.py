"""
Advent of Code 2024, Puzzle 1a: https://adventofcode.com/2024/day/1
"""


def solution(input: str) -> int:
    left_list: list[int] = []
    right_list: list[int] = []

    for line in input.splitlines():
        location_ids = [int(x) for x in line.split()]
        left_list.append(location_ids[0])
        right_list.append(location_ids[1])

    # pair smallest in each list, then second smallest, etc.
    pairs = zip(sorted(left_list), sorted(right_list))

    # compute distance between each pair (always positive)
    distances = [abs(x - y) for x, y in pairs]

    return sum(distances)


def test_solution() -> None:
    example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    example_answer = 11

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
