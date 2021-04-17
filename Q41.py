import RegulationFunction as rf
import math
import random
inputFilePath = 'Q41_nameList.txt'
outputFilePath = 'Q41_sortedNameList.txt'

class NameSorter:
    def __init__(self):
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath
        self.file = open(self.inputFilePath, 'r')
        self.nameList = []
        for name in self.file:
            self.nameList.append(name[:-1])
        self.file.close()


    def quickSort(self, list, sortedLevel):
        if len(list) == 1 or len(list) == 0:
            return list
        pivot = list[0][sortedLevel]
        mid_list = []
        left_list = []
        right_list = []

        for name in list:
            if name[sortedLevel] < pivot:
                left_list.append(name)
            elif name[sortedLevel] > pivot:
                right_list.append(name)
            else:
                mid_list.append(name)
        if len(mid_list) > 2:
            mid_list = self.quickSort(mid_list, sortedLevel+1)
        return self.quickSort(left_list, sortedLevel)+mid_list+self.quickSort(right_list, sortedLevel)


    def writeSortedNames(self):
        file = open(self.outputFilePath, 'w')
        file.write(f'Total of {len(self.nameList)} names')
        file.write('\n')
        file.write('-----------------')
        file.write('\n')
        for name in self.quickSort(self.nameList,0):
            file.write(name)
            file.write('\n')
        self.file.close()

    def outputSortedNames(self):
        print(f'Total of {len(self.nameList)} names')
        print('-----------------')
        for name in self.quickSort(self.nameList,0):
            print(name)

mainFunction = NameSorter()
mainFunction.writeSortedNames()