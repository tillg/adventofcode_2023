#!/usr/bin/python3

import pathlib
import sys
import logging
import os
from utils import get_logger
from collections import Counter
import functools

hand_classes = ["five_of_a_kind", "four_of_a_kind", "full_house", "three_of_a_kind", "two_pair", "one_pair", "high_card"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q","K", "A"]

def parse(raw_data):
    """Parse input."""
    logger = get_logger(parse.__name__, logging.INFO)
    lines = [line for line in raw_data.split("\n")]
    logger.info(f"Lines: {lines}")
    result = []
    for line in lines:
        words = [word for word in line.split()]
        sub_result = {"hand": words[0], "bid": int(words[1])}
        result.append(sub_result)
    logger.info(f"Result: {result}")
    return result

def classify_hand(hand):
    """Classify the hand."""
    logger = get_logger(classify_hand.__name__, logging.INFO)
    counts = Counter(hand)

    if all(c == hand[0] for c in hand):
        return "five_of_a_kind"
    if 4 in counts.values():
        return "four_of_a_kind"
    if sorted(counts.values()) == [2, 3]:
        return "full_house"
    if 3 in counts.values():
        return "three_of_a_kind"
    if list(counts.values()).count(2) == 2:
        return "two_pair"
    if 2 in counts.values():
        return "one_pair"
    return "high_card"

def compare_cards(card1, card2):
    """Compare two cards."""
    logger = get_logger(compare_cards.__name__, logging.WARNING)
    logger.info(f"Card1: {card1}")
    logger.info(f"Card2: {card2}")
    card1_index = cards.index(card1)
    card2_index = cards.index(card2)
    if card1_index > card2_index:
        return 1
    if card1_index < card2_index:
        return -1
    return 0

def compare_hands_by_cards(hand1, hand2):
    """Compare two hands by cards."""
    logger = get_logger(compare_hands_by_cards.__name__, logging.INFO)
    logger.info(f"Hand1: {hand1}")
    logger.info(f"Hand2: {hand2}")
    for i in range(len(hand1)):
        comparison = compare_cards(hand1[i], hand2[i])
        if comparison == 1:
            return 1
        if comparison == -1:
            return -1
    return 0

def compare_hands(hand1, hand2):
    """Compare two hands."""
    logger = get_logger(compare_hands.__name__, logging.INFO)
    hand1_class = classify_hand(hand1)
    hand2_class = classify_hand(hand2)
    logger.info(f"Hand1 class: {hand1_class}")
    logger.info(f"Hand2 class: {hand2_class}")
    if hand_classes.index(hand1_class) > hand_classes.index(hand2_class):
        return -1
    if hand_classes.index(hand1_class) < hand_classes.index(hand2_class):
        return 1
    return compare_hands_by_cards(hand1, hand2)

def compare_games(game1, game2):
    """Compare two games."""
    logger = get_logger(compare_games.__name__, logging.INFO)
    logger.info(f"Game1: {game1}")
    logger.info(f"Game2: {game2}")
    return compare_hands(game1["hand"], game2["hand"])

def sort_game(game):
    """Sort the game."""
    logger = get_logger(sort_game.__name__, logging.INFO)
    logger.info(f"Game: {game}")
    sorted_game = sorted(game, key=functools.cmp_to_key(compare_games))
    return sorted_game

def part1(input):
    """Solve part 1."""
    logger = get_logger(part1.__name__, logging.INFO)
    sum = 0
    sorted_game = sort_game(input)
    for rank, hand_bid in enumerate(sorted_game):
        product = (rank+1) * hand_bid["bid"]
        logger.info(f"Rank: {rank+1}, Hand: {hand_bid['hand']}, Bid: {hand_bid['bid']} --> Product: {product} ")
        sum += product
    return sum


def part2(data):
    """Solve part 2."""
    logger = get_logger(part2.__name__, logging.INFO)
    product = 1
    logger.info(f"Input: {input}")
    for i in range(len(input["time"])):
        faster_options = number_of_possible_faster_options(input["time"][i], data["distance"][i])    
        product *= faster_options
    return product

if __name__ == "__main__":
    logger = get_logger("main", logging.INFO)

    raw_data = pathlib.Path("./input1.txt").read_text().strip()
    logger.info(f"Raw_data: {raw_data}")

    input = parse(raw_data)
    solution1 = part1(input)
    print(f"Solution 1: {solution1}")

    # input2 = parse2(raw_data)
    # solution2 = part1(input2)
    # print(f"Solution 2: {solution2}")
