#
# Day 10: Syntax Scoring
# https://adventofcode.com/2021/day/10
#
from typing import List


def parse_line(line: str) -> List[str]:
    return [c for c in line.rstrip()]


CHAR_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

CHAR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def calculate(lines: list[str]) -> int:
    illegal_chars = []
    for line in lines:
        characters = parse_line(line)
        stack = list()
        for c in characters:
            if c in CHAR_MAP.values():  # is open char
                stack.append(c)
            elif c in CHAR_MAP.keys():  # is close char
                if not stack:
                    illegal_chars.append(c)
                    break
                last_char = stack.pop()
                if CHAR_MAP[c] != last_char:
                    illegal_chars.append(c)
                    break
    # Calculate score of illegal chars found
    score = 0
    for c in illegal_chars:
        score += CHAR_SCORES[c]

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
