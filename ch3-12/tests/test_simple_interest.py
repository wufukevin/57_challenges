import unittest
from unittest.mock import patch, call

from ch3_12.simple_interest import SimpleInterestCalculator, ask_question


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_simple_interest(self, mock_input, mock_print):
        mock_input.side_effect = ['1500', '4.3', '4']
        calculator = SimpleInterestCalculator()
        interests = calculator.calculate_simple_interest(*ask_question())
        self.assertEqual(['1564.50', '1629.00', '1693.50', '1758.00'], interests)
        calculator.reports(interests)
        mock_print.assert_has_calls([
            call('After 1 year at 4.3 %, the investment will be worth $1564.50.'),
            call('After 2 years at 4.3 %, the investment will be worth $1629.00.'),
            call('After 3 years at 4.3 %, the investment will be worth $1693.50.'),
            call('After 4 years at 4.3 %, the investment will be worth $1758.00.')
        ])


if __name__ == '__main__':
    unittest.main()
