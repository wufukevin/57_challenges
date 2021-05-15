import math
import RegulationFunction as rf
taxInWI = 5.5

def isWI(state):
    stateInLower = state.lower()
    return stateInLower == 'wi' or stateInLower == 'wisconsin'


input_order = rf.InputFunction('What is the order amount? ', 1, rf.isDigit)
input_state = rf.InputFunction('What is the state? ', 2)

order = float(input_order)
tax = round(order*taxInWI/100,2)
totalInWI = order+tax

if isWI(input_state):
    print(f'The subtotal is ${order} .')
    print(f'The tax is ${tax} .')
    print(f'The total is ${totalInWI} .')
else:
    print(f'The total is ${order} .')


