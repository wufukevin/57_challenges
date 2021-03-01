class SayHelloRobot(object):
    def ask_name(self):
        return input('What is your name? ')

    def generate_hello_sentence(self, name):
        return "Hello, " + name + ", nice to meet you!"
