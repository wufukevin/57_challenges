import unittest
from unittest.mock import patch

from counting_characters.counter import CharacterCounter


def given_input_word(mock_input, input_word):
    mock_input.return_value = input_word


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.counter = CharacterCounter()

    @patch("builtins.input")
    def test_count_homer(self, mock_input):
        given_input_word(mock_input, "Homer")
        self.counter.ask_input()
        self.input_word_should_be("Homer")
        self.count_result_should_be("Homer has 5 characters.")

    def count_result_should_be(self, result):
        self.assertEqual(result, self.counter.count_result())

    @patch("builtins.input")
    def test_count_python(self, mock_input):
        given_input_word(mock_input, "Python")
        self.counter.ask_input()
        self.input_word_should_be("Python")
        self.count_result_should_be("Python has 6 characters.")

    @patch("builtins.input")
    def test_count_empty(self, mock_input):
        given_input_word(mock_input, "")
        self.counter.ask_input()
        self.input_word_should_be("")
        self.count_result_should_be("No input detected!")

    def input_word_should_be(self, expected):
        self.assertEqual(expected, self.counter.word)


if __name__ == '__main__':
    unittest.main()
