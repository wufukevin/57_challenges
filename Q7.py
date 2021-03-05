unit = int(input('What unit do you want ot enter? 1) meter 2)feet ?')) - 1

unit_str = 'feet' if unit else 'meter'

while True:
    notrepeat = 1
    length_input = input('What is the length of the room in '+unit_str+'?')
    if length_input.isdigit():
        length = float(length_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break

while True:
    notrepeat = 1
    width_input = input('What is the width of the room in '+unit_str+'?')
    if width_input.isdigit():
        width = float(width_input)
    else:
        print('Please enter a valid number.')
        notrepeat = 0
    if notrepeat:
        break

def conversion(x):
    if unit:
        return x*0.09290304
    else:
        return x/0.09290304

print('You entered dimensions of '+length_input+' '+unit_str+' by '+width_input+' '+unit_str+'.')
print('The area is')
if unit:
    print(str(round(length*width, 3))+' square feet')
    print(str(round(conversion(length*width), 3))+ ' square meters')
else:
    print(str(round(length*width, 3))+' square meters')
    print(str(round(conversion(length*width), 3))+' squre feet')
