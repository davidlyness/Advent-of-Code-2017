# coding=utf-8
"""Advent of Code 2017, Day 12, Part 2"""


def find_program_group(current_program):
    """
    Determine which programs form a group with a specific program.
    :param current_program: the program to start with
    :return: list of programs in the same group as starting program
    """
    programs_to_explore = [current_program]
    explored_programs = []
    while len(programs_to_explore) > 0:
        current_program = programs_to_explore.pop()
        explored_programs.append(current_program)
        programs_to_explore.extend([p for p in pipes[current_program]
                                    if p not in explored_programs and p not in programs_to_explore])
    return explored_programs


with open("input.txt") as f:
    puzzle_input = f.read().rstrip("\n").split("\n")

pipes = {}
for line in puzzle_input:
    connection_strings = line.split(" <-> ")
    pipes[int(connection_strings[0])] = [int(n) for n in connection_strings[1].split(", ")]

groups = []
for program in pipes.keys():
    if all(program not in group for group in groups):
        groups.append(find_program_group(program))

print(len(groups))
