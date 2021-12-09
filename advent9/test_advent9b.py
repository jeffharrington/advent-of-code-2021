import unittest

from advent9b import calculate, parse_lines


class Test9B(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
        ]

    def test_parse_lines(self):
        heightmap = parse_lines(self.lines)
        self.assertEqual(
            heightmap,
            [
                [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
            ],
        )

    def test_calculate(self):
        result = calculate(lines=self.lines)
        print("result:", result)
        self.assertEqual(result, 1134)


if __name__ == "__main__":
    unittest.main()
