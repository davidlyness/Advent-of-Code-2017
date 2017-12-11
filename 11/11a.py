# coding=utf-8
"""Advent of Code 2017, Day 11, Part 1"""


def step(start, direction):
    """
    Determines the next position on the hexagonal grid after taking a step.
    :param start: the starting position in the grid
    :param direction: the direction in which to move
    :return: new position
    """
    x, y = start
    if direction == "n":
        return x, y - 1
    elif direction == "s":
        return x, y + 1
    elif direction == "ne":
        if x % 2 == 0:
            return x + 1, y - 1
        else:
            return x + 1, y
    elif direction == "sw":
        if x % 2 == 1:
            return x - 1, y + 1
        else:
            return x - 1, y
    elif direction == "nw":
        if x % 2 == 0:
            return x - 1, y - 1
        else:
            return x - 1, y
    elif direction == "se":
        if x % 2 == 1:
            return x + 1, y + 1
        else:
            return x + 1, y


def get_distance_from_origin(position):
    """
    Determines the minimum number of steps needed to return to the origin from a position on the hexagonal grid.
    :param position: the starting position to measure from
    :return: minimum number of steps to return to origin
    """
    num_steps = 0
    while position != (0, 0):
        x_position, y_position = position
        if x_position == 0:
            if y_position > 0:
                position = step(position, "n")
            else:
                position = step(position, "s")
        else:
            if x_position > 0:
                if y_position >= 0:
                    position = step(position, "nw")
                else:
                    position = step(position, "sw")
            else:
                if y_position >= 0:
                    position = step(position, "ne")
                else:
                    position = step(position, "se")
        num_steps += 1
    return num_steps


with open("input.txt") as f:
    moves = f.read().split(",")

current_position = (0, 0)
for move in moves:
    current_position = step(current_position, move)

print(get_distance_from_origin(current_position))
