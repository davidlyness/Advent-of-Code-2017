# coding=utf-8
"""Advent of Code 2017, Day 10, Part 1"""

with open("input.txt") as f:
    lengths = [int(n) for n in f.read().split(",")]

numbers = list(range(256))
current_position = 0
skip_size = 0

for length in lengths:
    numbers_to_reverse = [numbers[(current_position + i) % len(numbers)] for i in range(length)]
    for i in range(length):
        numbers[(current_position + length - 1 - i) % len(numbers)] = numbers_to_reverse[i]
    current_position += length + skip_size
    skip_size += 1

print(numbers[0] * numbers[1])
