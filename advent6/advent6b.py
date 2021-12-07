#
# Day 6: Lanternfish
# https://adventofcode.com/2021/day/6
#
from collections import Counter
from typing import List

REBORN_LIFE_TIMER = 6
NEWBORN_LIFE_TIMER = 8


def parse_line(line: str) -> List[int]:
    str_list = line.rstrip().split(",")
    return [int(c) for c in str_list]


def calculate(days: int, lines: list[str]) -> int:
    initial_state = parse_line(lines[0])
    fish_state = Counter(initial_state)
    for _ in range(days):
        reborn_fish: int = 0
        newborn_fish: int = 0
        for i in range(NEWBORN_LIFE_TIMER + 1):
            if i == 0:
                reborn_fish = fish_state[i]
                newborn_fish = fish_state[i]
            else:
                fish_state[i - 1] = fish_state[i]
        fish_state[REBORN_LIFE_TIMER] += reborn_fish
        fish_state[NEWBORN_LIFE_TIMER] = newborn_fish
    total_fish = sum([v for v in fish_state.values()])
    return total_fish


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    DAYS = 256
    num_fish = calculate(lines=lines, days=DAYS)
    print(f"There are {num_fish} fish after {DAYS} days")
