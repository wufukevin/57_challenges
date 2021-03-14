import RegulationFunction as rf
import math

numberList = []

numberToMonth = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'Auguest',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

def IsUsedNumberOrNO(Parameter):
    if Parameter.isdigit():
        for number in numberList:
            if float(Parameter) == number:
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
        if number>max:
            max = number
    return max


print('Please enter NO if you do not want to enter any more number!!!')
while True:
    input_Number = rf.InputFunction(f'Please enter {len(numberList)+1}th number: ', 1, IsUsedNumberOrNO)
    if input_Number == "NO":
        break
    numberList.append(float(input_Number))

maxNumber = findMax(numberList)

print(f'The largest number is {maxNumber}.')