"""Advent of Code 2024, Puzzle 9a: https://adventofcode.com/2024/day/9"""

from typing import Literal

from expression import pipe

DiskMap = list[int | Literal["."]]
FileSystemChecksum = int


def parse_disk_map(input: str) -> DiskMap:
    """
    Parse even indexes as files and odd indexes as free space. Represent files as their ID repeated in the same number
    of positions as their size. Represent free space as a "." repeated in the same number of positions as its size.
    """
    disk_map: DiskMap = []

    def file_block(index: int, char: str) -> list[int]:
        """Repeat the file's ID char times."""
        return [int(index / 2)] * int(char)

    def free_space(char: str) -> list[Literal["."]]:
        """Repeat "." char times."""
        return ["."] * int(char)

    for index, char in enumerate(input):
        if index % 2 == 0:
            disk_map += file_block(index, char)
        else:
            disk_map += free_space(char)

    return disk_map


def find_index_of_first_space(disk_map: DiskMap) -> int:
    return disk_map.index(".")


def find_index_of_last_file_block(disk_map: DiskMap) -> int:
    """Find the last file block in the disk map by searching from the end for a non-"." character."""
    for index, char in enumerate(reversed(disk_map)):
        if char != ".":
            return len(disk_map) - index - 1
    return -1


def compact_file_blocks(disk_map: DiskMap) -> DiskMap:
    """Move last file block to first free space until there are no gaps remaining between file blocks."""
    while True:
        first_space = find_index_of_first_space(disk_map)
        last_file_block = find_index_of_last_file_block(disk_map)

        if first_space == -1 or last_file_block == -1:
            break

        if first_space > last_file_block:
            break

        # Move last file block to first free space
        disk_map[first_space] = disk_map[last_file_block]
        disk_map[last_file_block] = "."

    return disk_map


def multiply_block_ids_and_positions(disk_map: DiskMap) -> list[int]:
    """Multiply the block ID by its position in the disk map to calculate the checksum components."""
    return [char * index for index, char in enumerate(disk_map) if char != "."]


def solution(input: str) -> FileSystemChecksum:
    return pipe(
        input,
        parse_disk_map,
        compact_file_blocks,
        multiply_block_ids_and_positions,
        sum,  # type: ignore
    )


def test_solution() -> None:
    example_input: str = """2333133121414131402"""
    example_answer: FileSystemChecksum = 1928

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
