import RegulationFunction as rf
import numpy as np
import math
import string
import random


class FilteringValues:
    def __init__(self, inputNumberString):
        self.inputNumberList = list(inputNumberString.split(' '))
        self.inputNumberList = list(map(int, self.inputNumberList))


    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('Enter a list of numbers, separated by spaces: ')
        )

    def filterEven(self):
        for num in self.inputNumberList:
            if num%2 == 1:
                self.inputNumberList.remove(num)

    def result(self):
        self.filterEven()
        print(f'The even numbers are {self.inputNumberList} .')


mainFunction = FilteringValues.fromInput()
mainFunction.result()
