import unittest

from advent11a import calculate, parse_lines, flash


class Test11A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "11111\n",
            "19991\n",
            "19191\n",
            "19991\n",
            "11111\n",
        ]
        self.large_lines = [
            "5483143223\n",
            "2745854711\n",
            "5264556173\n",
            "6141336146\n",
            "6357385478\n",
            "4167524645\n",
            "2176841721\n",
            "6882881134\n",
            "4846848554\n",
            "5283751526\n",
        ]

    def test_parse_lines(self):
        matrix = parse_lines(self.lines)
        self.assertEqual(
            matrix,
            [
                [1, 1, 1, 1, 1],
                [1, 9, 9, 9, 1],
                [1, 9, 1, 9, 1],
                [1, 9, 9, 9, 1],
                [1, 1, 1, 1, 1],
            ],
        )

    def test_flash(self):
        matrix = [
            [0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        flash(matrix, i=1, j=1)
        self.assertEqual(
            matrix,
            [
                [1, 1, 1, 0, 0],
                [1, -9, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )

    def test_calculate(self):
        result = calculate(lines=self.large_lines)
        print("Result:", result)
        self.assertEqual(result, 1656)


if __name__ == "__main__":
    unittest.main()
