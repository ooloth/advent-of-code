"""
Advent of Code 2024, Puzzle 2a: https://adventofcode.com/2024/day/2
"""

from expression import pipe

EngineerReports = str
Level = int
Report = list[Level]
SafeReportCount = int


def parse_engineer_reports(engineer_reports: EngineerReports) -> list[Report]:
    """Transform the engineer's report into a list of parsed reports."""
    return [[Level(level) for level in report.split()] for report in engineer_reports.splitlines()]


def is_safe(report: Report) -> bool:
    """
    Are the report levels sorted (either asc or desc)?
    And are all adjacent levels exactly 1-3 steps apart?
    """
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False

    for index, level in enumerate(report):
        if index > 0:
            if abs(level - report[index - 1]) < 1 or abs(level - report[index - 1]) > 3:
                return False

    return True


def keep_safe_reports(reports: list[Report]) -> list[Report]:
    return [report for report in reports if is_safe(report)]


def solution(input: EngineerReports) -> SafeReportCount:
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
    example_safe_count: SafeReportCount = 2

    assert solution(example_reports) == example_safe_count


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
