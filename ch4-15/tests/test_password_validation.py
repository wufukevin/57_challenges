import unittest
from unittest.mock import patch

from ch4_15.password_validation import PasswordValidator, ask_input_for_question


def given_username_and_password(mock_getpass, mock_input, username, password):
    mock_input.return_value = username
    mock_getpass.return_value = password
    username, password = ask_input_for_question()
    return password, username


def credentials_should_be_encrypted(mock_bcrypt):
    mock_bcrypt.hashpw.assert_called()


def result_should_be(mock_print, result):
    mock_print.assert_called_with(result)


def given_password_not_match(mock_bcrypt):
    mock_bcrypt.checkpw.return_value = False


class MyTestCase(unittest.TestCase):
    @patch('ch4_15.password_validation.bcrypt')
    @patch('builtins.print')
    @patch('ch4_15.password_validation.getpass')
    @patch('builtins.input')
    def test_password_validation(self, mock_input, mock_getpass, mock_print, mock_bcrypt):
        password, username = given_username_and_password(mock_getpass, mock_input, 'username', 'password')
        self.given_password_validator()
        credentials_should_be_encrypted(mock_bcrypt)
        self.when_validate(password, username)
        result_should_be(mock_print, 'Welcome!')
        password, username = given_username_and_password(mock_getpass, mock_input, 'username', 'incorrect password')
        mock_print.reset_mock()
        given_password_not_match(mock_bcrypt)
        self.when_validate(password, username)
        result_should_be(mock_print, 'I don\'t know you.')
        password, username = given_username_and_password(mock_getpass, mock_input, 'not exist user', 'any password')
        mock_print.reset_mock()
        self.when_validate(password, username)
        result_should_be(mock_print, 'I don\'t know you.')

    def given_password_validator(self):
        self.validator = PasswordValidator()

    def when_validate(self, password, username):
        self.validator.validate(username, password)


if __name__ == '__main__':
    unittest.main()
