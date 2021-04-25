from enum import Enum


class Gender(Enum):
    Male = 'M'
    Female = 'F'


class MeasureUnit(Enum):
    Metrics = '1'
    Imperial = '2'


def get_alcohol_consume(measure_unit, alcohol_consumed):
    return alcohol_consumed if measure_unit == MeasureUnit.Imperial else alcohol_consumed * 1000 / 28.34952


def get_weight(measure_unit, weight):
    return weight if measure_unit == MeasureUnit.Imperial else weight * 1000 / 453.5924


class BACChecker:
    def check(self, *params):
        measure_unit, alcohol_consumed, weight, gender, time_passed_in_minutes = params
        time_passed_in_hours = time_passed_in_minutes / 60
        # BAC = (A × 5.14 / W × r) − .015 × H
        bac = (get_alcohol_consume(measure_unit, alcohol_consumed) * 5.14 / get_weight(measure_unit, weight) * (
            0.73 if gender == Gender.Male else 0.66)) - 0.15 * time_passed_in_hours
        print(f'Your BAC is {bac:.2f}')
        print('It is not legal for you to drive.' if bac >= 0.08 else 'It is legal for you to drive.')


def ask_question():
    def float_convertor(f):
        return float(f)

    def gender_convertor(g):
        return Gender(g)

    def measure_convertor(m):
        return MeasureUnit(m)

    return (question['convertor'](input(question['content'])) for question in
            [
                {'content': 'Select measure unit: 1)Metric 2)Imperial', 'convertor': measure_convertor},
                {'content': 'How many alcohol do you consumed? ', 'convertor': float_convertor},
                {'content': 'What is your weight? ', 'convertor': float_convertor},
                {'content': 'What is your gender(M/F)? ', 'convertor': gender_convertor},
                {'content': 'How long from your last drink in minutes? ', 'convertor': float_convertor}
            ])
