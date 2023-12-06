
import pathlib
import pytest
import day06_wait_for_it.aoc202306 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {"time": [7,15,30], "distance": [9, 40, 200]}

def test_travel_distance():
    """Test calculation of travel distance."""
    assert aoc.travel_distances(7, 0) == 0
    assert aoc.travel_distances(7,1) == 6
    assert aoc.travel_distances(7,2) == 10
    assert aoc.travel_distances(7,3) == 12
    assert aoc.travel_distances(7,4) == 12
    assert aoc.travel_distances(7,5) == 10
    assert aoc.travel_distances(7,6) == 6
    assert aoc.travel_distances(7,7) == 0

def test_number_of_possible_faster_options(example1):
    """Test calculation of number of possible faster options."""
    assert aoc.number_of_possible_faster_options(7, 9) == 4
    assert aoc.number_of_possible_faster_options(15, 40) == 8
    assert aoc.number_of_possible_faster_options(30, 200) == 9

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