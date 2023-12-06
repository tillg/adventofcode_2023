#!/usr/bin/python3

import pathlib
import sys
import logging
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day01_trebuchet.utils import get_logger

def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split("\n")]

def is_number_at_position(line, position):
    """Check if a written number is within line at a certain position."""
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for counter, number_string in enumerate(numbers):
        if line[position:position + len(number_string)] == number_string:
            return counter
    return None

def identify_digit(line, position):
    """Identify the digit at the given position."""
    logger = get_logger(identify_digit.__name__, logging.INFO)
    digit = None
    if line[position].isdigit():
        digit = int(line[position]) 
        return digit
    if is_number_at_position(line, position) is not None:
        digit = is_number_at_position(line, position)
        return digit
    return digit

def get_number_of_line(line):
    """Get the digit of the line."""
    logger = get_logger(get_number_of_line.__name__, logging.INFO)
    first_digit_char = None
    for char in line:
        if char.isdigit():
            first_digit_char = char
    last_digit_char = None
    for char in reversed(line):
        if char.isdigit():
            last_digit_char = char
    if first_digit_char is None or last_digit_char is None:
        raise ValueError("No digit found in line")  
    first_digit = int(first_digit_char)
    last_digit = int(last_digit_char)
    digit = first_digit  + last_digit * 10
    # logger.info(f"Line {line} has digit {digit}")
    return digit

def get_number_of_line_including_written_numbers(line):
    """Get the digit of the line."""
    logger = get_logger(get_number_of_line_including_written_numbers.__name__, logging.INFO)
    first_digit = None
    for position, char in enumerate(line):
        if identify_digit(line, position) is not None:
            first_digit = identify_digit(line, position)
            logger.info(f"Found first digit {first_digit} at position {position} in line {line}")
            break
    last_digit = None
    for position, char in enumerate(reversed(line)):
        if identify_digit(line, position) is not None:
            last_digit = identify_digit(line, position)
    digit = first_digit *10 + last_digit
    logger.info(f"Line {line} has digit {digit}")
    return digit
    

def part1(data):
    """Solve part 1."""
    sum = 0
    for line in data:
        sum += get_number_of_line(line)
    return sum


def part2(data):
    """Solve part 2."""
    sum = 0
    for line in data:
        sum += get_number_of_line_including_written_numbers(line)
    return sum

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = pathlib.Path("./input1.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print(f"Solution 1: {solutions}")