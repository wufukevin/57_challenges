import unittest
from unittest.mock import patch


class SimpleMath(object):
    def __init__(self):
        self.second_input = 0
        self.first_input = 0

    def ask_two_numbers(self):
        self.first_input = input("What is the first number? ")
        self.second_input = input("What is the second number? ")


class MyTestCase(unittest.TestCase):
    @patch("builtins.input")
    def test_ask_input_two_numbers(self, mock_input):
        mock_input.side_effect = ["1", "2"]
        simple_math = SimpleMath()
        simple_math.ask_two_numbers()
        self.assertEqual("1", simple_math.first_input)
        self.assertEqual("2", simple_math.second_input)


if __name__ == '__main__':
    unittest.main()
