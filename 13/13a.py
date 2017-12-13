# coding=utf-8
"""Advent of Code 2017, Day 13, Part 1"""

with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split("\n")

layers = {int(line.split(": ")[0]): int(line.split(": ")[1]) for line in puzzle_input}
trip_severity = 0

for current_depth in range(max(layers)):
    if current_depth in layers and current_depth % (2 * layers[current_depth] - 2) == 0:
        trip_severity += current_depth * layers[current_depth]

print(trip_severity)
