import unittest
from unittest.mock import patch


def ask_for_continue():
    more_price_and_quantity = input('More price and quantity? (y/N)')
    return more_price_and_quantity.lower() == 'y'


class SelfCheckOut(object):
    def __init__(self):
        self.items = []

    def ask_for_price_and_quantity(self):
        price = int(input('Enter the price of item 1: '))
        quantity = int(input('Enter the quantity of item 1: '))
        self.items.append({'price': price, 'quantity': quantity})

    def items_count(self):
        return len(self.items)


class MyTestCase(unittest.TestCase):
    @patch('builtins.input')
    def test_ask_for_input(self, mock_input):
        mock_input.side_effect = ['25', '2']
        checker = SelfCheckOut()
        checker.ask_for_price_and_quantity()
        mock_input.reset_mock(return_value=True, side_effect=True)
        mock_input.return_value = 'n'
        continue_or_not = ask_for_continue()
        self.assertEqual(False, continue_or_not)
        self.assertEqual(1, checker.items_count())


if __name__ == '__main__':
    unittest.main()
