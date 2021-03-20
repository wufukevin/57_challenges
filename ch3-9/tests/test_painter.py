import unittest
from unittest.mock import patch

from ch3_9.painter import Painter, get_painter, ask_for_painter, LShaprePainter, RoundPainter


def given_input_length_and_width(mock_input, expected_input):
    mock_input.side_effect = expected_input


def result_should_be(mock_print, expected_result):
    mock_print.assert_called_with(expected_result)


def given_input_radius(mock_input, input_radius):
    mock_input.return_value = input_radius


def given_L_shape_length_and_width(mock_input, input_L_shape_length_and_width):
    mock_input.side_effect = input_L_shape_length_and_width


def given_painter_choice(mock_input, painter):
    mock_input.return_value = painter


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.l_shape_painter_option = '3'
        self.round_painter_option = '2'
        self.painter_option = '1'

    @patch('builtins.input')
    def test_ask_length_and_width(self, mock_input):
        given_painter_choice(mock_input, self.painter_option)
        self.painter = get_painter(ask_for_painter())
        given_input_length_and_width(mock_input, ['20', '18'])
        self.painter.ask_for_input()
        self.length_and_width_should_be(20, 18)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_calculate(self, mock_input, mock_print):
        given_painter_choice(mock_input, self.painter_option)
        self.painter = get_painter(ask_for_painter())
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
        given_painter_choice(mock_input, self.round_painter_option)
        self.painter = get_painter(ask_for_painter())
        given_input_radius(mock_input, '60')
        self.painter.ask_for_input()
        self.radius_should_be(60)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_calculate_round_room(self, mock_input, mock_print):
        given_painter_choice(mock_input, self.round_painter_option)
        self.painter = get_painter(ask_for_painter())
        given_input_radius(mock_input, '10')
        self.painter.ask_for_input()
        self.area_to_paint_should_be(314)
        self.painter.calculate_gallons()
        mock_print.assert_called_with('You will need to purchase 1 gallons of paint to cover 314 square feet.')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_calculate_L_shape_room(self, mock_input, mock_print):
        given_painter_choice(mock_input, self.l_shape_painter_option)
        self.painter = get_painter(ask_for_painter())
        given_L_shape_length_and_width(mock_input, ['10', '20', '5', '10'])
        self.painter.ask_for_input()
        self.area_to_paint_should_be(250)
        self.painter.calculate_gallons()
        mock_print.assert_called_with('You will need to purchase 1 gallons of paint to cover 250 square feet.')

    @patch('builtins.input')
    def test_ask_painter(self, mock_input):
        given_painter_choice(mock_input, self.painter_option)
        self.chosen_painter = ask_for_painter()
        painter = get_painter(self.chosen_painter)
        self.painter_type_should_be(painter, Painter)
        given_painter_choice(mock_input, self.round_painter_option)
        self.chosen_painter = ask_for_painter()
        painter = get_painter(self.chosen_painter)
        self.painter_type_should_be(painter, RoundPainter)
        given_painter_choice(mock_input, self.l_shape_painter_option)
        self.chosen_painter = ask_for_painter()
        painter = get_painter(self.chosen_painter)
        self.painter_type_should_be(painter, LShaprePainter)

    def painter_type_should_be(self, painter, expected_type):
        self.assertIsInstance(painter, expected_type)

    def radius_should_be(self, expected_radius):
        self.assertEqual(expected_radius, self.painter.radius)

    def area_to_paint_should_be(self, expected_area):
        self.assertEqual(expected_area, self.painter.area_to_paint())

    def length_and_width_should_be(self, length, width):
        self.assertEqual(length, self.painter.length)
        self.assertEqual(width, self.painter.width)


if __name__ == '__main__':
    unittest.main()
