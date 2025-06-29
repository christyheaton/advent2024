def get_sample_input() -> str:
    return """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""


def get_real_input() -> str:
    with open("day1_input.txt") as f:
        return f.read()
    

def prep_lists(puzzle_input: str) -> list:
    return [line.split() for line in puzzle_input.splitlines()]


def part_1(real_input: str) -> list:
    prelim_lists = prep_lists(real_input)
    sorted_first_list = sorted([int(val[0]) for val in prelim_lists])
    sorted_second_list = sorted([int(val[1]) for val in prelim_lists])
    result = 0
    for i, item in enumerate(sorted_first_list):
        difference = abs(item - sorted_second_list[i])
        result += difference
    return result


def part_2(real_input: str) -> list:
    prelim_lists = prep_lists(real_input)
    first_list = [int(val[0]) for val in prelim_lists]
    second_list = [int(val[1]) for val in prelim_lists]
    result = 0
    for item in first_list:
        result += second_list.count(item) * item
    return result


def main() -> None:
    # sample_input = get_sample_input()
    real_input = get_real_input()
    print(part_1(real_input))
    print(part_2(real_input))


if __name__ == "__main__":
    main()