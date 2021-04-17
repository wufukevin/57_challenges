import RegulationFunction as rf
import math
import random
inputFilePath = 'Q42_dataFile.txt'

class ParsingDataFile:
    def __init__(self):
        self.inputFilePath = inputFilePath
        self.file = None
        self.dataList = []
        self.lastNameList = []
        self.firstNameList = []
        self.salaryList = []
        self.readData()

    def readData(self):
        self.file = open(self.inputFilePath, 'r')
        self.dataList = []
        for name in self.file:
            self.dataList.append(name[:-1])
        self.file.close()

    def parseData(self):
        for string in self.dataList:
            data = string.split(',')
            self.lastNameList.append(data[0])
            self.firstNameList.append(data[1])
            self.salaryList.append(data[2])

    def outputParsedData(self):
        self.parseData()
        lastLength = max(len(item) for item in self.lastNameList) + 1
        firstLength = max(len(item) for item in self.firstNameList) + 1
        salaryLength = max(len(item) for item in self.salaryList) + 1
        allLength = lastLength+firstLength+salaryLength
        columnList = ['Last', 'First', 'Salary']

        # print(f'{columnList[0]:<{lastLength}}{columnList[1]:<{firstLength}}{columnList[2]:<{salaryLength}}')
        format_template = '%%-%ds%%-%ds%%-%ds'
        formatter = format_template % (lastLength, firstLength, salaryLength)

        print(formatter % (columnList[0], columnList[1], columnList[2]))
        print(''.ljust(allLength,'-'))
        for i in range(len(self.dataList)):
            print(formatter % (self.lastNameList[i], self.firstNameList[i], self.salaryList[i]))

mainFunction = ParsingDataFile()
mainFunction.outputParsedData()