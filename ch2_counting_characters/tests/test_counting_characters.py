import unittest
from unittest.mock import patch

from ch2_counting_characters.character_counter import CharacterCounter


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

    @patch("builtins.input")
    def test_count_empty(self, mock_input):
        mock_input.return_value = ""
        counter = CharacterCounter()
        counter.ask_input()
        self.assertEqual("", counter.word)
        self.assertEqual("No input detected!", counter.count_result())


if __name__ == '__main__':
    unittest.main()
