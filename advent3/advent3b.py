#
# Day 3: Binary Diagnostic
# https://adventofcode.com/2021/day/3
#
from collections import defaultdict
from typing import DefaultDict


def calculate_rating(lines: list[str], target_most_common: bool) -> str:
    position_sums: DefaultDict[int, int] = defaultdict(int)  # [Position, Sum]
    candidates = lines.copy()
    num_positions = len(lines[0].rstrip())
    for position in range(num_positions):
        on_candidates = []
        off_candidates = []
        num_lines = 0
        for line in candidates:
            curr_bit = int(line.rstrip()[position])  # 0 or 1
            if curr_bit:
                on_candidates.append(line)  # Current bit is on
            else:
                off_candidates.append(line)  # Current bit is off
            position_sums[position] += curr_bit
            most_common_bit = position_sums[position] > int(num_lines / 2)
            num_lines += 1
        if most_common_bit:
            # If we are targeting the most common bit, use the "on" candidates
            candidates = on_candidates if target_most_common else off_candidates
        else:
            # If we are targeting the least common bit, use the "off" candidates
            candidates = off_candidates if target_most_common else on_candidates
        if len(candidates) == 1:
            break
    rating_str = candidates[0].rstrip()  # Last remaining candidate should be rating
    return rating_str


def calculate(lines: list[str]):
    o2_generator_rating_str = calculate_rating(lines, target_most_common=True)
    o2_generator_rating_int = int(o2_generator_rating_str, 2)
    print(f"o2_generator_rating: {o2_generator_rating_str} ({o2_generator_rating_int})")
    co2_scrubber_rating_str = calculate_rating(lines, target_most_common=False)
    co2_scrubber_rating_int = int(co2_scrubber_rating_str, 2)
    print(f"co2_scrubber_rating: {co2_scrubber_rating_str} ({co2_scrubber_rating_int})")
    product = o2_generator_rating_int * co2_scrubber_rating_int
    print(f"Product: {product}")
    return product


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines)
