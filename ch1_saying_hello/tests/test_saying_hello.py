import unittest
from unittest.mock import patch

from ch1_saying_hello.say_hello_robot import SayHelloRobot


def given_ask_name(mock_input, name):
    mock_input.return_value = name


def question_should_be(mock_input, question_sentence):
    mock_input.assert_called_with(question_sentence)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.robot = SayHelloRobot()

    @patch("builtins.input")
    def test_ask_name_to_tony(self, mock_input):
        given_ask_name(mock_input, "Tony")
        self.name_shoule_be("Tony")
        question_should_be(mock_input, "What is your name? ")

    def name_shoule_be(self, name_of_target):
        self.assertEqual(name_of_target, self.robot.ask_name())

    @patch("builtins.input")
    def test_ask_name_to_stark(self, mock_input):
        given_ask_name(mock_input, "Stark")
        self.name_shoule_be("Stark")
        question_should_be(mock_input, "What is your name? ")

    @patch("builtins.input")
    def test_say_hello_to_stark(self, mock_input):
        given_ask_name(mock_input, "Stark")
        self.name_shoule_be("Stark")
        question_should_be(mock_input, "What is your name? ")
        sentence = self.robot.generate_hello_sentence("Stark")
        self.assertEqual("Hello, Stark, nice to meet you!", sentence)


if __name__ == '__main__':
    unittest.main()
