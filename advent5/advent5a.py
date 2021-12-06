#
# Day 5: Hydrothermal Venture
# https://adventofcode.com/2021/day/5
#
import re
from collections import defaultdict, namedtuple
from typing import List, Tuple, DefaultDict

LINE_PATTERN = r"^(\d.*),(\d.*) -> (\d.*),(\d.*).*$"

Point = namedtuple("Point", ["x", "y"])


def horizontal_locations_between_points(point1: Point, point2: Point) -> List[Point]:
    points: List[Point] = []
    x_moving_forward = (point1.x < point2.x)
    curr_x = point1.x
    while curr_x != point2.x:
        points.append(Point(x=curr_x, y=point1.y))
        curr_x += 1 if x_moving_forward else -1
    points.append(point2)
    return points

def vertical_locations_between_points(point1: Point, point2: Point) -> List[Point]:
    points: List[Point] = []
    y_moving_forward = (point1.y < point2.y)
    curr_y = point1.y
    while curr_y != point2.y:
        points.append(Point(x=point1.x, y=curr_y))
        curr_y += 1 if y_moving_forward else - 1
    points.append(point2)
    return points

def locations_between_two_points(point1: Point, point2: Point) -> List[Point]:
    points: List[Point] = []
    if (point1.x != point2.x) and (point1.y != point2.y):
        print("Non-straight line:", point1, point2)  # Moving diagonally
        return points
    #
    if point1.y == point2.y:
        # Moving horizontally
        points = horizontal_locations_between_points(point1, point2)
    elif point1.x == point2.x:
        # Moving vertically
        points = vertical_locations_between_points(point1, point2)

    return points


def parse_line(line: str) -> Tuple[Point, Point]:
    match = re.match(LINE_PATTERN, line)
    if not match:
        raise ValueError("No match on line:", line)
    point1 = Point(x=int(match.group(1)), y=int(match.group(2)))
    point2 = Point(x=int(match.group(3)), y=int(match.group(4)))
    return (point1, point2)


def calculate(lines: list[str]):
    ocean_map: DefaultDict[Point, int] = defaultdict(int)
    dangerous_points = set()
    for line in lines:
        point_pair = parse_line(line)
        locations = locations_between_two_points(point_pair[0], point_pair[1])
        for location in locations:
            ocean_map[location] += 1
            if ocean_map[location] >= 2:
                dangerous_points.add(location)
    print("Dangerous Points:", len(dangerous_points))
    return len(dangerous_points)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    calculate(lines)
