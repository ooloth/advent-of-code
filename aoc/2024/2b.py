"""Advent of Code 2024, Puzzle 2b: https://adventofcode.com/2024/day/2"""

from expression import pipe

EngineerReports = str
Level = int
Report = list[Level]
SafeReportCount = int


def parse_engineer_reports(engineer_reports: EngineerReports) -> list[Report]:
    """Same as 2a"""
    return [[Level(level) for level in report.split()] for report in engineer_reports.splitlines()]


def is_safe(report: Report) -> bool:
    """Same as 2a"""
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
        if is_safe(report_with_level_removed):
            return True

    return False


def keep_safe_reports(reports: list[Report]) -> list[Report]:
    """Keep reports that are safe or can be made safe by removing one level."""
    return [report for report in reports if is_safe(report) or is_safe_report_with_one_level_removed(report)]


def solution(input: EngineerReports) -> int:
    return pipe(
        input,
        parse_engineer_reports,
        keep_safe_reports,
        len,
    )


def test_solution() -> None:
    example_reports: EngineerReports = """7 6 4 2 1
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
