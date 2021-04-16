import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_driving_age(self, mock_print, mock_input):
        mock_input.return_value = '15'
        age = ask_question()
        assistant = DrivingAssistant()
        assistant.check_age(age)
        mock_print.assert_called_with('You are not old enough to legally drive.')
        mock_input.return_value = '35'
        age = ask_question()
        assistant.check_age(age)
        mock_print.assert_called_with('You are old enough to legally drive.')


if __name__ == '__main__':
    unittest.main()
