import math
import RegulationFunction as rf

''' 無條件進位 dig :小數點後第幾位
'''
def roundUp(num, dig):
    digNum = 1
    for i in range(dig):
        digNum *= 10
    return(math.ceil(num*digNum)/float(digNum))

def isFloat(numStr):
    flag = False
    numStr = str(numStr).strip().lstrip('-').lstrip('+')
    try:
        numFloat = float(numStr)
        flag = True
    except Exception as ex:
        print("isFloat() - error: " + str(ex))
    return flag

def isDigit(Parameter):
    try:
        floatParameter = float(Parameter)
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

def calculateSimpleInterest(rate, principal, year):
    return(roundUp(principal*(1+rate*year/100), 1))


input_principal = rf.InputFunction('Enter the principal: ', 1, isDigit)
input_rate = rf.InputFunction('nter the rate: ', 2, isFloat)
input_year = rf.InputFunction('Enter the number of years: ', 3, isDigit)

principal = int(input_principal)
rate = float(input_rate)
year = int(input_year)

for eachYear in range(year):
    eachYear += 1
    print(f'After {eachYear} years at {rate} %, the investment will be worth ${calculateSimpleInterest(rate,principal,eachYear)}.')

