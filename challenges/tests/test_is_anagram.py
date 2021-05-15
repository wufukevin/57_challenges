import unittest
from unittest.mock import patch

from challenges.anagram_checker import AnagramChecker, given_questioner


def report_should_be(mock_print, expected):
    mock_print.assert_called_once_with(expected)


def given_input_strings(mock_input, input_strings):
    mock_input.side_effect = input_strings


def given_answers(questioner):
    first_string, second_string = questioner.ask()
    return first_string, second_string


class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.questioner = given_questioner()
        self.anagram_checker = AnagramChecker()

    @patch('builtins.print')
    @patch('builtins.input')
    def test_is_anagram(self, mock_input, mock_print):
        questioner = given_questioner()
        given_input_strings(mock_input, ['note', 'tone'])
        first_string, second_string = given_answers(questioner)
        is_anagram = self.when_check_is_anagram(first_string, second_string)
        self.is_anagram_should_be(is_anagram, True)
        self.anagram_checker.report(is_anagram)
        report_should_be(mock_print, '"note" and "tone" are anagrams.')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_not_anagram(self, mock_input, mock_print):
        given_input_strings(mock_input, ['not', 'tone'])
        first_string, second_string = given_answers(self.questioner)
        is_anagram = self.when_check_is_anagram(first_string, second_string)
        self.is_anagram_should_be(is_anagram, False)
        self.when_checker_report(is_anagram)
        report_should_be(mock_print, '"not" and "tone" are not anagrams.')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_not_anagram2(self, mock_input, mock_print):
        given_input_strings(mock_input, ['abcd', 'tone'])
        first_string, second_string = given_answers(self.questioner)
        is_anagram = self.when_check_is_anagram(first_string, second_string)
        self.is_anagram_should_be(is_anagram, False)
        self.when_checker_report(is_anagram)
        report_should_be(mock_print, '"abcd" and "tone" are not anagrams.')

    def when_checker_report(self, is_anagram):
        self.anagram_checker.report(is_anagram)

    def is_anagram_should_be(self, is_anagram, expected):
        self.assertEqual(expected, is_anagram)

    def when_check_is_anagram(self, first_string, second_string):
        is_anagram = self.anagram_checker.is_anagram(first_string, second_string)
        return is_anagram


if __name__ == '__main__':
    unittest.main()
