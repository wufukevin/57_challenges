import unittest
from unittest.mock import Mock, patch


class QuotePrinter(object):
    def ask_quotes(self):
        self.quotes = input("What is the quote? ")

    def ask_who_said(self):
        self.who_said = input("Who said it? ")

    def show_quotes_said(self):
        print(self.who_said + " says, " + "\"" + self.quotes + "\"")


class MyTestCase(unittest.TestCase):
    @patch("builtins.input")
    @patch("builtins.print")
    def test_quotes(self, mock_print, mock_input):
        printer = QuotePrinter()
        mock_input.side_effect = ["These aren't the droids you're looking for.", "Obi-Wan Kenobi"]
        printer.ask_quotes()
        printer.ask_who_said()
        printer.show_quotes_said()
        mock_print.assert_called_with("Obi-Wan Kenobi says, \"These aren't the droids you're looking for.\"")


if __name__ == '__main__':
    unittest.main()
