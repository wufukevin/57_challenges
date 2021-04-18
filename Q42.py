import RegulationFunction as rf
import math
import random

inputFilePath = 'Q42_dataFile.txt'


class ParsingDataFile:
    def __init__(self):
        self.inputFilePath = inputFilePath
        # self.lastNameList = []
        # self.firstNameList = []
        # self.salaryList = []

        with open(self.inputFilePath, 'r') as f:
            self.dataList = [self.parseData(data[:-1]) for data in f]

    #     self.readData()
    #
    # def readData(self):
    #     self.file = open(self.inputFilePath, 'r')
    #     self.dataList = []
    #     for name in self.file:
    #         self.dataList.append(name[:-1])
    #     self.file.close()

    def parseData(self, raw_data):
        # for string in raw_data:
        data = raw_data.split(',')
        return {'lastName': data[0], 'firstName': data[1], 'salary': data[2]}
            # self.dataList.append()
            # self.lastNameList.append(data[0])
            # self.firstNameList.append(data[1])
            # self.salaryList.append(data[2])

    def outputParsedData(self):
        # self.parseData()
        # lastLength = max(len(item) for item in self.lastNameList) + 1
        lastLength = max(len(item['lastName']) for item in self.dataList) +1
        # firstLength = max(len(item) for item in self.firstNameList) + 1
        firstLength = max(len(item['firstName']) for item in self.dataList) + 1
        # salaryLength = max(len(item) for item in self.salaryList) + 1
        salaryLength = max(len(item['salary']) for item in self.dataList) + 1
        allLength = lastLength + firstLength + salaryLength
        headerColumns = ['Last', 'First', 'Salary']

        # print(f'{headerColumns[0]:<{lastLength}}{headerColumns[1]:<{firstLength}}{headerColumns[2]:<{salaryLength}}')
        format_template = '%%-%ds%%-%ds%%-%ds'
        formatter = format_template % (lastLength, firstLength, salaryLength)

        print(formatter % (headerColumns[0], headerColumns[1], headerColumns[2]))
        # print(''.ljust(allLength,'-'))
        print('-' * allLength)
        for data in self.dataList:
            print(formatter % (data['lastName'], data['firstName'], data['salary']))
        # for i in range(len(self.dataList)):
        #     print(formatter % (self.dataList[i]['lastName'], self.dataList[i]['firstName'], self.dataList[i]['salary']))


mainFunction = ParsingDataFile()
mainFunction.outputParsedData()
