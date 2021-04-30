import unittest
from unittest.mock import patch, call

from tax.multistate_tax import ask_more_questions_by_state, TaxCalculator, prepare_questions


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


def when_calculate_tax(calculator, amount, county, state):
    calculator.calculate(amount, state, county)


def given_tax_calculator():
    calculator = TaxCalculator()
    return calculator


def when_ask_county(questioner):
    (county,) = questioner.ask()
    return county


def when_ask_state_and_amount(questioner):
    (amount, state) = questioner.ask()
    return amount, state


def result_should_be(mock_print, result):
    mock_print.assert_has_calls(result)


class TestTaxCalculator(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_wisconsin_state(self, mock_input, mock_print):
        questioner = prepare_questions()
        given_answers(mock_input, ['10', 'Wisconsin', 'Eau Claire'])
        amount, state = when_ask_state_and_amount(questioner)
        ask_more_questions_by_state(questioner, state)
        county = when_ask_county(questioner)
        calculator = given_tax_calculator()
        when_calculate_tax(calculator, amount, county, state)
        result_should_be(mock_print, [
            call('The tax is $0.50.'),
            call('The total is $10.50.')
        ])

    @patch('builtins.print')
    @patch('builtins.input')
    def test_illinois_state(self, mock_input, mock_print):
        questioner = prepare_questions()
        given_answers(mock_input, ['10', 'Illinois'])
        amount, state = when_ask_state_and_amount(questioner)
        ask_more_questions_by_state(questioner, state)
        county = when_ask_county(questioner)
        calculator = given_tax_calculator()
        when_calculate_tax(calculator, amount, county, state)
        result_should_be(mock_print, [
            call('The tax is $0.80.'),
            call('The total is $10.80.')
        ])

    @patch('builtins.print')
    @patch('builtins.input')
    def test_other_state(self, mock_input, mock_print):
        questioner = prepare_questions()
        given_answers(mock_input, ['10', 'New York'])
        amount, state = when_ask_state_and_amount(questioner)
        ask_more_questions_by_state(questioner, state)
        county = when_ask_county(questioner)
        calculator = given_tax_calculator()
        when_calculate_tax(calculator, amount, county, state)
        result_should_be(mock_print, [
            call('The total is $10.00.')
        ])


if __name__ == '__main__':
    unittest.main()
