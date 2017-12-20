# coding=utf-8
"""Advent of Code 2017, Day 20, Part 1"""

import re


class Particle:
    """
    An instance of a Particle.
    """

    def __init__(self, line):
        match = re.search("p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>", line)
        self.position = int(match.group(1)), int(match.group(2)), int(match.group(3))
        self.velocity = int(match.group(4)), int(match.group(5)), int(match.group(6))
        self.acceleration = int(match.group(7)), int(match.group(8)), int(match.group(9))

    def update_state(self):
        """
        Update the velocity and position of the particle.
        """
        self.velocity = tuple([sum(n) for n in zip(self.velocity, self.acceleration)])
        self.position = tuple([sum(n) for n in zip(self.position, self.velocity)])

    def distance_from_origin(self):
        """
        Determine the distance of the particle from the origin.
        :return: Manhattan distance of the particle from the origin
        """
        return sum(abs(n) for n in self.position)


with open("input.txt") as f:
    puzzle_input = f.read().rstrip().split("\n")

particles = {i: Particle(puzzle_input[i]) for i in range(len(puzzle_input))}

for _ in range(1000):
    for p in particles:
        particles[p].update_state()

min_distance = min([p.distance_from_origin() for p in particles.values()])
for p in particles:
    if particles[p].distance_from_origin() == min_distance:
        print(p)
