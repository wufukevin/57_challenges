import RegulationFunction as rf
import math
import random
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def levelCheck(level):
    levelList = ['1','2','3']
    ansCorrect = True if level in levelList else False
    if not ansCorrect:
        print('Please enter correct level.')
    return ansCorrect

def wantAgain(ans):
    if ans != 'y' and ans != 'n':
        print("Please enter correct!!")
        return False
    elif ans == 'n':
        return True
    else:
        return True

class GuessNumber:
    def __init__(self, gameLevel):
        self.gameLevel = int(gameLevel)
        self.ansRange = math.pow(10,self.gameLevel)
        self.ans = random.randint(1,self.ansRange)
        print(f'ans = {self.ans}')
        self.yourGuess = 0
        self.guessTime = 0
        self.guessList = []
        self.again = False


    @classmethod
    def from_input(cls):
        print('Let\'s play Guess the Number.')
        return cls(
            rf.InputFunction('Pick a difficulty level (1, 2, or 3): ',1, levelCheck),
        )

    def Start(self):
        if self.guessTime == 0:
            sentence = 'I have my number. What\'s your guess? '
        elif self.yourGuess > self.ans:
            sentence = 'Too high. Guess again: '
        elif self.yourGuess < self.ans:
            sentence = 'Too low. Guess again: '
        else:
            print(f'You got it in {self.guessTime} guesses!')
            again = rf.InputFunction('Play again? ',1,wantAgain)
            if again == 'y':
                self.again = True
            return self.again
        self.yourGuess = int(rf.InputFunction(sentence))
        self.guessTime += 1
        self.Start()

mainFunction = GuessNumber.from_input()
while mainFunction.Start():
    print('new game')
    mainFunction = GuessNumber.from_input()
print('Goodbye!!')