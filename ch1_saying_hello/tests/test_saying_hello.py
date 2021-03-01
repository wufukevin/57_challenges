import unittest
from unittest.mock import patch


class SayHelloRobot(object):
    def ask_name(self):
        return input()


class MyTestCase(unittest.TestCase):

    @patch("builtins.input")
    def test_ask_name_to_tony(self, mock_input):
        robot = SayHelloRobot()
        mock_input.return_value = "Tony"
        self.assertEqual("Tony", robot.ask_name())

    @patch("builtins.input")
    def test_ask_name_to_stark(self, mock_input):
        robot = SayHelloRobot()
        mock_input.return_value = "Stark"
        self.assertEqual("Stark", robot.ask_name())


if __name__ == '__main__':
    unittest.main()
