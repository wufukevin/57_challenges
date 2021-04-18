import RegulationFunction as rf
import math
import random
inputFilePath = 'Q41_nameList.txt'
outputFilePath = 'Q41_sortedNameList.txt'

class NameSorter:
    def __init__(self):
        self.outputFilePath = outputFilePath
        with open(inputFilePath,'r') as f:
            self.nameList = [name[:-1] for name in f]
        # self.file = open(self.inputFilePath, 'r')
        #
        # for name in self.file:
        #     self.nameList.append(name[:-1])
        # self.file.close()


    def quickSort(self, list, sortCharIndex):
        if len(list) == 1 or len(list) == 0:
            return list
        pivot = list[0][sortCharIndex]
        midList = []
        leftList = []
        rightList = []

        for name in list:
            if name[sortCharIndex] < pivot:
                leftList.append(name)
            elif name[sortCharIndex] > pivot:
                rightList.append(name)
            else:
                midList.append(name)
        if len(midList) > 1:
            midList = self.quickSort(midList, sortCharIndex + 1)
        return self.quickSort(leftList, sortCharIndex) + midList + self.quickSort(rightList, sortCharIndex)


    def writeSortedNames(self):
        with open(self.outputFilePath, 'w+') as f:
            f.write(f'Total of {len(self.nameList)} names')
            f.write('\n')
            f.write('-----------------')
            f.write('\n')
            for name in self.quickSort(self.nameList,0):
                f.write(name)
                f.write('\n')

    def outputSortedNames(self):
        print(f'Total of {len(self.nameList)} names')
        print('-----------------')
        for name in self.quickSort(self.nameList,0):
            print(name)

mainFunction = NameSorter()
mainFunction.writeSortedNames()