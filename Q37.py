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
        self.asciiLettersList = []
        self.punctuationList = []
        self.digitsList = []


    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('What\'s the minimum length? ', 1, rf.isInteger),
            rf.InputFunction('How many special characters? ', 1, rf.isInteger),
            rf.InputFunction('How many numbers? ', 1, rf.isInteger)
        )

    def asciiLettersUsed(self, number):
        for i in range(number):
            self.asciiLettersList.append(random.choice(string.ascii_letters))
    def punctuationUsed(self, number):
        for i in range(number):
            self.punctuationList.append(random.choice(string.punctuation))
    def digitsUsed(self, number):
        for i in range(number):
            self.digitsList.append(random.choice(string.digits))

    def cleanList(self):
        self.asciiLettersList = []
        self.punctuationList = []
        self.digitsList = []

    def createPassword(self):
        passwordLength = self.minlength + random.randint(0, 3)
        asciiLettersNumber = passwordLength - self.punctuationNumber - self.digitsNumber
        self.asciiLettersUsed(asciiLettersNumber)
        self.punctuationUsed(self.punctuationNumber)
        self.digitsUsed(self.digitsNumber)
        materialList = self.asciiLettersList+self.punctuationList+self.digitsList
        password = ''
        # print(materialList)
        for word in random.sample(materialList,len(materialList)):
            password = password + word
        print(password)
        self.cleanList()

    def printPassword(self):
        print(f'Your password is')
        self.createPassword()
        self.createPassword()
        self.createPassword()


mainFunction = PasswordGenerator.fromInput()
mainFunction.printPassword()
