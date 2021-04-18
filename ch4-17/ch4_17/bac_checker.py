from enum import Enum


class Gender(Enum):
    Male = 'M'
    Female = 'F'


class BACChecker:
    def check(self, *params):
        alcohol_consumed, weight, gender, time_passed_in_minutes = params
        # BAC = (A × 5.14 / W × r) − .015 × H
        bac = (alcohol_consumed * 5.14 / weight * (
            0.73 if gender == Gender.Male else 0.66)) - 0.15 * time_passed_in_minutes / 60
        print(f'Your BAC is {bac:.2f}')
        print('It is not legal for you to drive.' if bac >= 0.08 else 'It is legal for you to drive.')


def ask_question():
    def float_convertor(f):
        return float(f)

    def gender_convertor(g):
        return Gender(g)

    return (question['convertor'](input(question['content'])) for question in
            [
                {'content': 'How many ounces alcohol do you consumed? ', 'convertor': float_convertor},
                {'content': 'What is your weight in pounds? ', 'convertor': float_convertor},
                {'content': 'What is your gender(M/F)? ', 'convertor': gender_convertor},
                {'content': 'How long from your last drink in minutes? ', 'convertor': float_convertor}
            ])
