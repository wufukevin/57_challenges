import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_convert_from_F_to_C(self, mock_input, mock_print):
        mock_input.side_effect = ['F', '32']
        mode, temperature = ask_question()
        convertor = TemperatureConvertor()
        convertor.convert(mode, temperature)
        mock_print.assert_called_with('The temperature in Celsius is 0.')


if __name__ == '__main__':
    unittest.main()
