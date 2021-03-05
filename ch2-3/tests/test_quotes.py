import unittest
from unittest.mock import patch

from printing_quotes.quote_printer import QuotePrinter


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
