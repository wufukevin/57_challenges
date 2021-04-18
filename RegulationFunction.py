from collections.abc import Callable
import math

def presetEnsureFunction(everyThing):
    return True


def InputFunction(InputString, InputOrder = '1', EnsureFunction = presetEnsureFunction):
    InputNotCorrect = True
    while InputNotCorrect:
        InputNotCorrect = False
        Input = input(InputString)
        if not EnsureFunction(Input):
            InputNotCorrect = True
    return Input

def roundUp(num, dig):
    digNum = math.pow(10, dig)
    return math.ceil(num*digNum)/digNum

def isYesOrNo(ans):
    if ans =='y' or ans == 'y':
        return True
    return False

def isFloat(numStr):
    try:
        numFloat = float(numStr)
        return True
    except Exception as ex:
        print("isFloat() - error: " + str(ex))
    return False

def isDigit(Parameter):
    isdigit = Parameter.isdigit()
    if not isdigit:
        print('Please enter a number!')
    return isdigit

def isInteger(Parameter):
    isinteger = Parameter.isdigit() and float(Parameter)%1==0
    if not isinteger:
        print('Please enter an integer!')
    return isinteger
