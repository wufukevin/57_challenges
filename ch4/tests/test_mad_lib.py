import unittest
from unittest.mock import patch


class MadLib(object):
    def ask_verb(self):
        self.verb = input("Enter a verb: ")

    def ask_noun(self):
        self.noun = input("Enter a noun: ")

    def ask_adv(self):
        self.adv = input("Enter an adv: ")

    def ask_adj(self):
        self.adj = input("Enter an adj: ")

    def tell_story(self):
        print(f"Do you {self.verb} your {self.adj} {self.noun} {self.adv}? That's hilarious!")


class MyTestCase(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input")
    def test_mad_lib(self, mock_input, mock_print):
        mad_lib = MadLib()
        mock_input.side_effect = ["dog", "walk", "blue", "quickly"]
        mad_lib.ask_noun()
        mad_lib.ask_verb()
        mad_lib.ask_adj()
        mad_lib.ask_adv()
        mad_lib.tell_story()
        mock_print.assert_called_with("Do you walk your blue dog quickly? That's hilarious!")


if __name__ == '__main__':
    unittest.main()
