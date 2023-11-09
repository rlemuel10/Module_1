from calculator import Calculator
import unittest
import random

"""
Tests assess the following questions for each method:

Can calculator be created with/out a starting number in memory?
Can add use both positive and negative floats and ints?
Does subtract works with floats and ints?
Does multiply work as expected?
Does divide work with floats and ints, but not zero?
Does root function work for ints and floats?
"""


class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        self.instance1 = Calculator(45)
        self.instance2 = Calculator()
        self.assertEqual(
            self.instance1.number_in_memory, 45, "Should be 45"
        )
        self.assertEqual(self.instance2.number_in_memory, 0, "Should be 0")

    def test_add(self):
        near_zero_calculation = Calculator()
        decimal_calculation = Calculator()
        negative_values_test = [-5, -0.76, -1]  # = -6.76
        decimals = [0.1] * 10  # should be 1.0
        for number in negative_values_test:
            self.answer1 = near_zero_calculation.add(number)
        self.assertEqual(self.answer1, -6.76, "Should be -6.76")

        for entry in decimals:
            self.answer2 = decimal_calculation.add(entry)
        self.assertEqual(self.answer2, 1, "Should be 1.0")

    def test_subtract(self):
        float_integer_subtraction_calculation = Calculator()
        float_int_list = [3, -2.32, -19, 243.5]
        for i in float_int_list:
            self.answer3 = float_integer_subtraction_calculation.subtract(
                i
            )
        self.assertEqual(self.answer3, -225.18, "Should be -225.18")

    def test_root(self):
        nth_root_calculation = Calculator(500)
        random_root = random.uniform(1, 5)
        self.answer4 = nth_root_calculation.root(random_root)
        manual_calc = 500 ** (1 / random_root)
        self.assertEqual(self.answer4, manual_calc, "Should be the same")


if __name__ == "__main__":
    unittest.main()
