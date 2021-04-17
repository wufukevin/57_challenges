import RegulationFunction as rf
import numpy as np
import math
import random


class ComputingStatistic:
    def __init__(self):
        self.inputList = []
        self.keepInput = True
        self.minimum = np.iinfo(np.int32).max
        self.maximum = np.iinfo(np.int32).min

    def inputNumber(self):
        inputedNumber = input('Enter a number: ')
        if inputedNumber == 'done':
            self.keepInput = False
        else:
            inputedNumber = int(inputedNumber)
            if inputedNumber > self.maximum:
                self.maximum = inputedNumber
            if inputedNumber < self.minimum:
                self.minimum = inputedNumber
            self.inputList.append(inputedNumber)

    def computeAverage(self):
        return sum(self.inputList)/len(self.inputList)

    def computeStandardDeviation(self):
        average = self.computeAverage()
        calculatedlist = [math.pow(num-average,2) for num in self.inputList]
        meanOfTheList = sum(calculatedlist)/len(self.inputList)
        return(math.sqrt(meanOfTheList))

    def printAnswer(self):
        print(f'Numbers: {self.inputList}')
        print(f'the average is {self.computeAverage()} .')
        print(f'the minimum is {self.minimum} .')
        print(f'the maximum is {self.maximum} .')
        print(f'the standard deviation is {self.computeStandardDeviation()} .')


mainFunction = ComputingStatistic()
while mainFunction.keepInput:
    mainFunction.inputNumber()
mainFunction.printAnswer()
