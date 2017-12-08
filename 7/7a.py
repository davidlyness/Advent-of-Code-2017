# coding=utf-8
"""Advent of Code 2017, Day 7, Part 1"""

import re

with open("input.txt") as f:
    puzzle_input = f.read().split("\n")

programs = []
for line in puzzle_input:
    match = re.search("(\w+) \((\d+)\)( -> (.*))?", line)
    if match.group(4) is not None:
        children = match.group(4).split(", ")
    else:
        children = []
    programs.append({
        "name": match.group(1),
        "weight": int(match.group(2)),
        "children": children
    })

all_programs = set()
child_programs = set()
for program in programs:
    all_programs.add(program['name'])
    for child in program['children']:
        child_programs.add(child)

print(list(all_programs - child_programs)[0])
