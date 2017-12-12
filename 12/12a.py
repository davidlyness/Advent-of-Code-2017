# coding=utf-8
"""Advent of Code 2017, Day 12, Part 1"""

with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split("\n")

pipes = {}
for line in puzzle_input:
    connection_strings = line.split(" <-> ")
    pipes[int(connection_strings[0])] = [int(n) for n in connection_strings[1].split(", ")]

programs_to_explore = [0]
explored_programs = []

while len(programs_to_explore) > 0:
    current_program = programs_to_explore.pop()
    explored_programs.append(current_program)
    programs_to_explore.extend([p for p in pipes[current_program]
                                if p not in explored_programs and p not in programs_to_explore])

print(len(explored_programs))
