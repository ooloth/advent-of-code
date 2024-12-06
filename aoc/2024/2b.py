"""
Advent of Code 2024, Puzzle 2b: https://adventofcode.com/2024/day/2
"""


def is_safe_report(report: list[int]) -> bool:
    """Same as 2a, but now we'll also pass it all report variants with one level removed."""
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False

    for index, level in enumerate(report):
        if index > 0:
            if abs(level - report[index - 1]) < 1 or abs(level - report[index - 1]) > 3:
                return False

    return True


def is_safe_report_with_one_level_removed(report: list[int]) -> bool:
    for index, _ in enumerate(report):
        report_with_level_removed = report[:index] + report[index + 1 :]
        if is_safe_report(report_with_level_removed):
            return True

    return False


def solution(input: str) -> int:
    safe_report_count = 0

    for line in input.splitlines():
        report = [int(x) for x in line.split()]
        if is_safe_report(report) or is_safe_report_with_one_level_removed(report):
            safe_report_count += 1

    return safe_report_count


def test_solution() -> None:
    example_reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    example_safe_report_count = 4

    assert solution(example_reports) == example_safe_report_count


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
