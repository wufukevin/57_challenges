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
    def setUp(self):
        self.simple_math = SimpleMath()

    @patch("builtins.input")
    def test_ask_input_two_numbers(self, mock_input):
        mock_input.side_effect = ["1", "2"]
        self.simple_math.ask_two_numbers()
        self.input_should_be("1", "2")

    def input_should_be(self, first, second):
        self.assertEqual(first, self.simple_math.first_input)
        self.assertEqual(second, self.simple_math.second_input)


if __name__ == '__main__':
    unittest.main()
