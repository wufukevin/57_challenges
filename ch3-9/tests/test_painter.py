import unittest
from unittest.mock import patch


class Painter(object):
    def __init__(self):
        self.width = None
        self.length = None

    def ask_for_length_and_width(self):
        self.length = int(input('Please input length: '))
        self.width = int(input('Please input width: '))


def given_input_length_and_width(mock_input, input):
    mock_input.side_effect = input


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.painter = Painter()

    @patch('builtins.input')
    def test_ask_length_and_width(self, mock_input):
        given_input_length_and_width(mock_input, ['20', '18'])
        self.painter.ask_for_length_and_width()
        self.length_and_width_should_be(20, 18)

    def length_and_width_should_be(self, length, width):
        self.assertEqual(length, self.painter.length)
        self.assertEqual(width, self.painter.width)


if __name__ == '__main__':
    unittest.main()
