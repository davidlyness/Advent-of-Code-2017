# coding=utf-8
"""Advent of Code 2017, Day 16, Part 2"""

with open("input.txt") as f:
    moves = f.read().rstrip("\n").split(",")

programs = list("abcdefghijklmnop")
total_programs = len(programs)

seen_programs = []
dance_num = 1
total_dances = 1000000000
cycle_traversed = False

while dance_num < total_dances:
    for move in moves:
        if move[0] == "s":
            num_programs = int(move[1:])
            programs = programs[-num_programs:] + programs[:total_programs - num_programs]
        elif move[0] == "x":
            position1, position2 = map(int, move[1:].split("/"))
            program1, program2 = programs[position1], programs[position2]
            programs[position1] = program2
            programs[position2] = program1
        elif move[0] == "p":
            program1, program2 = move[1:].split("/")
            for i in range(total_programs):
                if programs[i] == program1:
                    programs[i] = program2
                elif programs[i] == program2:
                    programs[i] = program1
    if programs in seen_programs and not cycle_traversed:
        cycle_length = dance_num - seen_programs.index(programs) - 1
        dance_num = total_dances - (total_dances % cycle_length)
        cycle_traversed = True
    else:
        seen_programs.append(programs)
    dance_num += 1

print("".join(programs))
