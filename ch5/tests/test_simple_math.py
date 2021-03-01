import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch("builtins.input")
    def test_ask_input_two_numbers(self):
        simple_math = SimpleMath()
        simple_math.ask_two_numbers()
        self.assertEqual("1", simple_math.first_input)
        self.assertEqual("2", simple_math.second_input)


if __name__ == '__main__':
    unittest.main()
