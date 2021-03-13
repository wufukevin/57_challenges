import math
import RegulationFunction as rf
taxInWI = 5.5


def isDigit(Parameter):
    try:
        floatParameter = float(Parameter)
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

def WIJudgment(state):
    stateInLower = state.lower()
    if stateInLower == 'wi' or stateInLower == 'wisconsin':
        return True
    return False


input_order = rf.InputFunction('What is the order amount? ', 1, isDigit)
input_state = rf.InputFunction('What is the state? ', 2)

order = float(input_order)
tax = round(order*taxInWI/100,2)
totalInWI = order+tax

if WIJudgment(input_state):
    print(f'The subtotal is ${order}.')
    print(f'The tax is ${tax}.')
    print(f'The total is ${totalInWI}.')
else:
    print(f'The total is ${order}.')


