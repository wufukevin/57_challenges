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

def calculateCompoundInterest(rate, principal, year, numPerYear):
    ans = principal
    comPerTime = 1+rate/numPerYear/100
    for i in range(year*numPerYear):
        ans *= comPerTime
    return(roundUp(ans, 2))

input_principal = rf.InputFunction('What is the principal amount? ', 1, isDigit)
input_rate = rf.InputFunction('What is the rate? ', 2, isFloat)
input_year = rf.InputFunction('What is the number of years? ', 3, isDigit)
input_numberPerYear = rf.InputFunction('What is the number of times the interest is compounded per year? ', 4, isDigit)

principal = int(input_principal)
rate = float(input_rate)
year = int(input_year)
numberPerYear = int(input_numberPerYear)
amount = calculateCompoundInterest(rate, principal, year, numberPerYear)

print(f'${principal} invested at {rate}% for {year} years compounded {numberPerYear} times per year is ${amount}.')