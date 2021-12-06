import unittest

from advent3a import calculate


class Test3A(unittest.TestCase):
    def test_success(self):
        lines = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        result = calculate(lines)
        self.assertEqual(result, 198)


if __name__ == "__main__":
    unittest.main()
