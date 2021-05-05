import unittest
from unittest.mock import patch, MagicMock

from utils.questioner import Questioner, InfiniteQuestioner, NotSupportedError, AskMode


def given_convertor(convertor, result):
    convertor.side_effect = result
    return convertor


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


def when_build_question(mock_convertor, questioner, question, retry):
    questioner.add_question(question, convertor=mock_convertor, retry=retry)


def when_ask_question(questioner):
    answers = questioner.ask()
    return answers


def given_convertor_exception(convertor):
    convertor.side_effect = Exception


def test_question_generator(question_count):
    count = 0
    while count < question_count:
        yield '', None, False
        count += 1


def empty_question_generator():
    yield from ()


class TestQuestioner(unittest.TestCase):
    def setUp(self):
        self.infinite_questioner = InfiniteQuestioner()
        self.retry = True
        self.mock_convertor = MagicMock()
        self.questioner = Questioner()
        self.wrong_answers = 'wrong answers'
        self.question = 'question'
        self.valid_input = 'valid input'
        self.not_retry = False

    def test_questioner_with_empty_questions(self):
        answers = self.questioner.ask()
        self.assertTupleEqual(answers, tuple())

    @patch('builtins.input')
    def test_questioner_get_answer_with_convertor_without_retry(self, mock_input):
        convertor = given_convertor(self.mock_convertor, [self.valid_input])
        given_answers(mock_input, [self.valid_input])
        when_build_question(convertor, self.questioner, self.question, self.not_retry)
        self.questions_should_be(self.questioner, [(self.question, convertor, self.not_retry)])
        answers = when_ask_question(self.questioner)
        self.answers_should_be(answers, (self.valid_input,))
        convertor.reset_mock()
        given_convertor_exception(convertor)
        mock_input.reset_mock()
        given_answers(mock_input, self.wrong_answers)
        self.should_raise_exception_when_ask(self.questioner)

    @patch('builtins.input')
    def test_questioner_get_answer_with_convertor_with_retry(self, mock_input):
        convertor = given_convertor(self.mock_convertor, [Exception, self.valid_input])
        given_answers(mock_input, [self.wrong_answers, self.valid_input])
        when_build_question(convertor, self.questioner, self.question, self.retry)
        self.questions_should_be(self.questioner, [(self.question, convertor, self.retry)])
        answers = when_ask_question(self.questioner)
        self.answers_should_be(answers, (self.valid_input,))
        self.assertEqual(2, mock_input.call_count)
        self.assertEqual(2, self.mock_convertor.call_count)

    @patch('builtins.input')
    def test_infinite_questioner_with_non_empty_generator(self, mock_input):
        self.should_raise_not_supported_exception_when_ask()
        self.when_set_question_generator(test_question_generator(3))
        given_answers(mock_input, ['1', 'a', ''])
        answers = self.when_infinite_questioner_ask()
        self.answers_should_be(answers, ('1', 'a', ''))

    @patch('builtins.input')
    def test_infinite_questioner_1_by_1(self, mock_input):
        given_answers(mock_input, ['1', 'a', ''])
        self.when_set_question_generator(test_question_generator(3))
        answers = self.when_infinite_questioner_ask_1_by_1()
        self.answers_should_be(answers, ('1', 'a', ''))

    def test_infinite_questioner_with_empty_generator(self):
        self.when_set_question_generator(empty_question_generator())
        answers = self.when_infinite_questioner_ask()
        self.answers_should_be(answers, tuple())

    def when_infinite_questioner_ask(self):
        answers = self.infinite_questioner.ask()
        return answers

    def when_set_question_generator(self, generator):
        self.infinite_questioner.set_question_generator(generator)

    def should_raise_not_supported_exception_when_ask(self):
        with self.assertRaises(NotSupportedError) as exception:
            self.infinite_questioner.add_question('some question')
        self.assertEqual('add_question is not supported', str(exception.exception))

    def when_infinite_questioner_ask_1_by_1(self):
        answers = tuple(answer for answer in self.infinite_questioner.ask(AskMode.OneByOne))
        return answers

    def should_raise_exception_when_ask(self, questioner):
        with self.assertRaises(Exception):
            questioner.ask()

    def answers_should_be(self, answers, expected_answers):
        self.assertTupleEqual(answers, expected_answers)

    def questions_should_be(self, questioner, questions):
        self.assertListEqual(questions, questioner.questions)


if __name__ == '__main__':
    unittest.main()
