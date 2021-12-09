#
# Day 9: Smoke Basin
# https://adventofcode.com/2021/day/9
#
from typing import Tuple, List, Set


def parse_lines(lines: list[str]) -> List[list[int]]:
    heightmap: List[List[int]] = []
    for line in lines:
        heightmap.append([int(char) for char in line.rstrip()])
    return heightmap


def is_low_point(heightmap, i, j) -> bool:
    height = len(heightmap)
    width = len(heightmap[i])
    curr_point = heightmap[i][j]
    if i > 0 and curr_point >= heightmap[i - 1][j]:  # top
        return False
    if j < (width - 1) and curr_point >= heightmap[i][j + 1]:  # right
        return False
    if i < (height - 1) and curr_point >= heightmap[i + 1][j]:  # bottom
        return False
    if j > 0 and curr_point >= heightmap[i][j - 1]:  # left
        return False
    return True


def get_basin_values(heightmap, i, j, basin_values: Set[int]) -> Set[Tuple[int, int]]:
    height = len(heightmap)
    width = len(heightmap[0])

    if i >= height or j >= width:  # Reached edge
        return basin_values

    if (i, j) in basin_values:
        return basin_values

    basin_values.add((i, j))
    if heightmap[i][j] == 9:
        return basin_values
    if i > 0:
        top_value = heightmap[i - 1][j]
        if top_value != 9:
            basin_values = basin_values.union(
                get_basin_values(heightmap, i - 1, j, basin_values)
            )  # top
    if j < (width - 1):
        right_value = heightmap[i][j + 1]
        if right_value != 9:
            basin_values = basin_values.union(
                get_basin_values(heightmap, i, j + 1, basin_values)
            )  # right
    if i < (height - 1):
        bottom_value = heightmap[i + 1][j]
        if bottom_value != 9:
            basin_values = basin_values.union(
                get_basin_values(heightmap, i + 1, j, basin_values)
            )  # bottom
    if j > 0:
        left_value = heightmap[i][j - 1]
        if left_value != 9:
            basin_values = basin_values.union(
                get_basin_values(heightmap, i, j - 1, basin_values)
            )  # left
    return basin_values


def calculate(lines: list[str]) -> int:
    heightmap = parse_lines(lines=lines)
    height = len(heightmap)
    # Find Low Points
    low_points: List[tuple] = list()
    for i in range(height):
        width = len(heightmap[i])
        for j in range(width):
            if is_low_point(heightmap, i, j):
                low_points.append((i, j))
    # Find Basins
    basin_lengths = list()
    for low_point in low_points:
        basin_values = get_basin_values(heightmap, low_point[0], low_point[1], set())
        basin_lengths.append(len(basin_values))
    top_basin_lengths = sorted(basin_lengths)[-3:] # Top 3 largest
    result = top_basin_lengths[0] * top_basin_lengths[1] * top_basin_lengths[2]
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
