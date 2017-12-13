# coding=utf-8
"""Advent of Code 2017, Day 13, Part 2"""

with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split("\n")

layers = {int(line.split(": ")[0]): int(line.split(": ")[1]) for line in puzzle_input}
is_caught = True
delay = -1

while is_caught:
    is_caught = False
    delay += 1
    current_depth = -1
    while current_depth < max(layers) and not is_caught:
        current_depth += 1
        is_caught = current_depth in layers and (current_depth + delay) % (2 * layers[current_depth] - 2) == 0

print(delay)
