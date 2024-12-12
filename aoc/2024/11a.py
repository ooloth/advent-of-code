"""Advent of Code 2024, Puzzle 11a: https://adventofcode.com/2024/day/11"""

from expression import pipe

Stone = int
NumberOfStonesAfter25Blinks = int


def parse_stones(input: str) -> list[Stone]:
    """Parse space-separated string of stones into a list of integers."""
    return [int(stone) for stone in input.split()]


def has_even_number_of_digits(stone: Stone) -> bool:
    """Check if a stone has an even number of digits."""
    return len(str(stone)) % 2 == 0


def split_into_two_stones(stone: Stone) -> tuple[Stone, Stone]:
    """Split digit in two halves and return both halves as a tuple with leading zeroes removed."""
    stone_str = str(stone)
    half_length: int = len(stone_str) // 2

    first_half: Stone = int(stone_str[0:half_length])
    second_half: Stone = int(stone_str[half_length : half_length * 2])

    return first_half, second_half


def blink(stones: list[Stone]) -> list[Stone]:
    """Blink and apply the first matching rule to each stone."""
    new_stones: list[Stone] = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        elif has_even_number_of_digits(stone):
            new_stones.extend(split_into_two_stones(stone))
            continue
        new_stones.append(stone * 2024)

    return new_stones


def blink_25_times(stones: list[Stone]) -> list[Stone]:
    """Blink 25 times and return the cumulative change to the stones."""
    for _ in range(25):
        stones = blink(stones)

    return stones


def solution(input: str) -> NumberOfStonesAfter25Blinks:
    return pipe(
        input,
        parse_stones,
        blink_25_times,
        len,
    )


def test_solution() -> None:
    example_input: str = """125 17"""
    example_answer: NumberOfStonesAfter25Blinks = 55312

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
