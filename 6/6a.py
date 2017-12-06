# coding=utf-8
"""Advent of Code 2017, Day 6, Part 1"""

with open("input.txt") as f:
    banks = [int(n) for n in f.read().split()]

seen_banks = []
num_banks = len(banks)
num_cycles = 0

while banks not in seen_banks:
    num_cycles += 1
    seen_banks.append(list(banks))
    max_bucket_value = max(banks)
    max_bucket_index = banks.index(max_bucket_value)
    banks[max_bucket_index] = 0
    for offset in range(max_bucket_value):
        banks[(max_bucket_index + offset + 1) % num_banks] += 1

print(num_cycles)
