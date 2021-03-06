import unittest
from unittest.mock import patch

from retirement_calculation.retirement_calculation import RetirementCalculator


def input_retire_age(mock_input, retire_age):
    mock_input.return_value = retire_age


def input_current_age(mock_input, current_age):
    mock_input.return_value = current_age


def years_left_should_be(mock_print, expected):
    mock_print.assert_called_with(expected)


def retire_year_should_be(mock_print, expected):
    mock_print.assert_called_with(expected)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = RetirementCalculator()

    @patch("builtins.print")
    @patch("builtins.input")
    def test_retirement_calculation(self, mock_input, mock_print):
        input_current_age(mock_input, 25)
        self.calculator.ask_current_age()
        input_retire_age(mock_input, 65)
        self.calculator.ask_retire_age()
        self.calculator.show_years_left()
        years_left_should_be(mock_print, 'You have 40 years left until you can retire.')
        self.calculator.show_retire_year()
        retire_year_should_be(mock_print, "It\'s 2015, so you can retire in 2055.")


if __name__ == '__main__':
    unittest.main()
