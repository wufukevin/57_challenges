import unittest
from unittest.mock import patch

from ch1_saying_hello.say_hello_robot import SayHelloRobot


def given_ask_name(mock_input, name):
    mock_input.return_value = name


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.robot = SayHelloRobot()

    @patch("builtins.input")
    def test_ask_name_to_tony(self, mock_input):
        given_ask_name(mock_input, "Tony")
        self.assertEqual("Tony", self.robot.ask_name())
        mock_input.assert_called_with("What is your name? ")

    @patch("builtins.input")
    def test_ask_name_to_stark(self, mock_input):
        given_ask_name(mock_input, "Stark")
        self.assertEqual("Stark", self.robot.ask_name())
        mock_input.assert_called_with("What is your name? ")


if __name__ == '__main__':
    unittest.main()
