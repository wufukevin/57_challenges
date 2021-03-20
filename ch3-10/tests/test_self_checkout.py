import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.input')
    def test_ask_for_input(self, mock_input):
        mock_input.side_effect = ['25', '2']
        checker = SelfCheckOut()
        checker.ask_for_price_and_quantity()
        mock_input.return_value = 'n'
        checker.ask_for_continue()
        self.assertEqual(1, checker.items_count())


if __name__ == '__main__':
    unittest.main()
