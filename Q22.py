import RegulationFunction as rf
import math

numberList = []


def IsUsedNumberOrNO(Parameter):
    if Parameter.isdigit():
        if int(Parameter) in numberList:
            print('Please enter a number which has not been entered.')
            return False
        return True
    elif Parameter == 'NO':
        return True
    print('Please enter a number!')
    return False

def findMax(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max


print('Please enter NO if you do not want to enter any more number!!!')
while True:
    inputNumber = rf.InputFunction(f'Please enter {len(numberList) + 1}th number: ', 1, IsUsedNumberOrNO)
    if inputNumber == "NO":
        break
    numberList.append(int(inputNumber))

maxNumber = findMax(numberList)

print(f'The largest number is {maxNumber}.')