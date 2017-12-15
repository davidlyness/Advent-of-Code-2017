# coding=utf-8
"""Advent of Code 2017, Day 15, Part 2"""


def generator_a(current_value):
    """
    Generate values for Generator A
    :param current_value: seed value for generator
    """
    while True:
        current_value = (current_value * 16807) % 2147483647
        if current_value % 4 == 0:
            yield current_value


def generator_b(current_value):
    """
    Generate values for Generator B
    :param current_value: seed value for generator
    """
    while True:
        current_value = (current_value * 48271) % 2147483647
        if current_value % 8 == 0:
            yield current_value


a_values = generator_a(516)
b_values = generator_b(190)
num_matches = 0

for _ in range(5000000):
    current_a = next(a_values)
    current_b = next(b_values)
    if str(format(current_a, "016b"))[-16:] == str(format(current_b, "016b"))[-16:]:
        num_matches += 1

print(num_matches)
