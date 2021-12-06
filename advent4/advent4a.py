#
# Day 4: Giant Squid Bingo
# https://adventofcode.com/2021/day/4
#
from typing import List, Set

ROW1_SET = set(range(0, 5))
ROW2_SET = set(range(5, 10))
ROW3_SET = set(range(10, 15))
ROW4_SET = set(range(15, 20))
ROW5_SET = set(range(20, 25))

COL1_SET = set([0, 5, 10, 15, 20])
COL2_SET = set([1, 6, 11, 16, 21])
COL3_SET = set([2, 7, 12, 17, 22])
COL4_SET = set([3, 8, 13, 18, 23])
COL5_SET = set([4, 9, 14, 19, 24])


def get_card_set(card: list[int], target_set: set[int]) -> set[int]:
    # Returns the set of numbers located on the card at the target_set
    card_set = set()
    for i in target_set:
        card_set.add(card[i])
    return card_set


def set_has_winner(
    card: list[int], target_set: set[int], drawn_numbers: set[int]
) -> bool:
    # Returns true/false if target_set on card matches 5 or more drawn_numbers
    card_set = get_card_set(card, target_set=target_set)
    intersection = card_set.intersection(drawn_numbers)
    return len(intersection) >= 5


def get_unmarked_numbers_from_card(
    card: List[int], drawn_numbers: Set[int]
) -> List[int]:
    full_card_set = set(card)
    difference = full_card_set.difference(drawn_numbers)
    return list(difference)


def card_has_horizontal_winner(card: list[int], drawn_numbers: set[int]) -> bool:
    # Returns true/false if any of the rows of the card contain 5 or more drawn numbers.
    return (
        set_has_winner(card=card, target_set=ROW1_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=ROW2_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=ROW3_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=ROW4_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=ROW5_SET, drawn_numbers=drawn_numbers)
    )


def card_has_vertical_winner(card: list[int], drawn_numbers: set[int]) -> bool:
    # Returns true/false if any of the cols of the card contain 5 or more drawn numbers.
    return (
        set_has_winner(card=card, target_set=COL1_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=COL2_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=COL3_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=COL4_SET, drawn_numbers=drawn_numbers)
        or set_has_winner(card=card, target_set=COL5_SET, drawn_numbers=drawn_numbers)
    )


def card_has_winner(card: List[int], drawn_numbers: Set[int]) -> bool:
    # Returns true/false if any of the rows or cols of the card contain 5 or more drawn numbers.
    return card_has_horizontal_winner(
        card=card, drawn_numbers=drawn_numbers
    ) or card_has_vertical_winner(card=card, drawn_numbers=drawn_numbers)


def get_numbers_to_draw_from_line(line: str) -> List[int]:
    # Converts the first line of Bingo input to set of integers
    num_str_list = line.rstrip().split(",")
    num_int_list = [int(c) for c in num_str_list]
    return num_int_list


def get_cards_from_input(lines: List[str]) -> List[list]:
    # Returns a list of lists representing all the bingo cards from the input.
    cards: List[list] = []
    curr_card: List[int] = []
    for line in lines:

        if line.rstrip() == "" and curr_card:
            cards.append(curr_card)
            curr_card = []
            continue
        else:
            num_str_list = line.rstrip().split()
            num_int_list = [int(c) for c in num_str_list]
            curr_card.extend(num_int_list)
    cards.append(curr_card)
    return cards


def calculate(lines: List[str]) -> int:
    # Process the input file and return the final score
    all_numbers = get_numbers_to_draw_from_line(line=lines[0])
    cards = get_cards_from_input(lines=lines[1:])
    drawn_numbers: Set[int] = set()
    winning_card = None
    final_score = 0
    for curr_number in all_numbers:
        drawn_numbers.add(curr_number)
        for card in cards:
            if card_has_winner(card=card, drawn_numbers=drawn_numbers):
                winning_card = card
                break
        if winning_card:
            unmarked_numbers = get_unmarked_numbers_from_card(
                card=winning_card, drawn_numbers=drawn_numbers
            )
            unmarked_sum = sum(unmarked_numbers)
            final_score = unmarked_sum * curr_number
            break
    if winning_card:
        print("-" * 100)
        print("We found a winner!")
        print("Winning card:", winning_card)
        print("Winning number:", curr_number)
        print("Unmarked numbers:", unmarked_numbers)
        print("Unmarked sum:", unmarked_sum)
        print("Final Score", final_score)
        print("-" * 100)
    return final_score


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    result = calculate(lines)
