import unittest
from unittest.mock import patch, call

from tax.multistate_tax import ask_more_questions_by_state
from utils.convertors import to_float, to_state
from utils.questioner import Questioner


class TaxCalculator:
    def calculate(self, amount, state, county):
        tax_mapping = {
            'Wisconsin,eau claire': 0.05,
            'Wisconsin,dunn': 0.04,
            'Illinos,': 0.08
        }
        sub_total = 0
        tax = tax_mapping.get(','.join([state, '' if county is None else county]), 0)
        if tax > 0:
            sub_total = tax * amount
            print(f'The tax is ${sub_total :.2f}.')
        total_amount = amount + sub_total
        print(f'The total is ${total_amount:.2f}.')


def prepare_questions():
    questioner = Questioner().add_question('What is the order amount?', to_float) \
        .add_question('What state do you live in?', to_state)
    return questioner


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
