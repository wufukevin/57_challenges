import RegulationFunction as rf
import math
import random
import operator
filePath = 'Q46_words.txt'


class WordFrequencyFinder:
    def __init__(self):
        with open(filePath) as f:
            inputFile = f.read()
        self.inputWord = inputFile.split()
        self.wordMap = {}
        self.wordFinder()

    def wordFinder(self):
        for word in self.inputWord:
            if word in self.wordMap.keys():
                self.wordMap[word] += 1
            else:
                self.wordMap[word] = 1

    def show(self):
        wordMaxLength = max(len(word) for word in self.wordMap.keys()) + 2
        formatTemplate = '%%-%ds'
        formatter = formatTemplate % (wordMaxLength)

        for element in sorted(self.wordMap.items(), key=lambda x:x[1], reverse=True):
            print(formatter % (element[0]+':') + '*'*element[1])

mainFunction = WordFrequencyFinder()
mainFunction.show()