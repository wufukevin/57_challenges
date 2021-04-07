import unittest
from unittest.mock import call, patch

from ch4_14.check_tax import CheckTax
from ch4_14.ask_input import ask_input_of_question


def given_tax_checker():
    check_tax = CheckTax()
    return check_tax


def given_inputs(mock_inputs, inputs):
    mock_inputs.side_effect = inputs
    amount, state = ask_input_of_question('4-14')
    return amount, state


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.checker = given_tax_checker()

    @patch('builtins.print')
    @patch('builtins.input')
    def test_check_tax_of_not_wisconsin(self, mock_inputs, mock_print):
        amount, state = given_inputs(mock_inputs, ['10', 'MN'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The total is $10.00.')])

    @patch('builtins.print')
    @patch('builtins.input')
    def test_check_tax_of_wisconsin(self, mock_input, mock_print):
        amount, state = given_inputs(mock_input, ['10', 'WI'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The subtotal is $10.00.'),
                                     call('The tax is $0.55.'),
                                     call('The total is $10.55.')])
        mock_print.reset_mock()
        amount, state = given_inputs(mock_input, ['10', 'wi'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The subtotal is $10.00.'),
                                     call('The tax is $0.55.'),
                                     call('The total is $10.55.')])
        mock_print.reset_mock()
        amount, state = given_inputs(mock_input, ['10', 'Wisconsin'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The subtotal is $10.00.'),
                                     call('The tax is $0.55.'),
                                     call('The total is $10.55.')])
        mock_print.reset_mock()
        amount, state = given_inputs(mock_input, ['10', 'wisconsin'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The subtotal is $10.00.'),
                                     call('The tax is $0.55.'),
                                     call('The total is $10.55.')])
        mock_print.reset_mock()
        amount, state = given_inputs(mock_input, ['10', 'WiScOnSiN'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The subtotal is $10.00.'),
                                     call('The tax is $0.55.'),
                                     call('The total is $10.55.')])
        mock_print.reset_mock()
        amount, state = given_inputs(mock_input, ['10', 'wI'])
        self.checker.check(amount, state)
        mock_print.assert_has_calls([call('The subtotal is $10.00.'),
                                     call('The tax is $0.55.'),
                                     call('The total is $10.55.')])


if __name__ == '__main__':
    unittest.main()
