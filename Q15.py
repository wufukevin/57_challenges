import RegulationFunction as rf

def isDigit(Parameter):
    try:
        floatParameter = float(Parameter)
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

def presetEnsureFunction(everyThing):
    return True

input_1 = rf.InputFunction('What is the order amount? ', 1, isDigit)
print(input_1)
input_2 = rf.InputFunction('What is the order amount? ', 1, presetEnsureFunction)
print(input_2)