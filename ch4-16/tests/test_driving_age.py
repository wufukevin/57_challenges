import unittest
from unittest.mock import patch

from ch4_16.driving_age import ask_question, DrivingAssistant


def given_input_age(mock_input, age):
    mock_input.return_value = age
    age = ask_question()
    return age


def result_should_be(mock_print, result):
    mock_print.assert_called_with(result)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driving_assistant = DrivingAssistant()

    @patch('builtins.input')
    @patch('builtins.print')
    def test_driving_age(self, mock_print, mock_input):
        age = given_input_age(mock_input, '15')
        self.when_check_driving_age(age)
        result_should_be(mock_print, 'You are not old enough to legally drive.')
        age = given_input_age(mock_input, '35')
        self.when_check_driving_age(age)
        result_should_be(mock_print, 'You are old enough to legally drive.')

    @patch('builtins.input')
    @patch('builtins.print')
    def test_input_incorrect_age(self, mock_print, mock_input):
        age = given_input_age(mock_input, 'abc')
        self.when_check_driving_age(age)
        result_should_be(mock_print, 'The format of the age is not correct!')
        age = given_input_age(mock_input, '-1')
        self.when_check_driving_age(age)
        result_should_be(mock_print, 'The format of the age is not correct!')

    def when_check_driving_age(self, age):
        self.driving_assistant.check_age(age)


if __name__ == '__main__':
    unittest.main()
