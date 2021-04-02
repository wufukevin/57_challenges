import unittest
from unittest.mock import patch, call


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_simple_interest(self, mock_input, mock_print):
        mock_input.side_effect = ['1500', '4.3', '4']
        calculator = SimpleInterestCalculator()
        calculator.calculateSimpleInterest(ask_question())
        mock_print.assert_has_calls([
            call('After 1 years at 4.3%, the investment will be worth $1564.5.'),
            call('After 2 years at 4.3%, the investment will be worth $1629.'),
            call('After 3 years at 4.3%, the investment will be worth $1693.5.'),
            call('After 4 years at 4.3%, the investment will be worth $1758.')
        ])


if __name__ == '__main__':
    unittest.main()
