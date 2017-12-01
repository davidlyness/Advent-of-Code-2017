# coding=utf-8
"""Advent of Code 2017, Day 1, Part 2"""

with open("input.txt") as f:
    digits = f.read().rstrip("\n")

digit_sum = 0
for i in range(len(digits)):
    if digits[i] == digits[(i + len(digits)//2) % len(digits)]:
        digit_sum += int(digits[i])

print(digit_sum)
