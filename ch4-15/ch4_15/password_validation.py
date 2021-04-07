from getpass import getpass

import bcrypt


def ask_input_for_question():
    username = input('What is your name? ')
    password = getpass('What is your password? ')
    return username, password


class PasswordValidator(object):
    def __init__(self):
        self.credentials = {
            'username': bcrypt.hashpw('password'.encode(), bcrypt.gensalt()),
        }

    def validate(self, username, password):
        if username not in self.credentials:
            print('I don\'t know you.')
            return

        if username in self.credentials:
            if bcrypt.checkpw(password.encode(), self.credentials[username]):
                print('Welcome!')
            else:
                print('I don\'t know you.')


if __name__ == '__main__':
    username, password = ask_input_for_question()
    validator = PasswordValidator()
    validator.validate(username, password)
