# coding=utf-8
"""Advent of Code 2017, Day 2, Part 1"""

with open("input.txt") as f:
    digits = [[int(n) for n in data.split()] for data in f]

print(sum(max(line) - min(line) for line in digits))
