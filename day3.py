import re

VALID_MULTS_RE = r"mul\(\d+,\d+\)"
VALS_TO_MULTIPLY_RE = r"\d+"


def get_sample_input():
    # return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def get_real_input():
    with open("day3_input.txt") as f:
        return f.read()
    

def part_1(puzzle_input):
    total = 0
    matches = re.findall(VALID_MULTS_RE, puzzle_input)
    for vals in matches:
        num1, num2 = re.findall(VALS_TO_MULTIPLY_RE, vals)
        total += int(num1) * int(num2)
    return total


def part_2(puzzle_input):
    donts = puzzle_input.split("don't")
    dos = [donts.pop(0)]

    for string in donts:
        new_list = string.split("do")
        if len(new_list) > 1:
            # print(new_list)
            mini_do_str = "".join(new_list[1:])
            dos.append(mini_do_str)
    # print(dos)

    do_str = "".join(dos)
    return(part_1(do_str))


def main():
    # puzzle_input = get_sample_input()
    puzzle_input = get_real_input()
    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


if __name__ == "__main__":
    main()