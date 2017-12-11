# coding=utf-8
"""Advent of Code 2017, Day 10, Part 2"""

import functools
import operator

with open("input.txt") as f:
    lengths = [ord(n) for n in f.read()]
lengths.extend([17, 31, 73, 47, 23])

num_rounds = 64
numbers = list(range(256))
current_position = 0
skip_size = 0

for _ in range(num_rounds):
    for length in lengths:
        numbers_to_reverse = [numbers[(current_position + i) % len(numbers)] for i in range(length)]
        for i in range(length):
            numbers[(current_position + length - 1 - i) % len(numbers)] = numbers_to_reverse[i]
        current_position += length + skip_size
        skip_size += 1

print("".join([format(functools.reduce(operator.xor, numbers[i * 16:i * 16 + 16]), "x") for i in range(16)]))
