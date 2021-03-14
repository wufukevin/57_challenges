import RegulationFunction as rf
import math

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

def IsMonthNum(Parameter):
    try:
        intParameter = int(Parameter)
        if intParameter < 1 or intParameter > 12:
            print('Please enter a number between 1 and 12.')
            return False
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

input_monthNumber = rf.InputFunction('Please enter the number of the month: ', 1, IsMonthNum)
month = numberToMonth[input_monthNumber]

print(f'The name of the month is {month}.')