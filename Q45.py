import RegulationFunction as rf
import math
import random
filePath = 'Q45_inputFile.txt'

class WordFinder:
    def __init__(self):
        with open(filePath) as f:
            self.inputFile = f.read()
        print(self.inputFile)
        self.newFileName = ''

    def replaceWord(self, oldWord = 'utilize', newWord = 'use'):
        oldString = self.inputFile
        newString = oldString.replace(oldWord,newWord,1)

        replacetime = 0
        while oldString != newString:
            replacetime += 1
            oldString = newString
            newString = oldString.replace(oldWord,newWord,1)
        print(f'There are {replacetime} places replaced!')

        self.newFileName = input('The name of the output file: ')
        outputFile = self.newFileName + '.txt'
        with open(outputFile, 'w+') as f:
            f.write(newString)


mainFunction = WordFinder()
mainFunction.replaceWord()