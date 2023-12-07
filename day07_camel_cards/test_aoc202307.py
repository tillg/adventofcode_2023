
import pathlib
import pytest
import aoc202307 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    raw_data = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(raw_data)

@pytest.fixture
def example2():
    raw_data = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(raw_data)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [{"hand": "32T3K", "bid": 765},
                        {"hand": "T55J5", "bid": 684},
                        {"hand": "KK677", "bid": 28},
                        {"hand": "KTJJT", "bid": 220},
                        {"hand": "QQQJA", "bid": 483}]

def test_hand_classifying():
    assert(aoc.classify_hand("32T3K")) == "one_pair"
    assert(aoc.classify_hand("T55J5")) == "three_of_a_kind"
    assert(aoc.classify_hand("KK677")) == "two_pair"
    assert(aoc.classify_hand("KTJJT")) == "two_pair"
    assert(aoc.classify_hand("QQQJA")) == "three_of_a_kind"
    assert(aoc.classify_hand("QQAQA")) == "full_house"
    assert(aoc.classify_hand("AQAAA")) == "four_of_a_kind"

def test_compare_cards():
    assert(aoc.compare_cards("2", "3")) == -1
    assert(aoc.compare_cards("3", "2")) == 1
    assert(aoc.compare_cards("2", "2")) == 0
    assert(aoc.compare_cards("T", "3")) == 1
    assert(aoc.compare_cards("3", "T")) == -1
    assert(aoc.compare_cards("T", "T")) == 0
    assert(aoc.compare_cards("T", "K")) == -1
    assert(aoc.compare_cards("K", "T")) == 1
    assert(aoc.compare_cards("T", "A")) == -1
    assert(aoc.compare_cards("A", "T")) == 1
    assert(aoc.compare_cards("K", "A")) == -1
    assert(aoc.compare_cards("A", "K")) == 1

def test_compare_hands_by_cards():
    assert(aoc.compare_hands_by_cards("32T3K", "T55J5")) == -1
    assert(aoc.compare_hands_by_cards("T55J5", "32T3K")) == 1
    assert(aoc.compare_hands_by_cards("32T3K", "32T3K")) == 0
    assert(aoc.compare_hands_by_cards("KTJJT", "KK677")) == -1
    assert(aoc.compare_hands_by_cards("KK677", "KTJJT")) == 1
    assert(aoc.compare_hands_by_cards("KTJJT", "KTJJT")) == 0
    assert(aoc.compare_hands_by_cards("KTJJT", "QQQJA")) == 1
    assert(aoc.compare_hands_by_cards("QQQJA", "KTJJT")) == -1
    assert(aoc.compare_hands_by_cards("KTJJT", "QQAQA")) == 1
    assert(aoc.compare_hands_by_cards("QQAQA", "KTJJT")) == -1
    assert(aoc.compare_hands_by_cards("KTJJT", "AQAAA")) == -1
    assert(aoc.compare_hands_by_cards("AQAAA", "KTJJT")) == 1
    assert(aoc.compare_hands_by_cards("KTJJT", "KQAAA")) == -1
    assert(aoc.compare_hands_by_cards("32T3K", "KK677")) == -1
    assert(aoc.compare_hands_by_cards("T55J5", "QQQJA")) == -1
    
def test_compare_hands():
    assert(aoc.compare_hands("32T3K", "T55J5")) == -1
    assert(aoc.compare_hands("T55J5", "32T3K")) == 1
    assert(aoc.compare_hands("32T3K", "32T3K")) == 0
    assert(aoc.compare_hands("KTJJT", "KK677")) == -1
    assert(aoc.compare_hands("KK677", "KTJJT")) == 1

def test_sort_games(example1):
        assert aoc.sort_game(example1) == [
            {"hand": "32T3K", "bid": 765},
            {"hand": "KTJJT", "bid": 220},
            {"hand": "KK677", "bid": 28},
            {"hand": "T55J5", "bid": 684},
            {"hand": "QQQJA", "bid": 483}
            ]

def test_solve1(example1):
    assert aoc.part1(example1) == 6440

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 288

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 281

@pytest.mark.skip(reason="Not implemented")
@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...