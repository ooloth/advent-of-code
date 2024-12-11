"""Advent of Code 2024, Puzzle 9b: https://adventofcode.com/2024/day/9"""

from typing import Literal

from expression import pipe

from aoc.utils.logs import log

DiskMap = list[int | Literal["."]]
Span = tuple[int, int]
FileSystemChecksum = int


def parse_disk_map(input: str) -> DiskMap:
    """Same as 9a."""
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


def find_next_space_of_size(disk_map: DiskMap, size: int) -> Span:
    """
    Searching from the beginning, find the first free space sequence of the given size in the disk map by searching for
    consecutive "." characters.
    """
    start_index = -1
    end_index = -1

    for i in range(len(disk_map)):
        # Measure the length of the free space sequence
        if disk_map[i] == ".":
            if start_index == -1:
                start_index = i
                end_index = i
            else:
                end_index = i
            # Break if the free space sequence is the desired size
            if i - start_index + 1 == size:
                break

        # Reset the start and end indexes if a non-"." character is found
        if disk_map[i] != ".":
            start_index = -1
            end_index = -1

    return start_index, end_index


def find_next_file_before_index(disk_map: DiskMap, file_id: int) -> Span:
    """
    Searching backwards from the end, find the next file with the given ID, and return its start and end indexes.
    """
    start_index = -1
    end_index = -1

    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] == file_id:
            if end_index == -1:
                start_index = i
                end_index = i
            else:
                start_index = i
                if disk_map[start_index - 1] != file_id:
                    break

    return start_index, end_index


def compact_file_blocks(disk_map: DiskMap) -> DiskMap:
    """Move last file block to first free space until there are no gaps remaining between file blocks."""
    next_highest_file_id = 0

    # Find the highest file ID in the disk map
    for i in range(len(disk_map)):
        if disk_map[i] != ".":
            next_highest_file_id = max(next_highest_file_id, int(disk_map[i]))

    while next_highest_file_id >= 0:
        log(f"{next_highest_file_id=}")

        file_start, file_end = find_next_file_before_index(disk_map, next_highest_file_id)
        space_start, space_end = find_next_space_of_size(disk_map, file_end - file_start + 1)

        if any(i == -1 for i in [file_start, space_start, file_end, space_end]):
            next_highest_file_id -= 1
            continue

        if space_end > file_start:
            next_highest_file_id -= 1
            continue

        file_length = file_end - file_start + 1

        # Move last file block to first free space that will fit it
        disk_map[space_start : space_start + file_length] = disk_map[file_start : file_start + file_length]
        disk_map[file_start : file_start + file_length] = ["."] * file_length

        next_highest_file_id -= 1

    return disk_map


def multiply_block_ids_and_positions(disk_map: DiskMap) -> list[int]:
    """Same as 9a."""
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
    example_answer: FileSystemChecksum = 2858

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
