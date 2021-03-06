import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch("datetime.date.today")
    @patch("builtins.input")
    def test_retirement_calculation(self, mock_input, mock_today):
        mock_input.side_effect = [25, 65]
        mock_today.year.return_value = 2015
        calculator = RetirementCalculator()
        calculator.ask_current_age()
        calculator.ask_retire_age()
        self.assertEqual('You have 40 years left until you can retire.', calculator.show_years_left())
        self.assertEqual('It\'s 2015, so you can retire in 2055.', calculator.show_retire_year())


if __name__ == '__main__':
    unittest.main()
