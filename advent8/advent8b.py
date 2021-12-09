#
# Day 8: Seven Segment Search
# https://adventofcode.com/2021/day/8
#
from collections import defaultdict
from typing import Tuple, Dict, List

# { Number: Count of Segments }
NUM_LENGTHS = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}


def parse_line(line: str) -> Tuple[List[set], List[set]]:
    signal_patterns = list()
    output_values = list()
    signal_switch = True
    for pattern in line.rstrip().split():
        if pattern == "|":
            signal_switch = False
            continue
        if signal_switch:
            signal_patterns.append(set(pattern))
        else:
            output_values.append(set(pattern))
    return (signal_patterns, output_values)


def decipher_signal_patterns(signal_patterns: List[set]) -> Dict[str, int]:
    patterns: Dict[int, set] = defaultdict(set)
    i = 0
    while len(patterns) < 10:  # Don't stop until we find all the patterns
        pattern = signal_patterns[i % len(signal_patterns)]
        i += 1
        if len(pattern) == NUM_LENGTHS[1]:
            patterns[1] = pattern
        elif len(pattern) == NUM_LENGTHS[4]:
            patterns[4] = pattern
        elif len(pattern) == NUM_LENGTHS[7]:
            patterns[7] = pattern
        elif len(pattern) == NUM_LENGTHS[8]:
            patterns[8] = pattern
        elif (
            len(pattern) == NUM_LENGTHS[3]
            and patterns[1]  # already found 1
            and patterns[1].issubset(pattern)
        ):
            patterns[3] = pattern
        elif (
            len(pattern) == NUM_LENGTHS[9]
            and patterns[4]  # already found 4
            and patterns[4].issubset(pattern)
        ):
            patterns[9] = pattern
        elif (
            len(pattern) == NUM_LENGTHS[0]
            and patterns[9]  # already found 9
            and patterns[1]  # already found 1
            and patterns[1].issubset(pattern)
        ):
            patterns[0] = pattern
        elif (
            len(pattern) == NUM_LENGTHS[6]
            and patterns[0]  # already found 0
            and patterns[9]  # already found 9
        ):
            patterns[6] = pattern
        elif (
            len(pattern) == NUM_LENGTHS[5]
            and patterns[9]  # already found 9
            and pattern.issubset(patterns[9])
        ):
            patterns[5] = pattern
        elif (
            len(pattern) == NUM_LENGTHS[2]
            and patterns[3]  # already found 3
            and patterns[5]  # already found 5
            and patterns[8]  # already found 8
            and pattern.issubset(patterns[8])
        ):
            patterns[2] = pattern
    return {
        "".join(sorted(pattern_set)): number for number, pattern_set in patterns.items()
    }


def decipher_output_values(
    output_values: List[set], pattern_table: Dict[str, int]
) -> int:
    value = ""
    for pattern in output_values:
        pattern_key = "".join(sorted(pattern))
        value += str(pattern_table[pattern_key])
    return int(value)


def calculate(lines: list[str]) -> int:
    values_sum = 0
    for line in lines:
        signal_patterns, output_values = parse_line(line)
        pattern_table = decipher_signal_patterns(signal_patterns)
        value = decipher_output_values(output_values, pattern_table)
        values_sum += value
    return values_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
