"""
Advent of Code 2024, Puzzle 5a: https://adventofcode.com/2024/day/5
"""

PageOrderingRulesAndPageNumbersInEachUpdate = str
PageOrderingRules = dict[str, list[str]]
PageNumbersInUpdate = list[str]
SumOfMiddlePageNumbersInCorrectlyOrderedUpdates = int


def parse_rules_and_updates(
    input: PageOrderingRulesAndPageNumbersInEachUpdate,
) -> tuple[PageOrderingRules, list[PageNumbersInUpdate]]:
    rules: PageOrderingRules = {}
    updates: list[PageNumbersInUpdate] = []

    parse_line_as = "rule"

    for line in input.splitlines():
        if line == "":
            parse_line_as = "update"
            continue

        if parse_line_as == "rule":
            preceding, following = line.split("|")
            rules.setdefault(preceding, []).append(following)
        elif parse_line_as == "update":
            updates.append(line.split(","))

    return rules, updates


def is_correctly_ordered(update: PageNumbersInUpdate, rules: PageOrderingRules) -> bool:
    """
    If an update includes a page number referenced by a rule, the rule page must come before it in the update
    (though not necessarily immediately before it).
    """
    for i in range(len(update)):
        current_page = update[i]
        for page_that_must_come_after in rules.get(current_page, []):
            if page_that_must_come_after in update[:i]:
                return False
    return True


def middle_page_number(update: PageNumbersInUpdate) -> int:
    return int(update[len(update) // 2])


def solution(input: PageOrderingRulesAndPageNumbersInEachUpdate) -> SumOfMiddlePageNumbersInCorrectlyOrderedUpdates:
    rules, updates = parse_rules_and_updates(input)

    return sum(middle_page_number(update) for update in updates if is_correctly_ordered(update, rules))


def test_solution() -> None:
    example_input: PageOrderingRulesAndPageNumbersInEachUpdate = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    example_answer: SumOfMiddlePageNumbersInCorrectlyOrderedUpdates = 143

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
