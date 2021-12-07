import unittest

from advent6a import (
    calculate,
    parse_line,
)


class Test6A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "3,4,3,1,2\n"
        ]

    def test_parse_line(self):
        num_list = parse_line(self.lines[0])
        self.assertEqual(num_list, [3, 4, 3, 1, 2])

    def test_calculate(self):
        num_fish = calculate(lines=self.lines, days=18)
        self.assertEqual(num_fish, 26)

        num_fish = calculate(lines=self.lines, days=80)
        self.assertEqual(num_fish, 5934)


if __name__ == "__main__":
    unittest.main()
