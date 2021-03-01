import unittest


class MyTestCase(unittest.TestCase):
    def test_quotes(self):
        printer = QuotePrinter()
        printer.ask_quotes()
        printer.ask_who_said()
        printer.show_quotes_said()


if __name__ == '__main__':
    unittest.main()
