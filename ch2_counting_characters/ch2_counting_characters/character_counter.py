class CharacterCounter(object):
    def __init__(self):
        self.word = None

    def ask_input(self):
        self.word = input("What is the input string?")

    def count_result(self):
        return self.word + " has " + str(len(self.word)) + " characters."
