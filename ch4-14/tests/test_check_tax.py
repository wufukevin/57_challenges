import unittest
from unittest.mock import call, patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_check_tax_of_not_wisconsin(self, mock_inputs, mock_print):
        mock_inputs.side_effect = ['10', 'MN']
        amount, state = ask_input_of_question('4-14')
        check_tax = CheckTax(amount, state)
        check_tax.check()
        mock_print.assert_has_calls([call('The total is $10.00')])


if __name__ == '__main__':
    unittest.main()
