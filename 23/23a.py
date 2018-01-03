# coding=utf-8
"""Advent of Code 2017, Day 23, Part 1"""

with open("input.txt") as f:
    instructions = [x.split(" ") for x in f.read().rstrip("\n").split("\n")]
registers = dict.fromkeys([instruction[1] for instruction in instructions if instruction[1].isalpha()], 0)


def get_value(input_value):
    """
    Determine the register or numeric value of the input.
    :param input_value: register or number to inspect
    :return: value of register or number
    """
    if input_value.isalpha():
        return registers[input_value]
    else:
        return int(input_value)


def get_num_mul_instructions():
    """
    Run the program, counting the number of `mul` instructions executed.
    :return: the number of `mul` instructions executed
    """
    i = 0
    num_mul = 0
    while 0 <= i < len(instructions):
        instruction = instructions[i]
        if instruction[0] == "set":
            registers[instruction[1]] = get_value(instruction[2])
            i += 1
        elif instruction[0] == "sub":
            registers[instruction[1]] -= get_value(instruction[2])
            i += 1
        elif instruction[0] == "mul":
            num_mul += 1
            registers[instruction[1]] *= get_value(instruction[2])
            i += 1
        elif instruction[0] == "jnz":
            if get_value(instruction[1]) != 0:
                i += get_value(instruction[2])
            else:
                i += 1
    return num_mul


print(get_num_mul_instructions())
