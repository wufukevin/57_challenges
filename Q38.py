import RegulationFunction as rf
import numpy as np
import math
import string
import random


class FilteringValues:
    def __init__(self, inputNumberString):
        # self.inputNumberList = list(inputNumberString.split(' '))
        self.inputNumberList = list(map(int, inputNumberString.split()))

    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('Enter a list of numbers, separated by spaces: ')
        )

    def filterEven(self):
        # outputNumberList = []
        # for num in self.inputNumberList:
        #     if num%2 == 0:
        #         outputNumberList.append(num)
        # return outputNumberList
        return [num for num in self.inputNumberList if num % 2 == 0]

    def result(self):
        print(f'The even numbers are {self.filterEven()} .')


mainFunction = FilteringValues.fromInput()
mainFunction.result()
