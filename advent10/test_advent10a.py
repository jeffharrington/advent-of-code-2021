import unittest

from advent10a import calculate, parse_line


class Test10A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "[({(<(())[]>[[{[]{<()<>>\n",
            "[(()[<>])]({[<{<<[]>>(\n",
            "{([(<{}[<>[]}>{[]{[(<()>\n",
            "(((({<>}<{<{<>}{[]{[]{}\n",
            "[[<[([]))<([[{}[[()]]]\n",
            "[{[{({}]{}}([{[{{{}}([]\n",
            "{<[[]]>}<{[{[{[]{()[[[]\n",
            "[<(<(<(<{}))><([]([]()\n",
            "<{([([[(<>()){}]>(<<{{\n",
            "<{([{{}}[<[[[<>{}]]]>[]]\n",
        ]

    def test_parse_line(self):
        line = parse_line(self.lines[0])
        self.assertEqual(
            line,
            [
                "[",
                "(",
                "{",
                "(",
                "<",
                "(",
                "(",
                ")",
                ")",
                "[",
                "]",
                ">",
                "[",
                "[",
                "{",
                "[",
                "]",
                "{",
                "<",
                "(",
                ")",
                "<",
                ">",
                ">",
            ],
        )

    def test_calculate(self):
        result = calculate(lines=self.lines)
        print("result:", result)
        self.assertEqual(result, 26397)


if __name__ == "__main__":
    unittest.main()
