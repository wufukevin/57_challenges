from enum import Enum

GRAMS_PER_KILOGRAM = 1000

KILOGRAMS_PER_POUNDS = 0.45359

INCHES_PER_FEET = 12

CMS_PER_METER = 100

POUNDS_PER_STONE = 14

CMS_PER_INCHES = 2.54


class Questioner:
    def __init__(self):
        self.questions = []

    def build_question(self, question, convertor, retry=False):
        self.questions.append((question, convertor, retry))
        return self

    def ask(self):
        answers = []
        for question, convertor, retry in self.questions:
            while True:
                try:
                    answer = input(question)
                    if convertor is not None:
                        answer = convertor(answer)
                    answers.append(answer)
                    break
                except Exception as e:
                    if not retry:
                        raise e
        return tuple(answers)


def to_enum(input_content, enum):
    input_in_lower_case = input_content.lower()
    for unit in enum:
        value_in_lower_case = unit.value.lower()
        if input_in_lower_case == value_in_lower_case or value_in_lower_case.startswith(input_in_lower_case, 0, 1):
            return unit
    raise Exception


def to_measure_unit(input_content):
    return to_enum(input_content, MeasureUnit)


def to_float(input_content):
    return float(input_content)


def to_imperial_length_unit(input_content):
    return to_enum(input_content, ImperialLengthUnit)


def to_imperial_weight_unit(input_content):
    return to_enum(input_content, ImperialWeightUnit)


def to_metric_length_unit(input_content):
    return to_enum(input_content, MetricLengthUnit)


def to_metric_weight_unit(input_content):
    return to_enum(input_content, MetricWeightUnit)


class MeasureUnit(Enum):
    Imperial = 'Imperial'
    Metric = 'Metric'


class ImperialLengthUnit(Enum):
    Feet = 'Feet'
    Inches = 'Inches'

    def to_inches(self, length):
        if self == ImperialLengthUnit.Feet:
            return length * INCHES_PER_FEET
        return length


class ImperialWeightUnit(Enum):
    Pounds = 'Pounds'
    Stones = 'Stones'

    def to_pounds(self, weight):
        if self == ImperialWeightUnit.Stones:
            return weight * POUNDS_PER_STONE
        return weight


class MetricLengthUnit(Enum):
    Meter = 'Meter'
    Centimeter = 'Centimeter'

    def to_inches(self, length):
        if self == MetricLengthUnit.Meter:
            return length * CMS_PER_METER / CMS_PER_INCHES
        return length / CMS_PER_INCHES


class MetricWeightUnit(Enum):
    Kilogram = 'Kilogram'
    Gram = 'Gram'

    def to_pounds(self, weight):
        if self == MetricWeightUnit.Kilogram:
            return weight / KILOGRAMS_PER_POUNDS
        return weight / GRAMS_PER_KILOGRAM / KILOGRAMS_PER_POUNDS


class BMIEvaluator:
    def evaluate(self, *params):
        length_unit, length, weight_unit, weight = params
        length_in_inches = length_unit.to_inches(length)
        weight_in_pounds = weight_unit.to_pounds(weight)
        bmi = (weight_in_pounds / pow(length_in_inches, 2)) * 703
        print(f'Your BMI is {bmi:.1f}.')
        if bmi < 18.5:
            print('You are underweight the ideal weight. Go to see the doctor.')
        elif bmi > 25:
            print('You are overweight the ideal weight. Go to see the doctor.')
        else:
            print('You are within the ideal weight range.')


def prepare_question(measure_unit):
    if measure_unit == MeasureUnit.Imperial:
        # Builder pattern
        return Questioner() \
            .build_question('Select the unit of the height, F)Feet or I)Inches? ',
                            convertor=to_imperial_length_unit,
                            retry=True) \
            .build_question('Please input the height: ', convertor=to_float, retry=True) \
            .build_question('Select the unit of the weight, P)Pounds or S)Stones? ', convertor=to_imperial_weight_unit,
                            retry=True) \
            .build_question('Please input the weight: ', convertor=to_float, retry=True)
    else:
        return Questioner() \
            .build_question('Select the unit of the height, M)Meter or C)Centimeter? ',
                            convertor=to_metric_length_unit,
                            retry=True) \
            .build_question('Please input the height: ', convertor=to_float, retry=True) \
            .build_question('Select the unit of the weight, K)Kilogram or G)Gram? ', convertor=to_metric_weight_unit,
                            retry=True) \
            .build_question('Please input the weight: ', convertor=to_float, retry=True)


if __name__ == '__main__':
    questioner = Questioner().build_question('Select a measure unit, I)Imperial or M)Metric? ',
                                             convertor=to_measure_unit, retry=True)
    measure_unit, = questioner.ask()
    questioner = prepare_question(measure_unit)
    answers = questioner.ask()
    bmi_evaluator = BMIEvaluator()
    bmi_evaluator.evaluate(*answers)
