import unittest
from unittest.mock import patch

from ch3_8.pizza_cut import PizzaParty


def given_function(mock_input, function):
    mock_input.return_value = function


def given_input_by_function(mock_input, input_for_function):
    mock_input.side_effect = input_for_function


def result_should_be(mock_print, expected):
    mock_print.assert_called_with(
        expected)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pizza_party = PizzaParty()

    @patch("builtins.print")
    @patch("builtins.input")
    def test_cut_1_pizza_1_people(self, mock_input, mock_print):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        self.function_should_be('cut')
        given_input_by_function(mock_input, ["1", "1"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '1 people with 1 pizza\nEach person gets 8 pieces of pizza.\nThere are 0 leftover pieces.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_cut_2_pizza_8_people(self, mock_input, mock_print):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        self.function_should_be('cut')
        given_input_by_function(mock_input, ["8", "2"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '8 people with 2 pizzas\nEach person gets 2 pieces of pizza.\nThere are 0 leftover pieces.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_cut_2_pizza_7_people(self, mock_input, mock_print):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        self.function_should_be('cut')
        given_input_by_function(mock_input, ["7", "2"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '7 people with 2 pizzas\nEach person gets 2 pieces of pizza.\nThere are 2 leftover pieces.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_cut_1_pizza_2_people(self, mock_input, mock_print):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        self.function_should_be('cut')
        given_input_by_function(mock_input, ["2", "1"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '2 people with 1 pizza\nEach person gets 4 pieces of pizza.\nThere are 0 leftover pieces.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_count_1_people_1_piece(self, mock_input, mock_print):
        given_function(mock_input, 'count')
        self.when_ask_function()
        self.function_should_be('count')
        given_input_by_function(mock_input, ["1", "1"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '1 people with 1 piece of pizza desired for each.\nThere should be 1 pizza.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_count_1_people_8_piece(self, mock_input, mock_print):
        given_function(mock_input, 'count')
        self.when_ask_function()
        self.function_should_be('count')
        given_input_by_function(mock_input, ["1", "8"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '1 people with 8 pieces of pizza desired for each.\nThere should be 1 pizza.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_count_2_people_3_piece(self, mock_input, mock_print):
        given_function(mock_input, 'count')
        self.when_ask_function()
        self.function_should_be('count')
        given_input_by_function(mock_input, ["2", "3"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '2 people with 3 pieces of pizza desired for each.\nThere should be 1 pizza.')

    @patch("builtins.print")
    @patch("builtins.input")
    def test_count_3_people_3_piece(self, mock_input, mock_print):
        given_function(mock_input, 'count')
        self.when_ask_function()
        self.function_should_be('count')
        given_input_by_function(mock_input, ["3", "3"])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '3 people with 3 pieces of pizza desired for each.\nThere should be 2 pizzas.')

    @patch("builtins.input")
    def test_ask_unsupported_function(self, mock_input):
        given_function(mock_input, 'cook')
        self.then_raise_exception(self.when_ask_function)

    @patch("builtins.input")
    def test_ask_non_numeric_people_or_pizza(self, mock_input):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        given_input_by_function(mock_input, ['a', '1'])
        self.then_raise_exception(self.when_ask_question_by_function)
        given_input_by_function(mock_input, ['1', 'a'])
        self.then_raise_exception(self.when_ask_question_by_function)

    @patch("builtins.input")
    def test_cut_pizza_1_people_0(self, mock_input):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        given_input_by_function(mock_input, ['0', '1'])
        self.then_raise_exception(self.when_ask_question_by_function)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_cut_pizza_0_people_1(self, mock_input, mock_print):
        given_function(mock_input, 'cut')
        self.when_ask_function()
        given_input_by_function(mock_input, ['1', '0'])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '1 people with 0 pizza\nEach person gets 0 piece of pizza.\nThere are 0 leftover pieces.')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_count_1_people_0_pieces(self, mock_input, mock_print):
        given_function(mock_input, 'count')
        self.when_ask_function()
        given_input_by_function(mock_input, ['1', '0'])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '1 people with 0 piece of pizza desired for each.\nThere should be 0 pizza.')

    @patch('builtins.print')
    @patch('builtins.input')
    def test_count_0_people_1_pieces(self, mock_input, mock_print):
        given_function(mock_input, 'count')
        self.when_ask_function()
        given_input_by_function(mock_input, ['0', '1'])
        self.when_ask_question_by_function()
        self.when_work()
        result_should_be(mock_print,
                         '0 people with 1 piece of pizza desired for each.\nThere should be 0 pizza.')

    def then_raise_exception(self, action):
        with self.assertRaises(Exception):
            action()

    def when_work(self):
        self.pizza_party.work()

    def when_ask_question_by_function(self):
        self.pizza_party.ask_questions_by_function()

    def function_should_be(self, expected):
        self.assertEqual(expected, self.pizza_party.function)

    def when_ask_function(self):
        self.pizza_party.ask_for_function()


if __name__ == '__main__':
    unittest.main()
