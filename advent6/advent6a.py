#
# Day 6: Lanternfish
# https://adventofcode.com/2021/day/6
#
from typing import List

REBORN_LIFE_TIMER = 6
NEWBORN_LIFE_TIMER = 8


def parse_line(line: str) -> List[int]:
    str_list = line.rstrip().split(",")
    return [int(c) for c in str_list]


def calculate(days: int, lines: list[str]) -> int:
    fish = parse_line(lines[0])
    for _ in range(days):
        new_fish = []
        for i, timer in enumerate(fish):
            if timer == 0:
                fish[i] = REBORN_LIFE_TIMER
                new_fish.append(NEWBORN_LIFE_TIMER)  # Add new fish
            else:
                fish[i] -= 1
        fish.extend(new_fish)
    return len(fish)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    DAYS = 80
    num_fish = calculate(lines=lines, days=DAYS)
    print(f"There are {num_fish} after {DAYS} days")
