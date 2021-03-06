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

    @patch("retirement_calculation.retirement_calculation.current_year")
    @patch("builtins.print")
    @patch("builtins.input")
    def test_retirement_calculation_with_example_age(self, mock_input, mock_print, mock_year):
        mock_year.return_value = 2015
        input_current_age(mock_input, 25)
        self.calculator.ask_current_age()
        input_retire_age(mock_input, 65)
        self.calculator.ask_retire_age()
        self.calculator.show_years_left()
        years_left_should_be(mock_print, 'You have 40 years left until you can retire.')
        self.calculator.show_retire_year()
        retire_year_should_be(mock_print, "It\'s 2015, so you can retire in 2055.")

    @patch("retirement_calculation.retirement_calculation.current_year")
    @patch("builtins.print")
    @patch("builtins.input")
    def test_current_age_30_retire_age_50(self, mock_input, mock_print, mock_year):
        mock_year.return_value = 2000
        input_current_age(mock_input, 30)
        self.calculator.ask_current_age()
        input_retire_age(mock_input, 50)
        self.calculator.ask_retire_age()
        self.calculator.show_years_left()
        years_left_should_be(mock_print, 'You have 20 years left until you can retire.')
        self.calculator.show_retire_year()
        retire_year_should_be(mock_print, "It\'s 2000, so you can retire in 2020.")


if __name__ == '__main__':
    unittest.main()
