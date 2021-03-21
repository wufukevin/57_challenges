import unittest
from unittest.mock import patch, call

from ch3_10.self_checkout import ask_for_continue, SelfCheckOut


def given_price_and_quantity(mock_input, price_and_quantity):
    mock_input.side_effect = price_and_quantity


def given_continue_input_price_and_quantity(mock_input, continue_or_not):
    mock_input.reset_mock(return_value=True, side_effect=True)
    mock_input.return_value = continue_or_not


def should_prompt_price_and_quantity(mock_input, price_and_quantity_prompted):
    mock_input.assert_has_calls(price_and_quantity_prompted)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.checker = SelfCheckOut()

    @patch('builtins.input')
    def test_ask_for_input_one_item(self, mock_input):
        given_price_and_quantity(mock_input, ['25', '2'])
        self.when_ask_for_input_price_and_quantity()
        should_prompt_price_and_quantity(mock_input, [call('Enter the price of item 1: '),
                                                      call('Enter the quantity of item 1: ')])
        given_continue_input_price_and_quantity(mock_input, 'n')
        self.should_not_continue(ask_for_continue())
        self.items_should_has_count(1)

    @patch('builtins.input')
    def test_ask_for_input_three_item(self, mock_input):
        given_price_and_quantity(mock_input, ['25', '2'])
        self.when_ask_for_input_price_and_quantity()
        should_prompt_price_and_quantity(mock_input, [call('Enter the price of item 1: '),
                                                      call('Enter the quantity of item 1: ')])
        given_continue_input_price_and_quantity(mock_input, 'y')
        self.assertEqual(True, ask_for_continue())
        given_price_and_quantity(mock_input, ['10', '1'])
        self.when_ask_for_input_price_and_quantity()
        should_prompt_price_and_quantity(mock_input, [call('Enter the price of item 2: '),
                                                      call('Enter the quantity of item 2: ')])
        given_continue_input_price_and_quantity(mock_input, 'y')
        self.assertEqual(True, ask_for_continue())
        given_price_and_quantity(mock_input, ['4', '1'])
        self.when_ask_for_input_price_and_quantity()
        should_prompt_price_and_quantity(mock_input, [call('Enter the price of item 3: '),
                                                      call('Enter the quantity of item 3: ')])
        given_continue_input_price_and_quantity(mock_input, 'n')
        self.should_not_continue(ask_for_continue())
        self.items_should_has_count(3)

    @patch('builtins.input')
    def test_checkout(self, mock_input):
        given_price_and_quantity(mock_input, ['25', '2'])
        self.when_ask_for_input_price_and_quantity()
        given_continue_input_price_and_quantity(mock_input, 'y')
        self.assertEqual(True, ask_for_continue())
        given_price_and_quantity(mock_input, ['10', '1'])
        self.when_ask_for_input_price_and_quantity()
        given_continue_input_price_and_quantity(mock_input, 'y')
        self.assertEqual(True, ask_for_continue())
        given_price_and_quantity(mock_input, ['4', '1'])
        self.when_ask_for_input_price_and_quantity()
        given_continue_input_price_and_quantity(mock_input, 'n')
        self.should_not_continue(ask_for_continue())
        self.checker.checkout()
        self.assertEqual('64.00', self.checker.subtotal)
        self.assertEqual('3.52', self.checker.tax)
        self.assertEqual('67.52', self.checker.total)

    def items_should_has_count(self, expected_count):
        self.assertEqual(expected_count, self.checker.items_count())

    def should_not_continue(self, continue_or_not):
        self.assertEqual(False, continue_or_not)

    def when_ask_for_input_price_and_quantity(self):
        self.checker.ask_for_price_and_quantity()


if __name__ == '__main__':
    unittest.main()
