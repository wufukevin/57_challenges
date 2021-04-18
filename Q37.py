import RegulationFunction as rf
import numpy as np
import math
import string
import random


class PasswordGenerator:
    def __init__(self, minlength, punctuationNumber, digitsNumber):
        self.minlength = int(minlength)
        self.punctuationNumber = int(punctuationNumber)
        self.digitsNumber = int(digitsNumber)

    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('What\'s the minimum length? ', 1, rf.isInteger),
            rf.InputFunction('How many special characters? ', 1, rf.isInteger),
            rf.InputFunction('How many numbers? ', 1, rf.isInteger)
        )

    def asciiLettersUsed(self, number):
        list = []
        for i in range(number):
            list.append(random.choice(string.ascii_letters))
        return list

    def punctuationUsed(self, number):
        list = []
        for i in range(number):
            list.append(random.choice(string.punctuation))
        return list

    def digitsUsed(self, number):
        list = []
        for i in range(number):
            list.append(random.choice(string.digits))
        return list

    def createPassword(self):
        passwordLength = self.minlength + random.randint(0, 3)
        asciiLettersNumber = passwordLength - self.punctuationNumber - self.digitsNumber
        materialList = self.asciiLettersUsed(asciiLettersNumber) + self.punctuationUsed(
            self.punctuationNumber) + self.digitsUsed(self.digitsNumber)
        # password = ''
        # for word in random.sample(materialList, len(materialList)):
        #     password = password + word
        print(''.join(word for word in random.sample(materialList, len(materialList))))
        # print(password)

    def printPassword(self):
        print(f'Your password is')
        self.createPassword()
        self.createPassword()
        self.createPassword()


mainFunction = PasswordGenerator.fromInput()
mainFunction.printPassword()
