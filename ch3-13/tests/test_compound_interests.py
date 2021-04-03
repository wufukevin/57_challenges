import unittest
from unittest.mock import patch

from ch3_13.compound_interests import CompoundInterestCalculator, ask_question


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_compound_interests(self, mock_input, mock_print):
        mock_input.side_effect = ['1500', '4.3', '6', '4']
        calculator = CompoundInterestCalculator()
        calculator.calculate_compound_interest(*ask_question())
        mock_print.assert_called_with('$1500.00 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.')


if __name__ == '__main__':
    unittest.main()
