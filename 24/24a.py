# coding=utf-8
"""Advent of Code 2017, Day 24, Part 1"""

with open("input.txt") as f:
    components = [(int(p1), int(p2)) for p1, p2 in [line.strip().split("/") for line in f]]


def bridge_strength(bridge):
    """
    Calculates strength of a bridge.
    :param bridge: specified bridge
    :return: strength of bright
    """
    return sum([sum(component) for component in bridge])


def find_max_strength_bridge(existing_bridge, available_components, pins):
    """
    Determines the maximum possible strength from the available components.
    :param existing_bridge: components of bridge already assembled
    :param available_components: components available for use
    :param pins: component pins to match candidate components
    :return: bridge with the highest strength
    """
    max_strength_bridge = existing_bridge
    for current_component in available_components:
        if pins in current_component:
            if current_component[0] == pins:
                new_pins = current_component[1]
            else:
                new_pins = current_component[0]
            candidate_bridge = find_max_strength_bridge(existing_bridge + [current_component],
                                                        [c for c in available_components if current_component != c],
                                                        new_pins)
            if bridge_strength(candidate_bridge) > bridge_strength(max_strength_bridge):
                max_strength_bridge = candidate_bridge
    return max_strength_bridge


print(bridge_strength(find_max_strength_bridge([], components, 0)))
