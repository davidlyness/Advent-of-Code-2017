# coding=utf-8
"""Advent of Code 2017, Day 9, Part 2"""

with open("input.txt") as f:
    stream = f.read()

i = 0
output_stream = ""
is_garbage = False
while i < len(stream):
    if stream[i] == "!":
        i += 1
    elif stream[i] == "<" and not is_garbage:
        is_garbage = True
    elif stream[i] == ">":
        is_garbage = False
    elif is_garbage:
        output_stream += stream[i]
    i += 1

print(len(output_stream))
