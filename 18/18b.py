# coding=utf-8
"""Advent of Code 2017, Day 18, Part 2"""

with open("input.txt") as f:
    instructions = [x.split(" ") for x in f.read().rstrip("\n").split("\n")]


class Program:
    """
    An instance of a Program.
    """

    def __init__(self, program_number):
        self.registers = dict.fromkeys([instruction[1] for instruction in instructions if instruction[1].isalpha()], 0)
        self.registers['p'] = program_number
        self.instruction_index = 0
        self.message_queue = []
        self.is_waiting = False
        self.num_values_sent = 0

    def get_value(self, input_value):
        """
        Determine the register or numeric value of the input.
        :param input_value: register or number to inspect
        :return: value of register or number
        """
        if input_value.isalpha():
            return self.registers[input_value]
        else:
            return int(input_value)

    def run_instruction(self):
        """
        Run a single instruction for the program.
        :return: a message if emitted; None otherwise
        """
        message = None
        instruction = instructions[self.instruction_index]
        if instruction[0] == "snd":
            message = self.get_value(instruction[1])
            self.num_values_sent += 1
            self.instruction_index += 1
        elif instruction[0] == "set":
            self.registers[instruction[1]] = self.get_value(instruction[2])
            self.instruction_index += 1
        elif instruction[0] == "add":
            self.registers[instruction[1]] += self.get_value(instruction[2])
            self.instruction_index += 1
        elif instruction[0] == "mul":
            self.registers[instruction[1]] *= self.get_value(instruction[2])
            self.instruction_index += 1
        elif instruction[0] == "mod":
            self.registers[instruction[1]] %= self.get_value(instruction[2])
            self.instruction_index += 1
        elif instruction[0] == "rcv":
            if len(self.message_queue) > 0:
                self.registers[instruction[1]] = self.message_queue.pop(0)
                self.instruction_index += 1
                self.is_waiting = False
            else:
                self.is_waiting = True
        elif instruction[0] == "jgz":
            if self.get_value(instruction[1]) > 0:
                self.instruction_index += self.get_value(instruction[2])
            else:
                self.instruction_index += 1
        return message


program_0 = Program(0)
program_1 = Program(1)
active_program = 0

while not (program_0.is_waiting and program_1.is_waiting):
    if active_program == 0:
        program_message = program_0.run_instruction()
        if program_message is not None:
            program_1.message_queue.append(program_message)
        active_program = 1
    else:
        program_message = program_1.run_instruction()
        if program_message is not None:
            program_0.message_queue.append(program_message)
        active_program = 0

print(program_1.num_values_sent)
