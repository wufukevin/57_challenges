import RegulationFunction as rf

def IsOneOrTwo(Parameter):
    if Parameter == '1' or Parameter=='2':
        return True
    else:
        print('Please enter correct number')
        return False
    
def Isdigit(Parameter):
    if Parameter.isdigit():
        return True
    else:
        print('Please enter a number!')
        return False

def IsFeet(unit_choose):
    if unit_choose == '1':
        return False
    else:
        return True

def anotherUnit(unit_choose):
    if unit_choose == '1':
        return 'feet'
    else:
        return 'meters'

unit_choose = rf.InputFunction('What unit do you want ot enter? 1) meter 2)feet ? ', 1, IsOneOrTwo)

unit = 'feet' if IsFeet(unit_choose) else 'meter'

input_01 = rf.InputFunction(f'What is the length of the room in {unit} ? ', 1, Isdigit)
input_02 = rf.InputFunction(f'What is the width of the room in {unit} ? ', 1, Isdigit)

length = float(input_01)
width = float(input_02)

def conversionFrom(num, unit_choose):
    feetToMeterRatio = 0.09290304
    if IsFeet(unit_choose):
        return num*feetToMeterRatio
    else:
        return num/feetToMeterRatio
plate = conversionFrom(length*width, unit_choose)

print()
print(f'You entered dimensions of {length} {unit} by {width} {unit}.')
print('The area is')
print(f'{round(length*width, 3)} square {unit}')
print(f'{round(plate, 3)}  square {anotherUnit(unit_choose)}')
