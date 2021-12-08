import unittest

from advent7b import (
    calculate,
    summation,
)


class Test7A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = ["16,1,2,0,4,2,7,1,2,14\n"]

    def test_calculate(self):
        fuel_cost = calculate(lines=self.lines)
        self.assertEqual(fuel_cost, 168)

    def test_summation(self):
        self.assertEqual(summation(target=abs(16 - 5)), 66)
        self.assertEqual(summation(target=abs(1 - 5)), 10)


if __name__ == "__main__":
    unittest.main()
