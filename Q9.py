import RegulationFunction as rf
import math
squareFeetForOneGallon = 350

def Isdigit(Parameter):
    try:
        floatParameter = float(Parameter)
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

input_length = rf.InputFunction('What is the length of the room in feet ? ', 1, Isdigit)
input_width = rf.InputFunction('What is the width of the room in feet ? ', 2, Isdigit)

length = float(input_length)
width = float(input_width)

def gallonNeedAmount(area):
    return int(math.ceil(area/squareFeetForOneGallon))

area = length*width

print(f'You will need to purchase {gallonNeedAmount(area)} gallons of paint to cover {area} square feet.')
