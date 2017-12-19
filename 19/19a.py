# coding=utf-8
"""Advent of Code 2017, Day 19, Part 1"""

with open("input.txt") as f:
    grid = f.readlines()

direction = "down"
current_char = "|"
x_position = (grid[0].index("|"))
y_position = 0
letters = ""

while current_char != " ":
    if direction == "up":
        y_position -= 1
    elif direction == "down":
        y_position += 1
    elif direction == "left":
        x_position -= 1
    elif direction == "right":
        x_position += 1
    current_char = grid[y_position][x_position]
    if current_char.isalpha():
        letters += current_char
    elif current_char == "+":
        if direction in ("up", "down"):
            if grid[y_position][x_position - 1] != " ":
                direction = "left"
            else:
                direction = "right"
        else:
            if grid[y_position - 1][x_position] != " ":
                direction = "up"
            else:
                direction = "down"

print(letters)
