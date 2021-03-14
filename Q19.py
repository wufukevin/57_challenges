import RegulationFunction as rf
BMI_upper = 25
BMI_lower = 18.5

def IsPostiveNum(Parameter):
    if Parameter.isdigit():
        return True
    else:
        print('Please enter a postive number!')
        return False

def BMI_function(weight, height):
    return weight/(height*height)

input_weight = rf.InputFunction('What is your weight: ', 1, IsPostiveNum)
input_height = rf.InputFunction('What is your height: ', 1, IsPostiveNum)

weight = float(input_weight)
height = float(input_height)/100
bmi = BMI_function(weight, height)

print(f'Your BMI is {bmi}.')
if bmi>BMI_upper:
    print('You are overweight!')
elif bmi<BMI_lower:
    print('You are underweight')
else:
    print('You are within the ideal weight range.')