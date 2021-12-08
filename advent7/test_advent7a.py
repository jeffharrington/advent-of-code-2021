import unittest

from advent7a import (
    calculate,
)


class Test7A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "16,1,2,0,4,2,7,1,2,14\n"
        ]

    def test_calculate(self):
        fuel_cost = calculate(lines=self.lines)
        self.assertEqual(fuel_cost, 37)


if __name__ == "__main__":
    unittest.main()
