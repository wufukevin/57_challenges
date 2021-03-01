import unittest


class SayHelloRobot(object):
    def ask_name(self):
        return "Tony"


class MyTestCase(unittest.TestCase):

    def test_ask_name_to_tony(self):
        robot = SayHelloRobot()
        self.assertEqual("Tony", robot.ask_name())

    def test_ask_name_to_stark(self):
        robot = SayHelloRobot()
        self.assertEqual("Stark", robot.ask_name())


if __name__ == '__main__':
    unittest.main()
