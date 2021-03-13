import RegulationFunction as rf
legalDrivingAge = 16

def IsInteger(Parameter):
    if not Parameter.isdigit():
        print('Please enter a valid age!')
        return False

    num = float(Parameter)
    if num%1==0:
        return True
    
    print('Please enter a valid age!')
    return False

input_age = rf.InputFunction('What is your age? ', 1, IsInteger)
age = int(input_age)
print('You are not old enough to legally drive.') if age<legalDrivingAge else print('You are old enough to legally drive.')