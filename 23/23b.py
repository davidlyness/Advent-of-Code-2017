# coding=utf-8
"""Advent of Code 2017, Day 23, Part 2"""

import math

register_h = 0
for i in range(107900, 124900 + 1, 17):
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            register_h += 1
            break

print(register_h)
