# coding=utf-8
"""Advent of Code 2017, Day 14, Part 2"""

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


def mark_neighbouring_squares(square):
    """
    Mark all neighbouring squares as part of the same region.
    :param square: The coordinates of the initial square
    """
    i, j = square
    if (i, j) not in visited_squares and grid[i][j] == "1":
        visited_squares.add((i, j))
        if i > 0:
            mark_neighbouring_squares((i - 1, j))
        if i < 127:
            mark_neighbouring_squares((i + 1, j))
        if j > 0:
            mark_neighbouring_squares((i, j - 1))
        if j < 127:
            mark_neighbouring_squares((i, j + 1))


with open("input.txt") as f:
    input_string = f.read().rstrip("\n")

grid = [knot_hash(input_string + "-" + str(row)) for row in range(128)]
visited_squares = set()
num_regions = 0

for row_num in range(128):
    for column_num in range(128):
        if (row_num, column_num) not in visited_squares and grid[row_num][column_num] == "1":
            num_regions += 1
            mark_neighbouring_squares((row_num, column_num))

print(num_regions)
