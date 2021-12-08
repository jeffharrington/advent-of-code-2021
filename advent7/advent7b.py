#
# Day 7: The Treachery of Whales
# https://adventofcode.com/2021/day/7
#
from collections import defaultdict
from typing import List


def parse_line(line: str) -> List[int]:
    num_str_list = line.rstrip().split(",")
    return [int(c) for c in num_str_list]


def summation(target: int) -> int:
    return sum([i for i in range(1, target + 1)])


def calculate(lines: list[str]) -> int:
    positions = parse_line(lines[0])
    min_fuel_costs = defaultdict(int)
    max_position = max(positions)
    for i in range(len(positions)):
        for j in range(max_position):
            num_moves = abs(positions[i] - j)
            min_fuel_costs[j] += summation(num_moves)
    return min(min_fuel_costs.values())


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    fuel_cost = calculate(lines=lines)
    print(f"There minimum fuel cost is {fuel_cost}.")
