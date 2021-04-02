import unittest
from unittest.mock import patch, MagicMock, call

from ch3_11.ask_question import AskQuestion
from ch3_11.currency_convertor import CurrencyConvertor


def result_should_be(mock_print, result):
    mock_print.assert_called_with(result)


def supported_currencies_should_be(mock_print, supported_currencies):
    mock_print.assert_called_with(supported_currencies)


def when_ask_for_currency_convert_info(convertor):
    ask_question = AskQuestion(convertor)
    ask_question.ask()


def given_currency_convert_info(mock_input):
    mock_input.side_effect = ['GBP', 'JPY', '25']


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_convert_result = {
            "success": True,
            "query": {
                "from": "GBP",
                "to": "JPY",
                "amount": 25
            },
            "info": {
                "timestamp": 1519328414,
                "rate": 148.972231
            },
            "historical": "",
            "date": "2018-02-22",
            "result": 3724.305775
        }
        self.mock_supported_symbols = {
            "success": True,
            "symbols": {
                "AED": "United Arab Emirates Dirham",
                "AFN": "Afghan Afghani",
                "ALL": "Albanian Lek",
                "AMD": "Armenian Dram",
                "GBP": "British Pound Sterling",
                "JPY": "Japanese Yen"
            }
        }

    @patch('ch3_11.currency_convertor.requests')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_ask_currency_convert_from_and_to(self, mock_input, mock_print, mock_requests):
        convertor = self.given_supported_currencies(mock_requests)
        self.given_convert_result(mock_requests)
        given_currency_convert_info(mock_input)
        when_ask_for_currency_convert_info(convertor)
        supported_currencies_should_be(mock_print, self.mock_supported_symbols['symbols'])
        self.currency_convert_info_should_be(convertor, 'GBP', 'JPY', 25.00)
        convertor.convert()
        result_should_be(mock_print, '25.00 GBP dollars at an exchange rate of 148.97 is 3724.31 JPY dollars')

    def currency_convert_info_should_be(self, convertor, convert_from, convert_to, amount):
        self.assertEqual(convert_from, convertor.currency_from)
        self.assertEqual(convert_to, convertor.currency_to)
        self.assertEqual(amount, convertor.amount)

    def given_convert_result(self, mock_requests):
        mock_requests.get.return_value.json.return_value = self.mock_convert_result

    def given_supported_currencies(self, mock_requests):
        mock_requests.get.return_value.json.return_value = self.mock_supported_symbols
        convertor = CurrencyConvertor()
        convertor.load_supported_currencies()
        return convertor


if __name__ == '__main__':
    unittest.main()
