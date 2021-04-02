import json
import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('ch3_11.currency_convertor.requests')
    @patch('builtins.input')
    def test_ask_currency_convert_from_and_to(self, mock_input, mock_requests):
        convertor = CurrencyConvertor()
        mock_requests.return_value = {
            "success": True,
            "symbols": {
                "GBP": "British Pound Sterling",
                "JPY": "Japanese Yen",
            }
        }
        convertor.load_supported_currencies()
        ask_question = AskQuestion(convertor)
        mock_input.side_effect = ['GBP', 'JPY', '25']
        ask_question.ask()
        self.assertEqual('GBP', convertor.currency_from)
        self.assertEqual('JPY', convertor.currency_to)
        self.assertEqual(25.00, convertor.amount)
        self.assertEqual(3724.31, convertor.convert())


if __name__ == '__main__':
    unittest.main()
