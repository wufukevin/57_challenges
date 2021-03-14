import RegulationFunction as rf
BMI_upper_bound = 25
BMI_lower_bound = 18.5

def BMI_function(weight, height):
    return weight/(height*height)

input_weight = rf.InputFunction('What is your weight: ', 1, rf.isDigit)
input_height = rf.InputFunction('What is your height: ', 1, rf.isDigit)

weight = float(input_weight)
height = float(input_height)/100
bmi = BMI_function(weight, height)

print(f'Your BMI is {bmi}.')
if bmi>BMI_upper_bound:
    print('You are overweight!')
elif bmi<BMI_lower_bound:
    print('You are underweight')
else:
    print('You are within the ideal weight range.')