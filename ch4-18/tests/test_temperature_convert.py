import unittest
from unittest.mock import patch

from ch4_18.temperature_convert import ask_question, TemperatureConvertor


def given_input(mock_input, input_mode, input_temperature):
    mock_input.side_effect = [input_mode, input_temperature]


def given_questions():
    mode, temperature = ask_question()
    return mode, temperature


def result_should_be(mock_print, expected):
    mock_print.assert_called_with(expected)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.convertor = TemperatureConvertor()

    @patch('builtins.print')
    @patch('builtins.input')
    def test_convert_from_F_to_C(self, mock_input, mock_print):
        given_input(mock_input, 'F', '32')
        mode, temperature = given_questions()
        self.when_convert(mode, temperature)
        result_should_be(mock_print, 'The temperature in Celsius is 0.00.')
        mock_input.reset()
        given_input(mock_input, 'f', '32')
        mode, temperature = given_questions()
        self.when_convert(mode, temperature)
        result_should_be(mock_print, 'The temperature in Celsius is 0.00.')

    def when_convert(self, mode, temperature):
        self.convertor.convert(mode, temperature)


if __name__ == '__main__':
    unittest.main()
