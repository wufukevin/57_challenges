import unittest
from math import ceil, pi
from unittest.mock import patch

PAINTABLE_AREA_IN_FEET_PER_GALLON = 350


class Painter(object):
    def __init__(self):
        self.width = None
        self.length = None
        self.radius = None

    def ask_for_input(self):
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


def given_input_radius(mock_input, input_radius):
    mock_input.return_value = input_radius


class RoundPainter(Painter):
    def ask_for_input(self):
        self.radius = int(input('Please input the radius of the round room: '))

    def area_to_paint(self):
        self.area = int(pow(self.radius, 2) * pi)
        return self.area


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.round_painter = RoundPainter()
        self.painter = Painter()

    @patch('builtins.input')
    def test_ask_length_and_width(self, mock_input):
        given_input_length_and_width(mock_input, ['20', '18'])
        self.painter.ask_for_input()
        self.length_and_width_should_be(20, 18)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_calculate(self, mock_input, mock_print):
        given_input_length_and_width(mock_input, ['20', '18'])
        self.painter.ask_for_input()
        self.area_to_paint_should_be(360)
        self.painter.calculate_gallons()
        result_should_be(mock_print, 'You will need to purchase 2 gallons of paint to cover 360 square feet.')

    @patch('builtins.input')
    def test_given_not_numeric_input(self, mock_input):
        given_input_length_and_width(mock_input, ['a', '18'])
        with self.assertRaises(Exception):
            self.painter.ask_for_input()
        given_input_length_and_width(mock_input, ['20', 'a'])
        with self.assertRaises(Exception):
            self.painter.ask_for_input()

    @patch('builtins.input')
    def test_ask_input_round_room(self, mock_input):
        given_input_radius(mock_input, '60')
        self.painter = RoundPainter()
        self.round_painter.ask_for_input()
        self.radius_should_be(60)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_calculate_round_room(self, mock_input, mock_print):
        given_input_radius(mock_input, '10')
        self.painter = RoundPainter()
        self.painter.ask_for_input()
        self.area_to_paint_should_be(314)
        self.painter.calculate_gallons()
        mock_print.assert_called_with('You will need to purchase 1 gallons of paint to cover 314 square feet.')

    def radius_should_be(self, expected_radius):
        self.assertEqual(expected_radius, self.round_painter.radius)

    def area_to_paint_should_be(self, expected_area):
        self.assertEqual(expected_area, self.painter.area_to_paint())

    def length_and_width_should_be(self, length, width):
        self.assertEqual(length, self.painter.length)
        self.assertEqual(width, self.painter.width)


if __name__ == '__main__':
    unittest.main()
