import unittest
from unittest.mock import patch, call

from utils.questioner import Questioner
from utils.validators import to_float


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input')
    def test_wisconsin_state(self, mock_input, mock_print):
        questioner = Questioner().add_question('What is the order amount?', to_float) \
            .add_question('What state do you live in?')
        mock_input.side_effect = ['10', 'Wisconsin', 'Eau Claire']
        (amount, state) = questioner.ask()
        ask_more_questions_by_state(questioner, state)
        (county,) = questioner.ask()
        calculator = TaxCalculator()
        calculator.calculate(amount, state, county)
        mock_print.assert_has_calls([
            call('The tax is $0.50.'),
            call('The total is $10.50.')
        ])


if __name__ == '__main__':
    unittest.main()
