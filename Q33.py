import RegulationFunction as rf
import math
import random

class Magic8Ball:
    def __init__(self):
        input('What\'s your question? ')
        self.randAns = random.randint(1, 4)
        self.ansTable = {
            1: 'Yes',
            2: 'No',
            3: 'Maybe',
            4: 'Ask again later.'
        }
    #
    # @classmethod
    # def from_input(cls):
    #     return cls(
    #         rf.InputFunction('What\'s your question? ')
    #     )
    def start(self):
        print(self.ansTable[self.randAns])

mainFunction = Magic8Ball()
mainFunction.start()