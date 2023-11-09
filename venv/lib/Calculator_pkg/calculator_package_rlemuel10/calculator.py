"""
This module performs the following functions:
Addition / Subtraction.
Multiplication / Division.
Take (n) root of a number.
Reset memory (Calculator must have its own memory, meaning it should manipulate
its starting number 0 until it is reset.). This means that, for example,
calculator should perform actions with a value inside its memory
"""

import math
from typing import Union


class Calculator:
    def __init__(self, starting_number=0):
        self.number_in_memory = starting_number
        # Class can be started with zero in memory, or with a specific number

    # Each arithmetic function has its own method
    # Fsum is used instead of sum for accuracy, and all outputs default to float
    def add(self, addend: float) -> float:
        self.number_in_memory = math.fsum([self.number_in_memory, addend])
        if math.isclose(self.number_in_memory, round(self.number_in_memory)):
            return float(round(self.number_in_memory))
        return self.number_in_memory

    def subtract(self, subtrahend: float) -> float:
        self.number_in_memory = math.fsum([self.number_in_memory, -subtrahend])
        return self.number_in_memory

    def multiply(self, multiplier: float) -> float:
        self.number_in_memory = self.number_in_memory * multiplier
        return self.number_in_memory

    def divide(self, denominator: float) -> Union[float, str]:
        try:
            self.number_in_memory = self.number_in_memory / denominator
            return self.number_in_memory
        except ZeroDivisionError:
            return "Can't divide by zero, try another number"
        # Method doesn't allow division by zero, user can try again

    def root(self, nth_root: float) -> Union[float, str]:
        try:
            self.number_in_memory = self.number_in_memory ** (1 / nth_root)
        except ZeroDivisionError:
            return "Zero-th root doesn't exist"
        if math.isclose(self.number_in_memory, math.ceil(self.number_in_memory)):
            return float(math.ceil(self.number_in_memory))
        else:
            return self.number_in_memory
        # Root method computes root, rounding to nearest float if needed

    def reset_memory(self) -> int:
        self.number_in_memory = 0
        return self.number_in_memory

    # Method resets memory as needed
