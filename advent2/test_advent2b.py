import unittest

from advent2b import calculate

class Test2b(unittest.TestCase):

    def test_success(self):
        lines = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        ]
        result = calculate(lines)
        self.assertEqual(result, 900)

if __name__ == '__main__':
    unittest.main()
