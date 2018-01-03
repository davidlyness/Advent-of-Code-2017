# coding=utf-8
"""Advent of Code 2017, Day 22, Part 1"""

with open("input.txt") as f:
    puzzle_input = f.read().rstrip().split("\n")

direction = 0, -1
current_position = len(puzzle_input) // 2, len(puzzle_input[0]) // 2
infected = set()
num_infected_bursts = 0

for j, row in enumerate(puzzle_input):
    for i, char in enumerate(row):
        if char == "#":
            infected.add((i, j))

for _ in range(10000):
    if current_position in infected:
        direction = -direction[1], direction[0]
        infected.remove(current_position)
    else:
        direction = direction[1], -direction[0]
        infected.add(current_position)
        num_infected_bursts += 1
    current_position = current_position[0] + direction[0], current_position[1] + direction[1]

print(num_infected_bursts)
