import unittest

from advent8a import calculate, parse_line


class Test8A(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\n",
        ]

    def test_parse_line(self):
        signal_patterns, output_values = parse_line(self.lines[0])
        self.assertEqual(
            signal_patterns,
            [
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ],
        )
        self.assertEqual(output_values, ["fdgacbe", "cefdb", "cefbgd", "gcbe"])

    def test_calculate(self):
        result = calculate(lines=self.lines)
        print("result:", result)
        self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest.main()
