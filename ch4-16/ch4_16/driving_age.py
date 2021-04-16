LEGAL_DRIVING_AGE = 16


def ask_question():
    return input('What is your age? ')


class DrivingAssistant:
    def check_age(self, age_str):
        try:
            age = int(age_str)
            if age < 0:
                raise Exception()
        except Exception:
            print('The format of the age is not correct!')
            return
        print(
            'You are not old enough to legally drive.' if age < LEGAL_DRIVING_AGE else 'You are old enough to legally drive.')


if __name__ == '__main__':
    age = ask_question()
    assistant = DrivingAssistant()
    assistant.check_age(age)
