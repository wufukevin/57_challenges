import unittest
from unittest.mock import patch

from retirement_calculation.retirement_calculation import RetirementCalculator


class MyTestCase(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input")
    def test_retirement_calculation(self, mock_input, mock_print):
        mock_input.side_effect = [25, 65]
        calculator = RetirementCalculator()
        calculator.ask_current_age()
        calculator.ask_retire_age()
        calculator.show_years_left()
        mock_print.assert_called_with('You have 40 years left until you can retire.')
        calculator.show_retire_year()
        mock_print.assert_called_with("It\'s 2015, so you can retire in 2055.")


if __name__ == '__main__':
    unittest.main()
