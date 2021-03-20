import unittest
from unittest.mock import patch

from ch3_10.self_checkout import ask_for_continue, SelfCheckOut


def given_price_and_quantity(mock_input, price_and_quantity):
    mock_input.side_effect = price_and_quantity


def given_continue_input_price_and_quantity(mock_input, continue_or_not):
    mock_input.reset_mock(return_value=True, side_effect=True)
    mock_input.return_value = continue_or_not


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.checker = SelfCheckOut()

    @patch('builtins.input')
    def test_ask_for_input(self, mock_input):
        given_price_and_quantity(mock_input, ['25', '2'])
        self.when_ask_for_input_price_and_quantity()
        given_continue_input_price_and_quantity(mock_input, 'n')
        self.should_continue(ask_for_continue())
        self.items_should_has_count(1)

    def items_should_has_count(self, expected_count):
        self.assertEqual(expected_count, self.checker.items_count())

    def should_continue(self, continue_or_not):
        self.assertEqual(False, continue_or_not)

    def when_ask_for_input_price_and_quantity(self):
        self.checker.ask_for_price_and_quantity()


if __name__ == '__main__':
    unittest.main()
