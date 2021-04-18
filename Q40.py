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
        startDate = inputDate - pd.DateOffset(months=6)
        finishDate = inputDate + pd.DateOffset(months=6)
        # print(startDate)
        # print(finishDate)
        searchFrom = self.data['Separation date'] >= startDate
        searchTo = self.data['Separation date'] < finishDate
        print(self.data[searchFrom & searchTo])

mainFunction = EmployeeData()
mainFunction.nameSearch(rf.InputFunction('Enter the name to search: '))
mainFunction.positionSearch(rf.InputFunction('Enter the position to search: '))
mainFunction.sixMonthSearch(rf.InputFunction('Enter the date in yyyymmdd format: '))