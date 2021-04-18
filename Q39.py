from enum import Enum

import RegulationFunction as rf
import numpy as np
import math
import string
import random
import pandas as pd
filePath = 'Q40_employeeData.csv'

class SortMethod(Enum):
    Separation = ('1', 'Separation date')
    Position = ('2', 'Position')
    Name = ('3', 'Name')

    def fromValue(self, value):
        if value == '1':
            return SortMethod.Separation
        elif value == '2':
            return SortMethod.Position
        else:
            return SortMethod.Name

def correctAnswer(ans):
    anslist = ['1','2','3']
    if ans not in anslist:
        print('Please enter a correct ans!')
        return False
    return True

class SortingRecords:
    def __init__(self):
        columnName = ['First Name', 'Last Name', 'Position', 'Separation date']
        self.data = pd.read_csv(filePath, names=columnName, parse_dates=['Separation date'])

        self.data['Name'] = self.data['First Name']+' '+self.data['Last Name']
        self.data = self.data[['Name', 'Position', 'Separation date']]


    def sort(self, sortedMethod):
        self.data = self.data.sort_values(by=[sortedMethod.value])
        # if sortedMethod == SortMethod.Separation:
        #     self.data = self.data.sort_values(by=[sortBy])
        # elif sortedMethod == SortMethod.Position:
        #     self.data = self.data.sort_values(by=['Position'])
        # elif sortedMethod == SortMethod.Name:
        #     self.data = self.data.sort_values(by=['Name'])


    def result(self):
        print('Before Sorting:')
        print(self.data)
        sortedMethod = rf.InputFunction('How to sort? 1)Separation date 2)position 3)last name',1, correctAnswer)
        self.sort(SortMethod.fromValue(sortedMethod))
        print('After Sorting')
        print(self.data)


mainFunction = SortingRecords()
mainFunction.result()
