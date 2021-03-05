import unittest
from unittest.mock import patch

from saying_hello.say_hello_robot import SayHelloRobot


def given_ask_name(mock_input, name):
    mock_input.return_value = name


def question_should_be(mock_input, question_sentence):
    mock_input.assert_called_with(question_sentence)


def should_say_hello_sentence(hello_sentence, mock_print):
    mock_print.assert_called_with(hello_sentence)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.robot = SayHelloRobot()

    @patch("builtins.input")
    def test_ask_name_to_tony(self, mock_input):
        given_ask_name(mock_input, "Tony")
        self.name_should_be("Tony")
        question_should_be(mock_input, "What is your name? ")

    def name_should_be(self, name_of_target):
        self.assertEqual(name_of_target, self.robot.ask_name())

    @patch("builtins.input")
    def test_ask_name_to_stark(self, mock_input):
        given_ask_name(mock_input, "Stark")
        self.name_should_be("Stark")
        question_should_be(mock_input, "What is your name? ")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_say_hello_to_stark(self, mock_input, mock_print):
        given_ask_name(mock_input, "Stark")
        self.name_should_be("Stark")
        question_should_be(mock_input, "What is your name? ")
        hello_sentence = self.robot.generate_hello_sentence("Stark")
        self.hello_sentence_should_be(hello_sentence, "Hello, Stark, nice to meet you!")
        self.robot.say_hello_to("Stark")
        should_say_hello_sentence(hello_sentence, mock_print)

    @patch("builtins.print")
    @patch("builtins.input")
    def test_say_hello_to_tony(self, mock_input, mock_print):
        given_ask_name(mock_input, "Tony")
        self.name_should_be("Tony")
        question_should_be(mock_input, "What is your name? ")
        hello_sentence = self.robot.generate_hello_sentence("Tony")
        self.hello_sentence_should_be(hello_sentence, "Hello, Tony, nice to meet you!")
        self.robot.say_hello_to("Tony")
        should_say_hello_sentence(hello_sentence, mock_print)

    def hello_sentence_should_be(self, sentence, expected):
        self.assertEqual(expected, sentence)


if __name__ == '__main__':
    unittest.main()
