# coding=utf-8
"""Advent of Code 2017, Day 5, Part 1"""

with open("input.txt") as f:
    instructions = [int(n) for n in f.read().split()]

pointer = 0
num_steps = 0
while pointer < len(instructions):
    new_pointer = pointer + instructions[pointer]
    instructions[pointer] += 1
    pointer = new_pointer
    num_steps += 1

print(num_steps)
