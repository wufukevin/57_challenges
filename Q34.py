import RegulationFunction as rf
import math
import random
filePath = 'Q34_employeeList.txt'

class EmployeeList:
    def __init__(self):
        self.file = None
        self.filePath = filePath
        self.nameList = ["John Smith", "Jackie Jackson", 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']
        self.writeFile()
        self.closeFile()

    def readFile(self):
        self.nameList = []
        self.file = open(self.filePath, 'r')
        for name in self.file:
            self.nameList.append(name[:-1])

    def writeFile(self):
        self.file = open(self.filePath, 'w')
        for index in range(len(self.nameList)):
            self.nameList[index] += '\n'
        self.file.writelines(self.nameList)

    def closeFile(self):
        self.file.close()

    def showNameList(self):
        self.readFile()
        self.closeFile()
        print(f'There are {len(self.nameList)} employees:')
        for name in self.nameList:
            print(name)

    def removeEmployee(self, name):
        self.readFile()
        self.closeFile()

        try:
            self.nameList.remove(name)
        except ValueError:
            print('This name doesn\'t exist!')
        self.writeFile()
        self.closeFile()

mainFunction = EmployeeList()
mainFunction.showNameList()
print()
mainFunction.removeEmployee(rf.InputFunction('Enter an employee name to remove: '))
print()
mainFunction.showNameList()
