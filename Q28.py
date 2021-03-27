import RegulationFunction as rf
import math
import re


class InputData:
    def __init__(self):
        self.inputTimes = int(rf.InputFunction('How many number you want to enter?: ',1,rf.isInteger))
        self.inputList = []
        for i in range(self.inputTimes):
            inputNumber = int(rf.InputFunction('Enter a number: ',1,rf.isInteger))
            self.inputList.append(inputNumber)

    def total(self):
        total = 0
        for number in self.inputList:
            total += number
        return total


mainFunction = InputData()
total = mainFunction.total()
print(f'The total is {total}.')