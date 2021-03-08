import unittest
from unittest.mock import patch

PIECES_PER_PIZZA = 8


class PizzaParty(object):
    def ask_for_function(self):
        self.function = input("Select Pizza Party Function: Cut Or Count")
        if self.function.lower() != 'cut' and self.function.lower() != 'count':
            raise Exception

    def ask_questions_by_function(self):
        if self.function.lower() == 'cut':
            self.ask_how_many_people()
            self.ask_how_many_pizza()

    def ask_how_many_people(self):
        self.people = input("How many people? ")
        if not self.people.isdigit():
            raise Exception()

    def work(self):
        if self.function.lower() == 'cut':
            print(
                f"{self.people} people with {self.pizza} pizza{self.is_plural(int(self.pizza))}\nEach person gets {self.cut_pieces()} piece{self.is_plural(self.cut_pieces())} of pizza.\nThere are {self.leftover_pieces()} leftover pieces.")

    def ask_how_many_pizza(self):
        self.pizza = input("How many pizzas do you have? ")
        if not self.pizza.isdigit():
            raise Exception()

    def is_plural(self, number):
        return 's' if number > 1 else ''

    def cut_pieces(self):
        return int(int(self.pizza) * PIECES_PER_PIZZA / int(self.people))

    def leftover_pieces(self):
        return int(int(self.pizza) * PIECES_PER_PIZZA % int(self.people))


class MyTestCase(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input")
    def test_cut_1_pizza_1_people(self, mock_input, mock_print):
        pizza_party = PizzaParty()
        mock_input.return_value = 'cut'
        pizza_party.ask_for_function()
        self.assertEqual('cut', pizza_party.function)
        mock_input.side_effect = ["1", "1"]
        pizza_party.ask_questions_by_function()
        pizza_party.work()
        mock_print.assert_called_with(
            '1 people with 1 pizza\nEach person gets 8 pieces of pizza.\nThere are 0 leftover pieces.')


if __name__ == '__main__':
    unittest.main()
