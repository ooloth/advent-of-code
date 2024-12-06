"""
Advent of Code 2024, Puzzle 1b: https://adventofcode.com/2024/day/1
"""


def solution(input: str) -> int:
    left_list: list[int] = []
    right_list: list[int] = []

    for line in input.splitlines():
        location_ids = [int(x) for x in line.split()]
        left_list.append(location_ids[0])
        right_list.append(location_ids[1])

    similarity_scores: list[int] = [x * right_list.count(x) for x in left_list]

    return sum(similarity_scores)


def test_solution() -> None:
    example_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    example_answer = 31

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
