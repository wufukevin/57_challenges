from enum import Enum


class Gender(Enum):
    Male = 'M'
    Female = 'F'


class MeasureType(Enum):
    Metrics = '1'
    Imperial = '2'


def get_alcohol_consume(measure_type, alcohol_consumed):
    return alcohol_consumed if measure_type == MeasureType.Imperial else alcohol_consumed * 1000 / 28.34952


def get_weight(measure_type, weight):
    return weight if measure_type == MeasureType.Imperial else weight * 1000 / 453.5924


class BACChecker:
    def check(self, *params):
        measure_type, alcohol_consumed, weight, gender, time_passed_in_minutes = params
        # BAC = (A × 5.14 / W × r) − .015 × H
        bac = (get_alcohol_consume(measure_type, alcohol_consumed) * 5.14 / get_weight(measure_type, weight) * (
            0.73 if gender == Gender.Male else 0.66)) - 0.15 * time_passed_in_minutes / 60
        print(f'Your BAC is {bac:.2f}')
        print('It is not legal for you to drive.' if bac >= 0.08 else 'It is legal for you to drive.')


def ask_question():
    def float_convertor(f):
        return float(f)

    def gender_convertor(g):
        return Gender(g)

    def measure_convertor(m):
        return MeasureType(m)

    return (question['convertor'](input(question['content'])) for question in
            [
                {'content': 'Select measure type: 1)Metric 2)Imperial', 'convertor': measure_convertor},
                {'content': 'How many alcohol do you consumed? ', 'convertor': float_convertor},
                {'content': 'What is your weight? ', 'convertor': float_convertor},
                {'content': 'What is your gender(M/F)? ', 'convertor': gender_convertor},
                {'content': 'How long from your last drink in minutes? ', 'convertor': float_convertor}
            ])
