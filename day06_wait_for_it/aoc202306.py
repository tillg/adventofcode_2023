#!/usr/bin/python3

import pathlib
import sys
import logging
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from day01_trebuchet.utils import get_logger

def parse(raw_data):
    """Parse input."""
    logger = get_logger(parse.__name__, logging.INFO)
    lines = [line for line in raw_data.split("\n")]
    logger.info(f"Lines: {lines}")
    times_words = [word for word in lines[0].split()]
    del times_words[0]
    times = [int(word) for word in times_words]
    logger.info(f"Times: {times}")
    distances_words = [word for word in lines[1].split()]
    del distances_words[0]
    distances = [int(word) for word in distances_words]
    return {"time": times, "distance": distances}

def parse2(raw_data):
    """Parse input for puzzle part2"""
    logger = get_logger(parse2.__name__, logging.INFO)
    interims_data = parse(raw_data)
    logger.info(f"Interims data: {interims_data}")
    time_strings = [str(time) for time in interims_data["time"]]
    time_string = "".join(time_strings)
    long_time = int(time_string)
    distance_strings = [str(distance) for distance in interims_data["distance"]]
    distance_string = "".join(distance_strings)
    long_distance = int(distance_string)
    new_input = {"time": [long_time], "distance": [long_distance]}
    logger.info(f"New input: {new_input}")
    return new_input

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

def part1(input):
    """Solve part 1."""
    product = 1
    for i in range(len(input["time"])):
        faster_options = number_of_possible_faster_options(input["time"][i], input["distance"][i])    
        product *= faster_options
    return product


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

    input2 = parse2(raw_data)
    solution2 = part1(input2)
    print(f"Solution 2: {solution2}")
