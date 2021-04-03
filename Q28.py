import RegulationFunction as rf
import math
import re


class InputData:
    def __init__(self, inputList):
        self.inputList = inputList

    @classmethod
    def fromInput(cls):
        inputTime = int(rf.InputFunction('How many number you want to enter?: ',1,rf.isInteger))
        inputList = []
        for i in range(inputTime):
            inputNumber = int(rf.InputFunction('Enter a number: ', 1, rf.isInteger))
            inputList.append(inputNumber)
        return cls(
            inputList
        )

    def total(self):
        print(f'The total is {sum(self.inputList)}.')


InputData.fromInput().total()
