def calculate(lines: list[str]):
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        command, value = line.split()
        if command == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        elif command == "down":
            aim += int(value)
        elif command == "up":
            aim -= int(value)
        print(
            f"{command.ljust(7)} {value}\tHoriz: {horizontal}\tDepth: {depth}\tAim: {aim}"
        )

    print(f"Position is {horizontal} & {depth} with {aim} ({horizontal * depth})")
    return horizontal * depth


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
