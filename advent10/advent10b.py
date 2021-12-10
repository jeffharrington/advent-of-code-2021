#
# Day 10: Syntax Scoring
# https://adventofcode.com/2021/day/10
#
from typing import List


OPEN_CHAR_MAP = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
CLOSE_CHAR_MAP = {v: k for k, v in OPEN_CHAR_MAP.items()}

CHAR_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse_line(line: str) -> List[str]:
    return [c for c in line.rstrip()]


def calculate(lines: list[str]) -> int:
    scores = list()
    for line in lines:
        corrupted = False
        characters = parse_line(line)
        stack = list()
        for c in characters:
            if c in OPEN_CHAR_MAP.keys():  # is open char
                stack.append(c)
            elif c in CLOSE_CHAR_MAP.keys():  # is close char
                if not stack:
                    corrupted = True
                    break
                last_char = stack.pop()
                if CLOSE_CHAR_MAP[c] != last_char:
                    corrupted = True
                    break
        if corrupted:
            # Line is corrupted
            continue
        if not stack:
            # Line is valid
            continue
        # Determine correct closing characters in order
        closing_line: List[str] = list()
        for c in stack:
            closing_line.insert(0, OPEN_CHAR_MAP[c])
        # Calculate score for closing line
        score = 0
        for c in closing_line:
            score *= 5
            score += CHAR_SCORES[c]
        scores.append(score)
    scores.sort()
    middle_score = scores[int(len(scores) / 2)]
    return middle_score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines=lines)
    print("Result:", result)
