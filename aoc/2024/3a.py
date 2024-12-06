"""
Advent of Code 2024, Puzzle 3a: https://adventofcode.com/2024/day/3
"""

from dataclasses import dataclass
from re import Match, finditer
from typing import Iterator

from expression import pipe


@dataclass
class Instruction:
    raw: str
    left: int
    right: int


CorruptedMemory = str
Product = int
Answer = int


def find_uncorrupted_mul_instructions(corrupted_memory: CorruptedMemory) -> Iterator[Match[str]]:
    """Find all valid mul instructions in a possibly-corrupted memory string."""
    return finditer(r"mul\((\d{1,3}),(\d{1,3})\)", corrupted_memory)


def parse_mul_instruction_matches(instruction_matches: Iterator[Match[str]]) -> list[Instruction]:
    """Parse valid mul instructions so they can be executed."""
    return [Instruction(match.group(), int(match.group(1)), int(match.group(2))) for match in instruction_matches]


def execute_instructions(instructions: list[Instruction]) -> Answer:
    """Compute the sum of the products of each valid mul instruction."""
    return sum(instruction.left * instruction.right for instruction in instructions)


def solution(input: CorruptedMemory) -> Answer:
    return pipe(
        input,
        find_uncorrupted_mul_instructions,
        parse_mul_instruction_matches,
        execute_instructions,
    )


def test_solution() -> None:
    example_currupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    example_result = 161  # 2*4 + 5*5 + 11*8 + 8*5

    assert solution(example_currupted_memory) == example_result


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
