#
# Day 8: Seven Segment Search
# https://adventofcode.com/2021/day/8
#
from typing import Tuple

ACCEPTABLE_LENGTHS = [2, 3, 4, 7]


def parse_line(line: str) -> Tuple[list, list]:
    signal_patterns = list()
    output_values = list()
    signal_switch = True
    for pattern in line.rstrip().split():
        if pattern == "|":
            signal_switch = False
            continue
        if signal_switch:
            signal_patterns.append(pattern)
        else:
            output_values.append(pattern)
    return (signal_patterns, output_values)


def calculate(lines: list[str]) -> int:
    count = 0
    for line in lines:
        _, output_values = parse_line(line)
        for pattern in output_values:
            if len(pattern) in ACCEPTABLE_LENGTHS:
                count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
