# coding=utf-8
"""Advent of Code 2017, Day 18, Part 1"""

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


def run_program():
    """
    Run program up to the first valid `rcv` instruction.
    :return: value emitted by the first valid `rcv` instruction
    """
    i = 0
    current_frequency = None
    while 0 <= i < len(instructions):
        instruction = instructions[i]
        if instruction[0] == "snd":
            current_frequency = get_value(instruction[1])
            i += 1
        elif instruction[0] == "set":
            registers[instruction[1]] = get_value(instruction[2])
            i += 1
        elif instruction[0] == "add":
            registers[instruction[1]] += get_value(instruction[2])
            i += 1
        elif instruction[0] == "mul":
            registers[instruction[1]] *= get_value(instruction[2])
            i += 1
        elif instruction[0] == "mod":
            registers[instruction[1]] %= get_value(instruction[2])
            i += 1
        elif instruction[0] == "rcv":
            if get_value(instruction[1]) != 0:
                return current_frequency
            i += 1
        elif instruction[0] == "jgz":
            if get_value(instruction[1]) > 0:
                i += get_value(instruction[2])
            else:
                i += 1


print(run_program())
