import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('ch4_15.bcrypt')
    @patch('builtins.print')
    @patch('builtins.password')
    @patch('builtins.input')
    def test_password_validation(self, mock_input, mock_password, mock_print, mock_bcrypt):
        mock_input.return_value = 'username'
        mock_password.return_value = 'password'
        username, password = ask_input_for_question()
        validator = PasswordValidator()
        mock_bcrypt.hashpw.assert_called()
        validator.validate(username, password)
        mock_print.assert_called_with('Welcome!')
        mock_input.return_value = 'username'
        mock_password.return_value = 'incorrect password'
        username, password = ask_input_for_question()
        validator.validate(username, password)
        mock_print.assert_called_with('I don\'t know you.')


if __name__ == '__main__':
    unittest.main()
