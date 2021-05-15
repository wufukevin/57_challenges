import math
import RegulationFunction as rf

def roundUp(num, dig):
    digNum = math.pow(10, dig)
    return math.ceil(num*digNum)/digNum

def isFloat(numStr):
    try:
        numFloat = float(numStr)
        return True
    except Exception as ex:
        print("isFloat() - error: " + str(ex))
    return False

def isDigit(Parameter):
    try:
        floatParameter = float(Parameter)
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

def calculateSimpleInterest(rate, principal, year):
    return(roundUp(principal*(100+rate*year)/100, 1))


input_principal = rf.InputFunction('Enter the principal: ', 1, isDigit)
input_rate = rf.InputFunction('Enter the rate: ', 2, isFloat)
input_year = rf.InputFunction('Enter the number of years: ', 3, isDigit)

principal = int(input_principal)
rate = float(input_rate)
year = int(input_year)

for eachYear in range(year):
    eachYear += 1
    print(f'After {eachYear} years at {rate} %, the investment will be worth ${calculateSimpleInterest(rate,principal,eachYear)}.')

