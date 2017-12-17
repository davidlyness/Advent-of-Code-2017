# coding=utf-8
"""Advent of Code 2017, Day 17, Part 1"""

with open("input.txt") as f:
    num_steps = int(f.read())

buffer = [0]
buffer_position = 0

for value in range(1, 2018):
    buffer_position = ((buffer_position + num_steps) % len(buffer)) + 1
    buffer.insert(buffer_position, value)

print(buffer[(buffer_position + 1) % len(buffer)])
