# coding=utf-8
"""Advent of Code 2017, Day 17, Part 2"""

with open("input.txt") as f:
    num_steps = int(f.read())

buffer_position = 0
current_value_after_0 = None

for value in range(1, 50000001):
    buffer_position = ((buffer_position + num_steps) % value) + 1
    if buffer_position == 1:
        current_value_after_0 = value

print(current_value_after_0)
