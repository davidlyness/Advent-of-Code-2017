# coding=utf-8
"""Advent of Code 2017, Day 15, Part 1"""

current_a = 516
current_b = 190
num_matches = 0

for _ in range(40000000):
    current_a = (current_a * 16807) % 2147483647
    current_b = (current_b * 48271) % 2147483647
    if str(format(current_a, "016b"))[-16:] == str(format(current_b, "016b"))[-16:]:
        num_matches += 1

print(num_matches)
