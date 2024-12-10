"""Advent of Code 2024, Puzzle 7b: https://adventofcode.com/2024/day/7"""

from itertools import product

from expression import pipe

CalibrationEquationsWithNoOperators = str
ResultsAndEquationNumbers = dict[int, list[int]]
CalibrationResult = int
TotalCalibrationResult = int  # sum of test values from the equations that can be made true


def parse_input(input: str) -> ResultsAndEquationNumbers:
    """Same as 7a."""
    return {
        int(test_value): list(map(int, equation_numbers.split(" ")))  # 3
        for line in input.splitlines()  # 1
        for test_value, equation_numbers in [line.split(": ")]  # 2
    }


def can_add_or_multiply_to_target(target: int, numbers: list[int]) -> bool:
    """
    Return True if the numbers can be added or multiplied to the target, including when neighbouring
    numbers are concatenated.
    """
    operators = ["+", "*", "||"]
    possible_operator_sequences = product(operators, repeat=len(numbers) - 1)

    def concatenate(a: int, b: int) -> int:
        return int(str(a) + str(b))

    for operator_list in possible_operator_sequences:
        result = numbers[0]

        # Apply the operators to the numbers from left to right
        for operator, number in zip(operator_list, numbers[1:]):
            if operator == "+":
                result += number
            elif operator == "*":
                result *= number
            elif operator == "||":
                result = concatenate(result, number)

        if result == target:
            return True
    return False


def keep_solvable_equations(test_values_and_equations: ResultsAndEquationNumbers) -> list[CalibrationResult]:
    """Same as 7a."""
    return [
        value  # 3
        for value, equation_numbers in test_values_and_equations.items()  # 1
        if can_add_or_multiply_to_target(value, equation_numbers)  # 2
    ]


def solution(input: str) -> TotalCalibrationResult:
    return pipe(
        input,
        parse_input,
        keep_solvable_equations,
        sum,  # type: ignore
    )


def test_solution() -> None:
    example_input: str = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    example_answer: TotalCalibrationResult = 11387

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
