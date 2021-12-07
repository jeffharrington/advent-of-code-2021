#
# Day 1: Sonar Sweep
# https://adventofcode.com/2021/day/1
#
def calculate(lines: list[str]):
    num_depth_increases = 0
    curr_depth = int(lines[0])
    print(f"{curr_depth} (N/A - no previous measurement)")
    for line in lines[1:]:
        depth = int(line)
        increased = depth > curr_depth
        if increased:
            num_depth_increases += 1
        print(f"{curr_depth} ({'increased' if increased else 'decreased'})")
        curr_depth = depth
    print(f"The depth increased {num_depth_increases} times.")
    return num_depth_increases


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
