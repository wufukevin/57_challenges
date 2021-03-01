import unittest
from unittest.mock import Mock, patch


class CharacterCounter(object):
    def __init__(self):
        self.word = None

    def ask_input(self):
        self.word = input("What is the input string?")

    def count_result(self):
        return self.word + " has " + str(len(self.word)) + " characters."


class MyTestCase(unittest.TestCase):
    @patch("builtins.input")
    def test_count_homer(self, mock_input):
        mock_input.return_value = "Homer"
        counter = CharacterCounter()
        counter.ask_input()
        self.assertEqual("Homer", counter.word)
        self.assertEqual("Homer has 5 characters.", counter.count_result())

    @patch("builtins.input")
    def test_count_python(self, mock_input):
        mock_input.return_value = "Python"
        counter = CharacterCounter()
        counter.ask_input()
        self.assertEqual("Python", counter.word)
        self.assertEqual("Python has 6 characters.", counter.count_result())


if __name__ == '__main__':
    unittest.main()
