def calculate(lines: list[str]):
    horizontal = 0
    depth = 0
    for line in lines:
        command, value = line.split()
        if command == "forward":
            horizontal += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)
    print(f"Position is {horizontal} & {depth} ({horizontal * depth})")
    return horizontal * depth


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
