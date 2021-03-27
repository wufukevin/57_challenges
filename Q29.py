import RegulationFunction as rf

def isCorrectRate(parameter):
    isdigit = parameter.isdigit()
    if not isdigit:
        print('Sorry. That\'s not a valid input.')
    elif parameter == '0':
        print('Rate can not be zero!!!')
        isdigit = False
    return isdigit


inputString = rf.InputFunction('What is the rate of return? ',1,isCorrectRate)
yearNeeded = float(72/int(inputString))
print(f'It will take {yearNeeded} years to double your initial investment.')