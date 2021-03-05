squareFeetForOneGallon = 350

while True:
    notrepeat = 1
    length_input = input('What is the length of the room in feet ? ')
    if length_input.isdigit():
        length = float(length_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break

while True:
    notrepeat = 1
    width_input = input('What is the width of the room in feet ? ')
    if width_input.isdigit():
        width = float(width_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break

def gallonNumber(x):
    if x%squareFeetForOneGallon == 0:
        return str(int(x/squareFeetForOneGallon))
    else:
        return str(int(x/squareFeetForOneGallon)+1)

area = length*width

print('You will need to purchase '+gallonNumber(area)+' gallons of paint to cover '+str(area)+' square feet.')
