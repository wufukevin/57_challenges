import unittest
from unittest.mock import patch


class SimpleMath(object):
    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.second_input = None
        self.first_input = None

    def ask_two_numbers(self):
        self.first_input = input("What is the first number? ")
        self.first_number = int(self.first_input)
        self.second_input = input("What is the second number? ")
        self.second_number = int(self.second_input)

    def calculate(self):
        add_statement = f'{self.first_number} + {self.second_number} = {self.first_number + self.second_number}'
        subtract_statement = f'{self.first_number} - {self.second_number} = {self.first_number - self.second_number}'
        multiply_statement = f'{self.first_number} * {self.second_number} = {self.first_number * self.second_number}'
        divide_statement = f'{self.first_number} / {self.second_number} = {int(self.first_number / self.second_number)}'
        print(f'{add_statement}\n{subtract_statement}\n{multiply_statement}\n{divide_statement}')


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.simple_math = SimpleMath()

    @patch("builtins.input")
    def test_ask_input_two_numbers(self, mock_input):
        mock_input.side_effect = ["1", "2"]
        self.simple_math.ask_two_numbers()
        self.input_should_be("1", "2")
        self.assertEqual(1, self.simple_math.first_number)
        self.assertEqual(2, self.simple_math.second_number)

    @patch("builtins.input")
    def test_ask_input_not_numbers(self, mock_input):
        mock_input.side_effect = ["a", "2"]
        with self.assertRaises(Exception):
            self.simple_math.ask_two_numbers()
        mock_input.side_effect = ["1", "a"]
        with self.assertRaises(Exception):
            self.simple_math.ask_two_numbers()

    @patch("builtins.print")
    @patch("builtins.input")
    def test_calculate(self, mock_input, mock_print):
        mock_input.side_effect = ["10", "5"]
        self.simple_math.ask_two_numbers()
        self.simple_math.calculate()
        mock_print.assert_called_with("10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2")

    def input_should_be(self, first, second):
        self.assertEqual(first, self.simple_math.first_input)
        self.assertEqual(second, self.simple_math.second_input)


if __name__ == '__main__':
    unittest.main()
