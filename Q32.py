import RegulationFunction as rf
import math
import random
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def levelCheckValidator(level):
    levelList = ['1','2','3']
    ansCorrect = True if level in levelList else False
    if not ansCorrect:
        print('Please enter correct level.')
    return ansCorrect

def wantAgainValidator(ans):
    if ans != 'y' and ans != 'n':
        print("Please enter correct!!")
        return False
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
        self.sentence = 'I have my number. What\'s your guess? '
        self.commentLevel = {
            1: 'perfect',
            2: 'good',
            3: 'good',
            4: 'good',
            5: 'bad',
            6: 'bad'
        }
        self.conclusion = {
            'perfect' : 'You’re a mind reader!',
            'good': 'Most impressive.',
            'bad': 'You can do better than that.',
            'terrible': 'Better luck next time.',
        }


    @classmethod
    def fromInput(cls):
        print('Let\'s play Guess the Number.')
        return cls(
            rf.InputFunction('Pick a difficulty level (1, 2, or 3): ', 1, levelCheckValidator),
        )

    def Start(self):
        self.yourGuess = int(rf.InputFunction(self.sentence))
        if self.yourGuess not in self.guessList: # use set DS!!
            self.guessTime += 1
            self.guessList.append(self.yourGuess)
            if self.yourGuess > self.ans:
                self.sentence = 'Too high. Guess again: '
            elif self.yourGuess < self.ans:
                self.sentence = 'Too low. Guess again: '
            else:
                print(f'You got it in {self.guessTime} guesses!')
                comment = self.commentLevel.get(self.guessTime, 'terrible')
                print(self.conclusion[comment])
                again = rf.InputFunction('Play again? ', 1, wantAgainValidator)
                if again == 'y':
                    self.again = True
                return self.again
        else:
            self.sentence = 'You have guessed this number, try another one!'
        return self.Start() #maybe overstack!!
        # if self.yourGuess not in self.guessList:
        #     if self.guessTime == 0:
        #         sentence = 'I have my number. What\'s your guess? '
        #     elif self.yourGuess > self.ans:
        #         sentence = 'Too high. Guess again: '
        #     elif self.yourGuess < self.ans:
        #         sentence = 'Too low. Guess again: '
        #     else:
        #         print(f'You got it in {self.guessTime} guesses!')
        #         again = rf.InputFunction('Play again? ',1,wantAgain)
        #         if again == 'y':
        #             self.again = True
        #         return self.again
        #     self.yourGuess = int(rf.InputFunction(sentence))
        #     self.guessTime += 1
        #     self.guessList.append(self.yourGuess)
        # else:
        #     sentence = 'You have guessed this number, try another one!'
        # self.Start()

mainFunction = GuessNumber.fromInput()
while mainFunction.Start():
    print('New Game~~~~~')
    mainFunction = GuessNumber.fromInput()
print('Goodbye!!')