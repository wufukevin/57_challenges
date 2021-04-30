import unittest
from unittest.mock import patch, call, MagicMock

from utils.questioner import Questioner


def given_validator(validator, result):
    validator.side_effect = result
    return validator


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


def when_build_question(mock_convertor, questioner, question, retry):
    questioner.add_question(question, convertor=mock_convertor, retry=retry)


def when_ask_question(questioner):
    answers = questioner.ask()
    return answers


def given_validator_exception(validator):
    validator.side_effect = Exception


class TestQuestioner(unittest.TestCase):
    def setUp(self):
        self.retry = True
        self.mock_convertor = MagicMock()
        self.questioner = Questioner()
        self.wrong_answers = 'wrong answers'
        self.question = 'question'
        self.valid_input = 'valid input'
        self.not_retry = False

    @patch('builtins.input')
    def test_questioner_get_answer_with_validator_without_retry(self, mock_input):
        convertor = given_validator(self.mock_convertor, [self.valid_input])
        given_answers(mock_input, [self.valid_input])
        when_build_question(convertor, self.questioner, self.question, self.not_retry)
        self.questions_should_be(self.questioner, [(self.question, convertor, self.not_retry)])
        answers = when_ask_question(self.questioner)
        self.answers_should_be(answers, (self.valid_input,))
        convertor.reset_mock()
        given_validator_exception(convertor)
        mock_input.reset_mock()
        given_answers(mock_input, self.wrong_answers)
        self.should_raise_exception_when_ask(self.questioner)

    @patch('builtins.input')
    def test_questioner_get_answer_with_validator_with_retry(self, mock_input):
        convertor = given_validator(self.mock_convertor, [Exception, self.valid_input])
        given_answers(mock_input, [self.wrong_answers, self.valid_input])
        when_build_question(convertor, self.questioner, self.question, self.retry)
        self.questions_should_be(self.questioner, [(self.question, convertor, self.retry)])
        answers = when_ask_question(self.questioner)
        self.answers_should_be(answers, (self.valid_input,))
        self.assertEqual(2, mock_input.call_count)
        self.assertEqual(2, self.mock_convertor.call_count)

    def should_raise_exception_when_ask(self, questioner):
        with self.assertRaises(Exception):
            questioner.ask()

    def answers_should_be(self, answers, expected_answers):
        self.assertTupleEqual(answers, expected_answers)

    def questions_should_be(self, questioner, questions):
        self.assertListEqual(questions, questioner.questions)

    if __name__ == '__main__':
        unittest.main()
