# coding=utf-8
"""Advent of Code 2017, Day 25, Part 1"""

turing_machine_rules = {
    ("a", 0): (1, "R", "b"),
    ("a", 1): (1, "L", "e"),
    ("b", 0): (1, "R", "c"),
    ("b", 1): (1, "R", "f"),
    ("c", 0): (1, "L", "d"),
    ("c", 1): (0, "R", "b"),
    ("d", 0): (1, "R", "e"),
    ("d", 1): (0, "L", "c"),
    ("e", 0): (1, "L", "a"),
    ("e", 1): (0, "R", "d"),
    ("f", 0): (1, "R", "a"),
    ("f", 1): (1, "R", "c"),
}

tape = {}
current_state = "a"
current_position = 0

for _ in range(12459852):
    if current_position in tape:
        current_value = tape.get(current_position)
    else:
        current_value = 0
    new_value, direction, new_state = turing_machine_rules.get((current_state, current_value))
    tape[current_position] = new_value
    if direction == "R":
        current_position += 1
    else:
        current_position -= 1
    current_state = new_state

print(sum(tape.values()))
