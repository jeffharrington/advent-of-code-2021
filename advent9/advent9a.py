#
# Day 9: Smoke Basin
# https://adventofcode.com/2021/day/9
#
from typing import Tuple, List


def parse_lines(lines: list[str]) -> List[list[int]]:
    heightmap: List[List[int]] = []
    for line in lines:
        heightmap.append([int(char) for char in line.rstrip()])
    return heightmap


def calculate(lines: list[str]) -> int:
    heightmap = parse_lines(lines=lines)
    height = len(heightmap)
    low_points = list()
    for i in range(height):
        width = len(heightmap[i])
        for j in range(width):
            curr_point = heightmap[i][j]
            if i > 0 and curr_point >= heightmap[i - 1][j]:  # top
                continue
            if j < (width - 1) and curr_point >= heightmap[i][j + 1]:  # right
                continue
            if i < (height - 1) and curr_point >= heightmap[i + 1][j]:  # bottom
                continue
            if j > 0 and curr_point >= heightmap[i][j - 1]:  # left
                continue
            # If we've gotten here, we've reached a low point
            low_points.append(curr_point)
    result = sum([(p + 1) for p in low_points])
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
