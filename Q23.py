import RegulationFunction as rf
import math

ansString = '0'
questionAndAnswer = {
    '0': ['q','Is the car silent when you turn the key?' ],
    '00': ['q','Does the car make a clicking noise? '],
    '01': ['q','Are the battery terminals corroded? '],
    '000': ['q', 'Does the car crank up but fail to start? '],
    '001': ['a', 'Replace the battery.'],
    '010': ['a', 'Replace cables and try again.'],
    '011': ['a', 'Clean terminals and try starting again.'],
    '0000': ['q', 'Does the engine start and then die? '],
    '0001': ['a', ' Check spark plug connections.'],
    '00000': ['a', 'I do not know how to answer!!!!!!!!!'],
    '00001': ['q', 'Does your car have fuel injection? '],
    '000010': ['a', 'Check to ensure the choke is opening and closing.'],
    '000011': ['a', ' Get it in for service.'],
}

def yesOrNO(Parameter):
    if Parameter=='y' or Parameter == 'n':
        return True
    print('Please enter a number!')
    return False

while True:
    input_ans = rf.InputFunction(questionAndAnswer[ansString][1], 1, yesOrNO)
    ans = '1' if input_ans == 'y' else '0'
    ansString = ansString + ans
    if questionAndAnswer[ansString][0] == 'a':
        print(questionAndAnswer[ansString][1])
        break
