import RegulationFunction as rf

def Isdigit(Parameter):
    if Parameter.isdigit():
        return True
    else:
        print('Please enter a number!')
        return False

def IsFeet(unit_choose):
    if unit_choose == 1:
        return False
    else:
        return True

def anotherUnit(unit_choose):
    if unit_choose == 1:
        return 'feet'
    else:
        return 'meters'

unit_choose = int(input('What unit do you want ot enter? 1) meter 2)feet ? '))

unit = 'feet' if IsFeet(unit_choose) else 'meter'

input_01 = rf.InputFunction(f'What is the length of the room in {unit} ? ', 1, Isdigit)
input_02 = rf.InputFunction(f'What is the width of the room in {unit} ? ', 1, Isdigit)

length = float(input_01)
width = float(input_02)

def conversion(num, unit_choose):
    if IsFeet(unit_choose):
        return num*0.09290304
    else:
        return num/0.09290304

print()
print(f'You entered dimensions of {length} {unit} by {width} {unit}.')
print('The area is')
print(f'{round(length*width, 3)} square {unit}')
print(f'{round(conversion(length*width, unit_choose), 3)}  square {anotherUnit(unit_choose)}')
