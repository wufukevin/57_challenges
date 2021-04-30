from enum import Enum


class Questioner:
    def __init__(self):
        self.questions = []

    def add_question(self, question, validator, retry):
        self.questions.append((question, validator, retry))
        return self

    def ask(self):
        answers = []
        for question, validator, retry in self.questions:
            while True:
                try:
                    answer = input(question)
                    if validator is not None:
                        answer = validator(answer)
                    answers.append(answer)
                    break
                except:
                    if not retry:
                        break
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


def to_imperial_length(input_content):
    return to_enum(input_content, ImperialLength)


def to_imperial_weight(input_content):
    return to_enum(input_content, ImperialWeight)


class MeasureUnit(Enum):
    Imperial = 'Imperial'
    Metric = 'Metric'


class ImperialLength(Enum):
    Feet = 'Feet'
    Inches = 'Inches'


class ImperialWeight(Enum):
    Ponds = 'Ponds'
    Stones = 'Stones'
