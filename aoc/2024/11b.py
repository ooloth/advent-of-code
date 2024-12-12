"""Advent of Code 2024, Puzzle 11b: https://adventofcode.com/2024/day/11"""

from collections import defaultdict
from functools import lru_cache

from expression import pipe

Stone = int
StoneCounts = dict[Stone, int]
TotalStoneCount = int


def parse_stone_counts(input: str) -> StoneCounts:
    """Parse space-separated string of stones into a dictionary of the counts of each stone."""
    stone_counts: StoneCounts = defaultdict(int)

    for stone in map(int, input.split()):
        stone_counts[stone] += 1

    return stone_counts


@lru_cache(maxsize=None)
def has_even_number_of_digits(stone: Stone) -> bool:
    """Same as 11a, with caching."""
    return len(str(stone)) % 2 == 0


@lru_cache(maxsize=None)
def split_into_two_stones(stone: Stone) -> tuple[Stone, Stone]:
    """Same as 11a, with caching."""
    stone_str = str(stone)
    half_length: int = len(stone_str) // 2

    return int(stone_str[:half_length]), int(stone_str[half_length:])


def blink(stone_counts: StoneCounts) -> StoneCounts:
    """Blink and apply the first matching rule, updating the count of each stone."""
    new_stones: StoneCounts = defaultdict(int)

    for stone, count in stone_counts.items():
        if stone == 0:
            new_stones[0] -= count
            new_stones[1] += count
        elif has_even_number_of_digits(stone):
            first_half, second_half = split_into_two_stones(stone)
            new_stones[stone] -= count
            new_stones[first_half] += count
            new_stones[second_half] += count
        else:
            new_stones[stone] -= count
            new_stones[stone * 2024] += count

    return new_stones


def blink_75_times(stone_counts: StoneCounts) -> StoneCounts:
    """Blink 75 times and return the cumulative updates to the counts of each stone."""
    for count in range(75):
        new_stone_counts = blink(stone_counts)
        for stone, count in new_stone_counts.items():
            stone_counts[stone] += count

    return stone_counts


def count_stones(stones: StoneCounts) -> int:
    """Count the total number of stones after 75 blinks."""
    return sum(stones.values())


def solution(input: str) -> TotalStoneCount:
    return pipe(
        input,
        parse_stone_counts,
        blink_75_times,
        count_stones,
    )


def test_solution() -> None:
    example_input: str = """125 17"""
    example_answer: TotalStoneCount = 55312

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
