import unittest
from unittest.mock import patch, call

from ch4_19.bmi import Questioner, MeasureUnit, to_enum, \
    to_measure_unit, BMIEvaluator, prepare_question


def when_convert_to_enum(input_content, enum):
    measure_unit = to_enum(input_content, enum)
    return measure_unit


def given_input_content(content):
    input_content = content
    return input_content


def given_answers(mock_input, answers):
    mock_input.side_effect = answers


def result_should_be(mock_print, result):
    mock_print.assert_has_calls(
        result)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bmi_evaluator = BMIEvaluator()
        self.measure_unit_questioner = Questioner()

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
        self.prepare_measure_unit_question()
        given_answers(mock_input, ['I'])
        answers = self.when_ask_question()
        self.should_have_input_counts(mock_input, 1)
        self.answers_should_be(answers, (MeasureUnit.Imperial,))
        mock_input.reset_mock()
        mock_input.side_effect = ['j', 'i']
        answers = self.when_ask_question()
        self.should_have_input_counts(mock_input, 2)
        self.answers_should_be(answers, (MeasureUnit.Imperial,))

    def prepare_measure_unit_question(self):
        self.measure_unit_questioner.add_question('Select a measure unit, I)Imperial or M)Metric? ',
                                                  validator=to_measure_unit, retry=True)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_bmi_in_imperial(self, mock_input, mock_print):
        self.prepare_measure_unit_question()
        given_answers(mock_input, ['i'])
        measure_unit, = self.when_ask_question()
        questioner = prepare_question(measure_unit)
        given_answers(mock_input, ['F', '7', 'P', '155'])
        answers = questioner.ask()
        self.when_evaluate_bmi(answers)
        result_should_be(mock_print, [call('Your BMI is 15.4.'), call(
            'You are underweight the ideal weight. Go to see the doctor.')])
        mock_input.reset_mock()
        mock_print.reset_mock()
        given_answers(mock_input, ['F', '6', 'P', '155'])
        answers = questioner.ask()
        self.bmi_evaluator.evaluate(*answers)
        result_should_be(mock_print,
                         [call('Your BMI is 21.0.'), call('You are within the ideal weight range.')])
        mock_input.reset_mock()
        mock_print.reset_mock()
        given_answers(mock_input, ['F', '5', 'P', '155'])
        answers = questioner.ask()
        self.bmi_evaluator.evaluate(*answers)
        result_should_be(mock_print,
                         [call('Your BMI is 30.3.'),
                          call('You are overweight the ideal weight. Go to see the doctor.')])
        mock_input.reset_mock()
        mock_print.reset_mock()
        given_answers(mock_input, ['I', '60', 'S', '11'])
        answers = questioner.ask()
        self.bmi_evaluator.evaluate(*answers)
        result_should_be(mock_print,
                         [call('Your BMI is 30.1.'),
                          call('You are overweight the ideal weight. Go to see the doctor.')])

    @patch('builtins.print')
    @patch('builtins.input')
    def test_bmi_in_metric(self, mock_input, mock_print):
        self.prepare_measure_unit_question()
        given_answers(mock_input, ['m'])
        measure_unit, = self.when_ask_question()
        questioner = prepare_question(measure_unit)
        given_answers(mock_input, ['m', '1.7', 'k', '70'])
        answers = questioner.ask()
        self.when_evaluate_bmi(answers)
        result_should_be(mock_print, [call('Your BMI is 24.2.'), call(
            'You are within the ideal weight range.')])
        mock_input.reset_mock()
        mock_print.reset_mock()
        given_answers(mock_input, ['centimeter', '170', 'g', '70000'])
        answers = questioner.ask()
        self.bmi_evaluator.evaluate(*answers)
        result_should_be(mock_print,
                         [call('Your BMI is 24.2.'), call('You are within the ideal weight range.')])

    def when_evaluate_bmi(self, answers):
        self.bmi_evaluator.evaluate(*answers)

    def answers_should_be(self, answers, expected):
        self.assertTupleEqual(answers, expected)

    def should_have_input_counts(self, mock_input, expected_count):
        self.assertEqual(expected_count, mock_input.call_count)

    def when_ask_question(self):
        answers = self.measure_unit_questioner.ask()
        return answers


if __name__ == '__main__':
    unittest.main()
