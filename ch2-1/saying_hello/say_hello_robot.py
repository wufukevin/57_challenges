class SayHelloRobot(object):
    def ask_name(self):
        return input('What is your name? ')

    def generate_hello_sentence(self, name):
        return "Hello, " + name + ", nice to meet you!"

    def say_hello_to(self, name):
        print(self.generate_hello_sentence(name))


if __name__ == '__main__':
    robot = SayHelloRobot()
    name = robot.ask_name()
    robot.say_hello_to(name)
