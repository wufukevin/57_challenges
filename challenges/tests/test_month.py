import unittest
from unittest.mock import patch

from type.month import Month, prepare_questions


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


def when_ask(questioner):
    (language, input_month) = questioner.ask()
    return input_month, language


class TestMonth(unittest.TestCase):
    @patch('builtins.input')
    def test_valid_month(self, mock_input):
        questioner = prepare_questions()
        given_answers(mock_input, ['1', '6'])
        input_month, language = when_ask(questioner)
        self.month_should_be(input_month, language, 'June')
        mock_input.reset_mock()
        given_answers(mock_input, ['2', '10'])
        input_month, language = when_ask(questioner)
        self.month_should_be(input_month, language, '十月')

    @patch('builtins.input')
    def test_invalid_month(self, mock_input):
        questioner = prepare_questions()
        given_answers(mock_input, ['1', '13'])
        input_month, language = when_ask(questioner)
        self.month_should_be(input_month, language, 'unknown')

    def month_should_be(self, input_month, language, expected):
        month = Month(language, input_month)
        self.assertEqual(expected, str(month))


if __name__ == '__main__':
    unittest.main()
