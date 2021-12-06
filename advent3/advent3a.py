from collections import defaultdict
from typing import DefaultDict


def calculate(lines: list[str]):
    position_sums: DefaultDict[int, int] = defaultdict(int)
    gamma_rate: DefaultDict[int, str] = defaultdict(str)
    epsilon_rate: DefaultDict[int, str] = defaultdict(str)

    num_lines = 0
    for line in lines:
        for i, bit in enumerate(line.rstrip()):
            position_sums[i] += int(bit)
            if position_sums[i] > int(num_lines / 2):
                gamma_rate[i] = "1"
                epsilon_rate[i] = "0"
            else:
                gamma_rate[i] = "0"
                epsilon_rate[i] = "1"
        num_lines += 1

    gamma_rate_str = "".join(gamma_rate.values())
    gamma_rate_int = int(gamma_rate_str, 2)
    print(f"Gamma Rate: {gamma_rate_str} ({gamma_rate_int})")

    epsilon_rate_str = "".join(epsilon_rate.values())
    epsilon_rate_int = int(epsilon_rate_str, 2)
    print(f"Epsilon Rate: {epsilon_rate_str} ({epsilon_rate_int})")

    result = gamma_rate_int * epsilon_rate_int
    print(f"Result: {result}")
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines)
