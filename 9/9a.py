# coding=utf-8
"""Advent of Code 2017, Day 9, Part 1"""

with open("input.txt") as f:
    stream = f.read()

i = 0
output_stream = ""
is_garbage = False
while i < len(stream):
    if stream[i] == "!":
        i += 1
    elif stream[i] == "<":
        is_garbage = True
    elif not is_garbage:
        output_stream += stream[i]
    elif stream[i] == ">":
        is_garbage = False
    i += 1

score = 0
depth = 0
for c in output_stream:
    if c == "{":
        depth += 1
        score += depth
    elif c == "}":
        depth -= 1

print(score)
