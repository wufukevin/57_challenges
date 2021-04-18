import unittest
from unittest.mock import patch, call

from ch4_17.bac_checker import BACChecker, ask_question


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_bac_in_imperial(self, mock_input, mock_print):
        mock_input.side_effect = ['5', '80', 'M', '60']
        checker = BACChecker()
        checker.check(*ask_question())
        mock_print.assert_has_calls([call('Your BAC is 0.08'),
                                     call('It is not legal for you to drive.')])


if __name__ == '__main__':
    unittest.main()
