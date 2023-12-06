# aoc_template.py

import pathlib
import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day01_trebuchet.utils import get_logger

def parse(puzzle_input):
    """Parse input."""
    logger = get_logger(parse.__name__, logging.INFO)


def part1(data):
    """Solve part 1."""
    logger = get_logger(part1.__name__, logging.INFO)

def part2(data):
    """Solve part 2."""
    logger = get_logger(part2.__name__, logging.INFO)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    logger = get_logger(solve.__name__, logging.INFO)

    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    print("Hello")
    puzzle_input = pathlib.Path("input1.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print(f"Solution 1: {solutions}")