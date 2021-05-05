import unittest
from unittest.mock import patch

from find_max.find_max import generate_question, FindMax
from utils.questioner import InfiniteQuestioner


def given_infinite_questioner(question_generator):
    infinite_questioner = InfiniteQuestioner().set_question_generator(question_generator=question_generator)
    return infinite_questioner


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


def when_find_from_infinite_questioner(find_max, infinite_questioner):
    max_of_inputs = find_max.find(infinite_questioner)
    return max_of_inputs


def given_find_max_object():
    find_max = FindMax()
    return find_max


class TestFindMax(unittest.TestCase):
    @patch('builtins.input')
    def test_find_max(self, mock_input):
        infinite_questioner = given_infinite_questioner(generate_question(3))
        given_answers(mock_input, ['10', '20', 'n'])
        find_max = given_find_max_object()
        max_of_inputs = when_find_from_infinite_questioner(find_max, infinite_questioner)
        self.max_of_input_should_be(max_of_inputs, 20)

    def max_of_input_should_be(self, max_of_inputs, expected):
        self.assertEqual(expected, max_of_inputs)


if __name__ == '__main__':
    unittest.main()
