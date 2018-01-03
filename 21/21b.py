# coding=utf-8
"""Advent of Code 2017, Day 21, Part 2"""


def convert_string_to_grid(grid_string):
    """
    Convert the string representation of the grid to a 2D array.
    :param grid_string: input string
    :return: 2D representation of the grid
    """
    return list(map(list, grid_string.split("/")))


def convert_grid_to_string(grid):
    """
    Convert the 2D representation of the grid to a string.
    :param grid: input 2D array
    :return: string representation of the grid
    """
    return "/".join("".join(row) for row in grid)


with open("input.txt") as f:
    puzzle_input = f.read().rstrip().split("\n")
rules = {}
for line in puzzle_input:
    rule_input, rule_output = line.split(" => ")
    for flip_count in range(2):
        for rotation_count in range(4):
            equivalent_rule_input = convert_string_to_grid(rule_input)
            grid_rule_length = len(equivalent_rule_input)
            for _ in range(flip_count):
                equivalent_rule_input = [list(reversed(row)) for row in equivalent_rule_input]
            for _ in range(rotation_count):
                temp_grid = [[None] * grid_rule_length for _ in range(grid_rule_length)]
                for i in range(grid_rule_length):
                    for j in range(grid_rule_length):
                        temp_grid[i][j] = equivalent_rule_input[- j - 1][i]
                equivalent_rule_input = temp_grid
            rules[convert_grid_to_string(equivalent_rule_input)] = rule_output

current_pattern = [
    [".", "#", "."],
    [".", ".", "#"],
    ["#", "#", "#"]
]

for _ in range(18):
    grid_length = len(current_pattern)
    if grid_length % 2 == 0:
        new_grid_length = grid_length // 2 * 3
        split_length = 2
        iterated_split_length = 3
    else:
        new_grid_length = grid_length // 3 * 4
        split_length = 3
        iterated_split_length = 4
    output_grid = [[None] * new_grid_length for _ in range(new_grid_length)]
    for i in range(0, grid_length // split_length):
        for j in range(0, grid_length // split_length):
            start_i = i * split_length
            start_j = j * split_length
            new_grid = [row[start_j:start_j + split_length] for row in current_pattern[start_i:start_i + split_length]]
            new_grid_string = convert_grid_to_string(new_grid)
            transformed_new_grid = convert_string_to_grid(rules[new_grid_string])
            output_i = i * iterated_split_length
            output_j = j * iterated_split_length
            for a in range(iterated_split_length):
                for b in range(iterated_split_length):
                    output_grid[output_i + a][output_j + b] = transformed_new_grid[a][b]
    current_pattern = output_grid
print(convert_grid_to_string(current_pattern).count("#"))
