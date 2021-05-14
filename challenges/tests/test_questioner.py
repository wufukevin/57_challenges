import unittest
from unittest.mock import patch, MagicMock

from utils.questioner import Questioner, NotSupportedError, AskMode, QuestionIterator, SimpleQuestionIterator


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


class test_question_generator(QuestionIterator):
    def __init__(self, question_count):
        super().__init__()
        self.question_count = question_count

    def __next__(self):
        if self._current_question_index >= self.question_count:
            raise StopIteration
        self._current_question_index += 1
        return '', None, False


class EmptyQuestionIterator(QuestionIterator):
    pass


class TestQuestionIterator(SimpleQuestionIterator):
    def add_question(self, question, convertor, retry):
        return super().add_question(question, convertor, retry)


class TestQuestioner(unittest.TestCase):
    def setUp(self):
        self.infinite_questioner = Questioner()
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
        answers = when_ask_question(self.questioner)
        self.answers_should_be(answers, (self.valid_input,))
        self.assertEqual(2, mock_input.call_count)
        self.assertEqual(2, self.mock_convertor.call_count)

    @patch('builtins.input')
    def test_infinite_questioner_with_non_empty_generator(self, mock_input):
        self.when_set_question_iterator(test_question_generator(3))
        given_answers(mock_input, ['1', 'a', ''])
        answers = self.when_infinite_questioner_ask()
        self.answers_should_be(answers, ('1', 'a', ''))

    @patch('builtins.input')
    def test_infinite_questioner_1_by_1(self, mock_input):
        given_answers(mock_input, ['1', 'a', ''])
        self.when_set_question_iterator(test_question_generator(3))
        answers = self.when_infinite_questioner_ask_1_by_1()
        self.answers_should_be(answers, ('1', 'a', ''))

    def test_infinite_questioner_with_empty_generator(self):
        self.when_set_question_iterator(EmptyQuestionIterator())
        answers = self.when_infinite_questioner_ask()
        self.answers_should_be(answers, tuple())

    def test_question_iterator(self):
        question_iterator = SimpleQuestionIterator()
        question_iterator = question_iterator.add_question('question', None, False)
        question_added = [(question, convertor, retry) for question, convertor, retry in question_iterator]
        self.assertListEqual(question_added, question_iterator.questions)

    def when_infinite_questioner_ask(self):
        answers = self.infinite_questioner.ask()
        return answers

    def when_set_question_iterator(self, iterator):
        self.infinite_questioner.add_question_iterator(iterator)

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


if __name__ == '__main__':
    unittest.main()
