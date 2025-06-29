def get_sample_input():
    return """7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9"""


def get_real_input():
    with open("day2_input.txt") as f:
        return f.read()


def prep_lists(puzzle_input: str) -> list:
    return [line.split() for line in puzzle_input.splitlines()]
    

def part_1(puzzle_input):
    results = []
    reports = prep_lists(puzzle_input)
    
    for report in reports:
        report = [int(x) for x in report]
        results.append(is_safe_part1(report))

    return results.count(True)


def is_safe_part1(report):
    """
    A report is safe if:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    safe_checks = []
    for i, _ in enumerate(report):
        if i == 0:
            continue
        if abs(report[i] - report[i-1]) < 1 or abs(report[i] - report[i-1]) > 3:
            return False
        if report[i] > report[i-1]:
            safe_checks.append("Increasing")
        if report[i] < report[i-1]:
            safe_checks.append("Decreasing")
    if len(set(safe_checks)) == 1:
        return True
    return False


def main():
    # puzzle_input = get_sample_input()
    puzzle_input = get_real_input()
    print(part_1(puzzle_input))


if __name__ == "__main__":
    main()