import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.input')
    def test_ask_length_and_width(self, mock_input):
        painter = Painter()
        mock_input.side_effect = ['20', '18']
        painter.ask_for_length_and_width()
        self.assertEqual(20, painter.length)
        self.assertEqual(18, painter.width)


if __name__ == '__main__':
    unittest.main()
