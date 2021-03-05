class CharacterCounter(object):
    def __init__(self):
        self.word = None

    def ask_input(self):
        self.word = input("What is the input string?")

    def count_result(self):
        if len(self.word) == 0:
            return 'No input detected!'
        return self.word + " has " + str(len(self.word)) + " characters."


if __name__ == '__main__':
    counter = CharacterCounter()
    counter.ask_input()
    print(counter.count_result())
