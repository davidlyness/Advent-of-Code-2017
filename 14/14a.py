# coding=utf-8
"""Advent of Code 2017, Day 14, Part 1"""

import functools
import operator


def knot_hash(string):
    """
    Perform a knot hash (http://adventofcode.com/2017/day/10)
    :param string: the input string for the hash
    :return: the binary result of the hash
    """
    lengths = [ord(n) for n in string]
    lengths.extend([17, 31, 73, 47, 23])
    num_rounds = 64
    nums = list(range(256))
    current_position = 0
    skip_size = 0
    for _ in range(num_rounds):
        for length in lengths:
            numbers_to_reverse = [nums[(current_position + i) % len(nums)] for i in range(length)]
            for i in range(length):
                nums[(current_position + length - 1 - i) % len(nums)] = numbers_to_reverse[i]
            current_position += length + skip_size
            skip_size += 1
    string_hash = "".join([format(functools.reduce(operator.xor, nums[i * 16:i * 16 + 16]), "02x") for i in range(16)])
    return format(int(string_hash, 16), "0128b")


with open("input.txt") as f:
    input_string = f.read().rstrip("\n")

print(sum([str(knot_hash(input_string + "-" + str(row))).count("1") for row in range(128)]))
