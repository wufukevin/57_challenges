import unittest
from math import ceil
from unittest.mock import patch

PAINTABLE_AREA_IN_FEET_PER_GALLON = 350


class Painter(object):
    def __init__(self):
        self.width = None
        self.length = None

    def ask_for_length_and_width(self):
        self.length = int(input('Please input length: '))
        self.width = int(input('Please input width: '))

    def area_to_paint(self):
        self.area = self.width * self.length
        return self.area

    def calculate_gallons(self):
        number_of_gallons = ceil(self.area / PAINTABLE_AREA_IN_FEET_PER_GALLON)
        print(
            f'You will need to purchase {number_of_gallons} gallons of paint to cover {self.area} square feet.')


def given_input_length_and_width(mock_input, expected_input):
    mock_input.side_effect = expected_input


def result_should_be(mock_print, expected_result):
    mock_print.assert_called_with(expected_result)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.painter = Painter()

    @patch('builtins.input')
    def test_ask_length_and_width(self, mock_input):
        given_input_length_and_width(mock_input, ['20', '18'])
        self.painter.ask_for_length_and_width()
        self.length_and_width_should_be(20, 18)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_calculate(self, mock_input, mock_print):
        given_input_length_and_width(mock_input, ['20', '18'])
        self.painter.ask_for_length_and_width()
        self.area_to_paint_should_be(360)
        self.painter.calculate_gallons()
        result_should_be(mock_print, 'You will need to purchase 2 gallons of paint to cover 360 square feet.')

    @patch('builtins.input')
    def test_given_not_numeric_input(self, mock_input):
        given_input_length_and_width(mock_input, ['a', '18'])
        with self.assertRaises(Exception):
            self.painter.ask_for_length_and_width()
        given_input_length_and_width(mock_input, ['20', 'a'])
        with self.assertRaises(Exception):
            self.painter.ask_for_length_and_width()

    @patch('builtins.input')
    def test_ask_input_round_room(self, mock_input):
        mock_input.return_value = '60'
        self.painter.ask_for_input_radius()
        self.assertEqual(60, self.painter.radius)

    def area_to_paint_should_be(self, expected_area):
        self.assertEqual(expected_area, self.painter.area_to_paint())

    def length_and_width_should_be(self, length, width):
        self.assertEqual(length, self.painter.length)
        self.assertEqual(width, self.painter.width)


if __name__ == '__main__':
    unittest.main()
