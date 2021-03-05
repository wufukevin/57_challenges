import unittest
from unittest.mock import patch

from simple_math.simple_math import SimpleMath


def result_should_be(mock_print, expected):
    mock_print.assert_called_with(expected)


def given_input(mock_input, input_numbers):
    mock_input.side_effect = input_numbers


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.simple_math = SimpleMath()

    @patch("builtins.input")
    def test_ask_input_two_numbers(self, mock_input):
        given_input(mock_input, ["1", "2"])
        self.simple_math.ask_two_numbers()
        self.input_should_be("1", "2")
        self.first_number_should_be(1)
        self.second_number_should_be(2)

    def second_number_should_be(self, expected):
        self.assertEqual(expected, self.simple_math.second_number)

    def first_number_should_be(self, expected):
        self.assertEqual(expected, self.simple_math.first_number)

    @patch("builtins.input")
    def test_ask_input_not_numbers(self, mock_input):
        given_input(mock_input, ["a", "2"])
        self.should_raise_exception()
        given_input(mock_input, ["1", "a"])
        self.should_raise_exception()

    def should_raise_exception(self):
        with self.assertRaises(Exception):
            self.simple_math.ask_two_numbers()

    @patch("builtins.print")
    @patch("builtins.input")
    def test_calculate(self, mock_input, mock_print):
        mock_input.side_effect = ["10", "5"]
        self.simple_math.ask_two_numbers()
        self.simple_math.calculate()
        result_should_be(mock_print, "10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2")

    @patch("builtins.input")
    def test_input_negative_number(self, mock_input):
        mock_input.side_effect = ["-1", "5"]
        self.should_raise_exception()

    def input_should_be(self, first, second):
        self.assertEqual(first, self.simple_math.first_input)
        self.assertEqual(second, self.simple_math.second_input)


if __name__ == '__main__':
    unittest.main()
