"""Advent of Code 2024, Puzzle 5b: https://adventofcode.com/2024/day/5"""

PageOrderingRulesAndPageNumbersInEachUpdate = str
PageOrderingRules = dict[str, list[str]]
PageNumbersInUpdate = list[str]
SumOfMiddlePageNumbersInReorderedUpdates = int


def parse_rules_and_updates(
    input: PageOrderingRulesAndPageNumbersInEachUpdate,
) -> tuple[PageOrderingRules, list[PageNumbersInUpdate]]:
    """Same as 5a."""
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
    """Same as 5a."""
    for i, page in enumerate(update):
        for page_that_must_come_after in rules.get(page, []):
            if page_that_must_come_after in update[:i]:
                return False
    return True


def reorder_update(update: PageNumbersInUpdate, rules: PageOrderingRules) -> PageNumbersInUpdate:
    """Reorder the update so that all pages that must come after a page come after it."""
    reordered_update: PageNumbersInUpdate = update

    for i, page in enumerate(update):
        for page_that_must_come_after in rules.get(page, []):
            if page_that_must_come_after in update[:i]:
                reordered_update.remove(page_that_must_come_after)
                reordered_update.append(page_that_must_come_after)

    assert len(reordered_update) == len(update), "Reordering should not change the number of pages"

    if not is_correctly_ordered(reordered_update, rules):
        return reorder_update(reordered_update, rules)

    return reordered_update


def middle_page_number(update: PageNumbersInUpdate) -> int:
    """Same as 5a."""
    return int(update[len(update) // 2])


def solution(input: PageOrderingRulesAndPageNumbersInEachUpdate) -> SumOfMiddlePageNumbersInReorderedUpdates:
    rules, updates = parse_rules_and_updates(input)

    return sum(
        middle_page_number(reorder_update(update, rules))
        for update in updates
        if not is_correctly_ordered(update, rules)
    )


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
    example_answer: SumOfMiddlePageNumbersInReorderedUpdates = 123

    assert solution(example_input) == example_answer


if __name__ == "__main__":
    import sys

    # Pass the CLI input string to the solution and print the result to stdout for bin/run to capture
    print(solution(sys.argv[1]))
