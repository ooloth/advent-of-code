"""
Advent of Code 2024, Puzzle 3b: https://adventofcode.com/2024/day/3
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
ProductSum = int


def find_uncorrupted_mul_and_do_and_dont_instructions(corrupted_memory: CorruptedMemory) -> Iterator[Match[str]]:
    """
    Find all valid mul instructions in a possibly-corrupted memory string, along with the do and don't instructions
    that enable and disable them.
    """
    valid_mul_instruction = r"mul\((\d{1,3}),(\d{1,3})\)"
    do = r"do\(\)"
    dont = r"don't\(\)"

    return finditer(f"{do}|{dont}|{valid_mul_instruction}", corrupted_memory)


def keep_enabled_mul_instruction_matches(instruction_matches: Iterator[Match[str]]) -> Iterator[Match[str]]:
    """Remove mul instruction matches that disabled by a preceding don't() instruction."""
    multiplication_enabled = True

    for instruction_match in instruction_matches:
        instruction = instruction_match.group(0)

        match instruction:
            case "do()":
                multiplication_enabled = True
            case "don't()":
                multiplication_enabled = False
            case _ if instruction.startswith("mul") and multiplication_enabled:
                yield instruction_match


def parse_mul_instruction_matches(instruction_matches: Iterator[Match[str]]) -> list[Instruction]:
    """Parse mul instruction matches so they can be executed."""
    return [Instruction(match.group(), int(match.group(1)), int(match.group(2))) for match in instruction_matches]


def execute_instructions(instructions: list[Instruction]) -> ProductSum:
    """Compute the sum of the products of each valid mul instruction."""
    return sum(instruction.left * instruction.right for instruction in instructions)


def solution(input: CorruptedMemory) -> ProductSum:
    return pipe(
        input,
        find_uncorrupted_mul_and_do_and_dont_instructions,
        keep_enabled_mul_instruction_matches,
        parse_mul_instruction_matches,
        execute_instructions,
    )


def test_solution() -> None:
    example_currupted_memory: CorruptedMemory = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    example_product_sum: ProductSum = 48  # 2*4 + 8*5

    assert solution(example_currupted_memory) == example_product_sum


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
