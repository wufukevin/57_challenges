import unittest


class SayHelloRobot(object):
    def ask_name(self):
        return "Tony Stark"


class MyTestCase(unittest.TestCase):

    def test_ask_name(self):
        robot = SayHelloRobot()
        name = robot.ask_name()
        self.assertEqual("Tony Stark", name)


if __name__ == '__main__':
    unittest.main()
