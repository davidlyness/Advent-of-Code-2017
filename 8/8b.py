# coding=utf-8
"""Advent of Code 2017, Day 8, Part 1"""

import re

with open("input.txt") as f:
    puzzle_input = f.read().split("\n")

register_names = set()
operations = []
for line in puzzle_input:
    match = re.search("(.*) (\w+) (-?\d+) if (.*) (.*) (-?\d+)", line)
    register_names.add(match.group(1))
    register_names.add(match.group(4))
    operations.append({
        "target_register": match.group(1),
        "direction": match.group(2),
        "target_value": int(match.group(3)),
        "conditional_register": match.group(4),
        "condition": match.group(5),
        "condition_value": int(match.group(6))
    })

registers = {}
for name in register_names:
    registers[name] = 0

max_overall_value = 0
for op in operations:
    if eval("{} {} {}".format(registers[op['conditional_register']], op['condition'], op['condition_value'])):
        if op['direction'] == "inc":
            registers[op['target_register']] += op['target_value']
        else:
            registers[op['target_register']] -= op['target_value']
    max_overall_value = max(max_overall_value, registers[op['target_register']])

print(max_overall_value)
