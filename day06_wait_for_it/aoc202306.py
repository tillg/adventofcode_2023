#!/usr/bin/python3

import pathlib
import sys
import logging
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day01_trebuchet.utils import get_logger

def parse(puzzle_input):
    """Parse input."""
    logger = get_logger(parse.__name__, logging.INFO)
    lines = [line for line in puzzle_input.split("\n")]
    logger.info(f"Lines: {lines}")
    times_words = [word for word in lines[0].split()]
    del times_words[0]
    times = [int(word) for word in times_words]
    logger.info(f"Times: {times}")
    distances_words = [word for word in lines[1].split()]
    del distances_words[0]
    distances = [int(word) for word in distances_words]
    return {"time": times, "distance": distances}

def travel_distances(race_duration, time_pressed):
    speed = time_pressed
    time_to_travel = race_duration-time_pressed
    distance = speed * time_to_travel
    return distance

def number_of_possible_faster_options(race_duration, farthest_distance):
    faster_options = 0
    for time_pressed in range(race_duration):
        if travel_distances(race_duration, time_pressed) > farthest_distance:
            faster_options += 1
    return faster_options

def part1(data):
    """Solve part 1."""
    product = 1
    for i in range(len(data["time"])):
        faster_options = number_of_possible_faster_options(data["time"][i], data["distance"][i])    
        product *= faster_options
    return product


def part2(data):
    """Solve part 2."""
    sum = 0
    for line in data:
        sum += get_number_of_line_including_written_numbers(line)
    return sum

if __name__ == "__main__":
    puzzle_input = pathlib.Path("./input1.txt").read_text().strip()
    input = parse(puzzle_input)
    solution1 = part1(input)
    print(f"Solution 1: {solution1}")
    #solution2 = part2(puzzle_input)
