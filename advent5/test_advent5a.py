import unittest

from advent5a import (
    calculate,
    parse_line,
    locations_between_two_points,
    Point,
)


class Test5A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "0,9 -> 5,9\n",
            "8,0 -> 0,8\n",
            "9,4 -> 3,4\n",
            "2,2 -> 2,1\n",
            "7,0 -> 7,4\n",
            "6,4 -> 2,0\n",
            "0,9 -> 2,9\n",
            "3,4 -> 1,4\n",
            "0,0 -> 8,8\n",
            "5,5 -> 8,2\n",
        ]

    def test_locations_between_two_points(self):
        points = locations_between_two_points(Point(x=0, y=9), Point(x=5, y=9))
        self.assertEqual(
            points,
            [
                Point(x=0, y=9),
                Point(x=1, y=9),
                Point(x=2, y=9),
                Point(x=3, y=9),
                Point(x=4, y=9),
                Point(x=5, y=9),
            ],
        )
        #
        points = locations_between_two_points(Point(x=2, y=2), Point(x=2, y=1))
        self.assertEqual(
            points,
            [
                Point(x=2, y=2),
                Point(x=2, y=1),
            ],
        )

    def test_parse_line(self):
        (point1, point2) = parse_line(self.lines[0])
        self.assertEqual(point1, Point(x=0, y=9))
        self.assertEqual(point2, Point(x=5, y=9))


    def test_calculate(self):
        num_dangerous_points = calculate(self.lines)
        self.assertEqual(num_dangerous_points, 5)


if __name__ == "__main__":
    unittest.main()
