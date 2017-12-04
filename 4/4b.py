# coding=utf-8
"""Advent of Code 2017, Day 4, Part 2"""

with open("input.txt") as f:
    passphrases = f.read().split("\n")

print(sum(len(p.split()) == len(set("".join(sorted(i)) for i in p.split())) for p in passphrases))
