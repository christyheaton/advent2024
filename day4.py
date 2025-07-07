import numpy as np

def get_sample_input() -> str:
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def get_real_input():
    with open("day4_input.txt") as f:
        return f.read()

def prep_input(puzzle_input):
    input_list = puzzle_input.split("\n")
    return [list(l) for l in input_list if l]


def part1(puzzle_input):
    matrix_list = prep_input(puzzle_input)
    matrix = np.array(matrix_list, dtype=str)

    xmas_count = 0

    for row in matrix:
        # Find instances in rows going forward
        xmas_count +="".join(row).count("XMAS")
        # Find instances in rows going backward
        xmas_count +="".join(row[::-1]).count("XMAS")

    for col in matrix.T:
        # Find instances in columns going forward
        xmas_count +="".join(col).count("XMAS")
        # Find instances in columns going backward
        xmas_count +="".join(col[::-1]).count("XMAS")

    rows, cols = matrix.shape
    for offset in range(-(rows - 1), cols):
        diagonal = np.diagonal(matrix, offset=offset)
        # Find instances in diagonals going from upper left to lower right
        xmas_count += "".join(diagonal).count("XMAS")
        # Find instances in diagonals going from lower right to upper left
        xmas_count += "".join(diagonal[::-1]).count("XMAS")

        flipped = np.fliplr(matrix)
        diagonal = np.diagonal(flipped, offset=offset)
        # Find instances in diagonals going from upper right to lower left
        xmas_count += "".join(diagonal).count("XMAS")
        # Find instances in diagonals going from lower left to upper right
        xmas_count += "".join(diagonal[::-1]).count("XMAS")

    return xmas_count


def main():
    # puzzle_input = get_sample_input()
    puzzle_input = get_real_input()
    print(part1(puzzle_input))


if __name__ == "__main__":
    main()