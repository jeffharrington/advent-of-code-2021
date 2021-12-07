#
# Day 1: Sonar Sweep
# https://adventofcode.com/2021/day/1
#
SET_SIZE = 3


def calculate(lines: list[str]) -> int:
    prev_depth_set = [int(line) for line in lines[0:SET_SIZE]]
    prev_set_sum = sum(prev_depth_set)
    print(f"{prev_depth_set} - {prev_set_sum} - (N/A - no previous measurement)")
    num_depth_increases = 0
    i = 1  # Start on second set
    while i < len(lines):
        curr_depth_set = [int(line) for line in lines[i : (i + SET_SIZE)]]
        if len(curr_depth_set) < SET_SIZE:
            break
        curr_set_sum = sum(curr_depth_set)
        increased = curr_set_sum > prev_set_sum
        if increased:
            num_depth_increases += 1
        print(
            f"{curr_depth_set} - {curr_set_sum} - ({'increased' if increased else 'decreased'}) - {num_depth_increases}"
        )
        prev_depth_set = curr_depth_set
        prev_set_sum = curr_set_sum
        i += 1
    print(f"The depth increased {num_depth_increases} times.")
    return num_depth_increases


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
