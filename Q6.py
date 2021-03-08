from datetime import datetime
import RegulationFunction as rf

def IsPostiveNum(Parameter):
    if Parameter.isdigit():
        num = int(Parameter)
        if num>0:
            return True
        else:
            print('Please enter a postive number!')
            return False
    else:
        print('Please enter a number!')
        return False


input_01 = rf.InputFunction('What is your current age? ', 1, IsPostiveNum)
input_02 = rf.InputFunction('At what age would you like to retire? ', 2, IsPostiveNum)

now = datetime.now()
num_01 = int(input_01)
num_02 = int(input_02)

yearsLeft = num_02-num_01
retireYear = now.year+yearsLeft

if yearsLeft<0:
    print('You can already retire.')
else:
    print(f'You have {yearsLeft} years left until you can retire.')
    print(f"It's {now.year}, so you can retire in {retireYear}.")