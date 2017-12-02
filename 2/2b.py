# coding=utf-8
"""Advent of Code 2017, Day 2, Part 1"""

import itertools

with open("input.txt") as f:
    digits = [[int(n) for n in data.split()] for data in f]

print(sum(m // n for line in digits for m, n in itertools.combinations(sorted(line, reverse=True), 2) if m % n == 0))
