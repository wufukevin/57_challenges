import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input")
    def test_sale_1_pizza_1_people(self, mock_input, mock_print):
        pizza_party = PizzaParty()
        mock_input.return_value = 'sale'
        pizza_party.ask_for_function()
        self.assertEqual('sale', pizza_party.function)
        mock_input.side_effect = ["1", "1"]
        pizza_party.ask_questions_by_function()
        pizza_party.work()
        mock_print.assert_called_with(
            '1 people with 1 pizza\nEach person gets 1 piece of pizza.\nThere are 0 leftover pieces.')


if __name__ == '__main__':
    unittest.main()
