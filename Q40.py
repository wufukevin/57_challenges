import RegulationFunction as rf
import math
import random
import numpy as np
import pandas as pd

filePath = 'Q40_employeeData.csv'

class EmployeeData:
    def __init__(self):
        columnName = ['First Name', 'Last Name', 'Position', 'Separation date']
        self.data = pd.read_csv(filePath, names=columnName, parse_dates=['Separation date'])

        self.data['Name'] = self.data['First Name']+' '+self.data['Last Name']
        self.data = self.data[['Name', 'Position', 'Separation date']]

        print(self.data)

    def nameSearch(self, searchedString):
        print(self.data.loc[self.data['Name'].str.contains(searchedString,case=False)])

    def positionSearch(self, searchedPosition):
        print(self.data.loc[self.data['Position'].str.contains(searchedPosition, case=False)])

    def sixMonthSearch(self, inputDateString):
        inputDate = pd.to_datetime(inputDateString)
        open_day = inputDate - pd.DateOffset(months=6)
        close_day = inputDate + pd.DateOffset(months=6)
        print(open_day)
        print(close_day)
        con1 = self.data['Separation date'] >= open_day
        con2 = self.data['Separation date'] < close_day
        print(self.data[con1 & con2])

mainFunction = EmployeeData()
mainFunction.nameSearch(rf.InputFunction('Enter the name to search: '))
mainFunction.positionSearch(rf.InputFunction('Enter the position to search: '))
mainFunction.sixMonthSearch(rf.InputFunction('Enter the date in yyyymmdd format: '))