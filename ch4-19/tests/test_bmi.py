import unittest
from unittest.mock import patch

from ch4_19.bmi import Questioner, to_float, MeasureUnit, ImperialLength, ImperialWeight, \
    to_imperial_length, to_imperial_weight, to_enum, to_measure_unit


def when_convert_to_enum(input_content, enum):
    measure_unit = to_enum(input_content, enum)
    return measure_unit


def given_input_content(content):
    input_content = content
    return input_content


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.questioner = Questioner()
        self.prepare_questions()

    def test_to_enum(self):
        input_content = given_input_content('i')
        measure_unit = when_convert_to_enum(input_content, MeasureUnit)
        self.enum_value_should_be(measure_unit, MeasureUnit.Imperial)
        input_content = given_input_content('Imperial')
        measure_unit = when_convert_to_enum(input_content, MeasureUnit)
        self.enum_value_should_be(measure_unit, MeasureUnit.Imperial)
        input_content = given_input_content('Imperia')
        with self.assertRaises(Exception):
            when_convert_to_enum(input_content, MeasureUnit)

    def enum_value_should_be(self, measure_unit, expected):
        self.assertEqual(expected, measure_unit)

    @patch('builtins.input')
    def test_questioner(self, mock_input):
        given_answers(mock_input, ['I', 'F', '7', 'P', '155'])
        answers = self.when_ask_question()
        self.should_have_input_counts(mock_input, 5)
        self.answers_should_be(answers, (MeasureUnit.Imperial, ImperialLength.Feet, 7.0, ImperialWeight.Ponds, 155.0))
        mock_input.reset_mock()
        mock_input.side_effect = ['j', 'i', 'F', '7', 'P', '155']
        answers = self.when_ask_question()
        self.should_have_input_counts(mock_input, 6)
        self.answers_should_be(answers, (MeasureUnit.Imperial, ImperialLength.Feet, 7.0, ImperialWeight.Ponds, 155.0))

    def answers_should_be(self, answers, expected):
        self.assertTupleEqual(answers, expected)

    def should_have_input_counts(self, mock_input, expected_count):
        self.assertEqual(expected_count, mock_input.call_count)

    def when_ask_question(self):
        answers = self.questioner.ask()
        return answers

    def prepare_questions(self):
        self.questioner.add_question('Select a measure unit, I)Imperial or M)Metric? ', validator=to_measure_unit,
                                     retry=True) \
            .add_question('Select the unit of the height, F)Feet or I)Inches? ', validator=to_imperial_length,
                          retry=True) \
            .add_question('Please input the height in feet: ', validator=to_float, retry=True) \
            .add_question('Select the unit of the weight, P)Ponds or S)Stones? ', validator=to_imperial_weight,
                          retry=True) \
            .add_question('Please input the weight in ponds: ', validator=to_float, retry=True)


if __name__ == '__main__':
    unittest.main()
