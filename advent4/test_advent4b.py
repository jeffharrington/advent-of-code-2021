import unittest

from advent4b import (
    calculate,
    card_has_horizontal_winner,
    card_has_vertical_winner,
    COL1_SET,
    get_card_set,
    ROW1_SET,
    ROW2_SET,
    set_has_winner,
    get_numbers_to_draw_from_line,
    get_cards_from_input,
    get_unmarked_numbers_from_card,
)


class Test4B(unittest.TestCase):
    def setUp(self) -> None:
        self.input = [
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n",
            "\n",
            "22 13 17 11  0\n",
            "8  2 23  4 24\n",
            "21  9 14 16  7\n",
            "6 10  3 18  5\n",
            "1 12 20 15 19\n",
            "\n",
            "3 15  0  2 22\n",
            "9 18 13 17  5\n",
            "19  8  7 25 23\n",
            "20 11 10 24  4\n",
            "14 21 16 12  6\n",
            "\n",
            "14 21 17 24  4\n",
            "10 16 15  9 19\n",
            "18  8 23 26 20\n",
            "22 11 13  6  5\n",
            "2  0 12  3  7\n",
        ]
        self.drawn_numbers = [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ]
        self.test_card = [
            22,
            13,
            17,
            11,
            0,
            8,
            2,
            23,
            4,
            24,
            21,
            9,
            14,
            16,
            7,
            6,
            10,
            3,
            18,
            5,
            1,
            12,
            20,
            15,
            19,
        ]
        return super().setUp()

    def test_get_card_set(self):
        row_set = get_card_set(card=self.test_card, target_set=ROW1_SET)
        self.assertEqual(row_set, set([22, 13, 17, 11, 0]))

        col_set = get_card_set(card=self.test_card, target_set=COL1_SET)
        self.assertEqual(col_set, set([22, 8, 21, 6, 1]))

    def test_set_has_winner(self):
        success_drawn_numbers = set([8, 2, 9, 23, 4, 1, 24, 19])
        has_winner = set_has_winner(
            card=self.test_card,
            target_set=ROW2_SET,
            drawn_numbers=success_drawn_numbers,
        )
        self.assertTrue(has_winner)
        #
        bad_drawn_numbers = set([22, 21, 8, 3, 4, 1, 5, 19])
        has_winner = set_has_winner(
            card=self.test_card,
            target_set=ROW2_SET,
            drawn_numbers=bad_drawn_numbers,
        )
        self.assertFalse(has_winner)

    def test_card_has_horizontal_winner(self):
        success_drawn_numbers = set([6, 21, 10, 3, 14, 18, 7, 5])
        has_horizontal_winner = card_has_horizontal_winner(
            card=self.test_card,
            drawn_numbers=success_drawn_numbers,
        )
        self.assertTrue(has_horizontal_winner)
        #
        bad_drawn_numbers = set([1, 21, 6, 8, 22, 13, 2, 9])
        has_horizontal_winner = card_has_horizontal_winner(
            card=self.test_card,
            drawn_numbers=bad_drawn_numbers,
        )
        self.assertFalse(has_horizontal_winner)

    def test_card_has_vertical_winner(self):
        success_drawn_numbers = set([22, 8, 9, 21, 10, 6, 20, 1])
        has_vertical_winner = card_has_vertical_winner(
            card=self.test_card,
            drawn_numbers=success_drawn_numbers,
        )
        self.assertTrue(has_vertical_winner)
        #
        bad_drawn_numbers = set([6, 21, 10, 3, 14, 18, 7, 5])
        has_vertical_winner = card_has_vertical_winner(
            card=self.test_card,
            drawn_numbers=bad_drawn_numbers,
        )
        self.assertFalse(has_vertical_winner)

    def test_get_numbers_to_draw_from_line(self):
        line = (
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n"
        )
        drawn_numbers = get_numbers_to_draw_from_line(line)
        self.assertEqual(
            drawn_numbers,
            [
                7,
                4,
                9,
                5,
                11,
                17,
                23,
                2,
                0,
                14,
                21,
                24,
                10,
                16,
                13,
                6,
                15,
                25,
                12,
                22,
                18,
                20,
                8,
                19,
                3,
                26,
                1,
            ],
        )

    def test_get_cards_from_input(self):
        cards = get_cards_from_input(self.input[1:])
        self.assertEqual(len(cards), 3)
        self.assertEqual(cards[0], self.test_card)

    def test_get_unmarked_numbers_from_card(self):
        first_8_numbers = self.drawn_numbers[:8]
        unmarked_numbers = get_unmarked_numbers_from_card(
            card=self.test_card, drawn_numbers=set(first_8_numbers)
        )
        self.assertEqual(
            unmarked_numbers,
            [0, 1, 3, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24],
        )

    def test_calculate(self):
        final_score = calculate(lines=self.input)
        self.assertEqual(final_score, 1924)


if __name__ == "__main__":
    unittest.main()
