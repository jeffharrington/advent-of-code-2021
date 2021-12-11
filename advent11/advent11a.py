#
# Day 11: Dumbo Octopus
# https://adventofcode.com/2021/day/11
#
from typing import List

NUM_STEPS = 100


def parse_lines(lines: List[str]) -> List[List[int]]:
    matrix = list()
    for line in lines:
        matrix.append([int(char) for char in line.rstrip()])
    return matrix


def print_matrix(matrix: List[List[int]], step: int) -> None:
    print(f"Step {step}")
    print("-" * len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]}", end="")
        print("\n", end="")
    print("-" * len(matrix))


def flash(matrix: List[List[int]], i: int, j: int):
    matrix[i][j] = -9
    if (i - 1) >= 0:
        matrix[i - 1][j] += 1  # Flash above
    if (j - 1) >= 0:
        matrix[i][j - 1] += 1  # Flash left
    if (i + 1) < len(matrix):
        matrix[i + 1][j] += 1  # Flash below
    if (j + 1) < len(matrix):
        matrix[i][j + 1] += 1  # Flash right
    if (i - 1) >= 0 and (j - 1) >= 0:
        matrix[i - 1][j - 1] += 1  # Flash upper-left
    if (i - 1) >= 0 and (j + 1) < len(matrix):
        matrix[i - 1][j + 1] += 1  # Flash upper-right
    if (j - 1) >= 0 and (i + 1) < len(matrix):
        matrix[i + 1][j - 1] += 1  # Flash bottom-left
    if (j + 1) < len(matrix) and (i + 1) < len(matrix):
        matrix[i + 1][j + 1] += 1  # Flash bottom-right


def calculate(lines: list[str]) -> int:
    matrix = parse_lines(lines)
    num_flashes = 0
    for step in range(NUM_STEPS):
        print_matrix(matrix, step=step)
        # Increase everyone by 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += 1
        # Find the flashes and flash them
        check_for_flashes = True
        while check_for_flashes:
            check_for_flashes = False
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] > 9:
                        flash(matrix, i, j)
                        num_flashes += 1
                        check_for_flashes = True
        # Reset flashed circles
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    matrix[i][j] = 0
    return num_flashes


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
