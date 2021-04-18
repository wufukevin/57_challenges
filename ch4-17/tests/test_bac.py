import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_bac_in_imperial(self, mock_input, mock_print):
        mock_input.side_effect = ['5', '80', 'M', '60']
        checker = BACChecker()
        checker.check(*ask_question())
        mock_print.assert_called_once_with('It is not legal for you to drive.')


if __name__ == '__main__':
    unittest.main()
