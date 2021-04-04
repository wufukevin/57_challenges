import RegulationFunction as rf
import math
import random


class WinnerPicker:
    def __init__(self):
        self.contestantList = []
        self.endOfSignUp = False

    def signUp(self):
        name = input('Enter a name: ')
        if name == '':
            self.endOfSignUp = True
        else:
            if name in self.contestantList:
                print('You have already singed up!!')
            else:
                self.contestantList.append(name)

    def drawLot(self):
        if len(self.contestantList) == 0:
            print('No one want to play this game QQ')
            return
        lot = random.randint(1, len(self.contestantList))-1
        print(f'The winner is... {self.contestantList[lot]}.')
        del self.contestantList[lot]



mainFunction = WinnerPicker()
while not mainFunction.endOfSignUp:
    mainFunction.signUp()
mainFunction.drawLot()
mainFunction.drawLot()
mainFunction.drawLot()

