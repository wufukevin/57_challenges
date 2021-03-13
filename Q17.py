import RegulationFunction as rf
legalBloodAlcoholContent = 0.08
def IsPostiveNum(Parameter):
    try:
        floatParameter = float(Parameter)
        if floatParameter <0:
            print('Please enter a postive number.')
            return False
        return True
    except Exception as ex :
        print('Please enter a number!')
        return False

def correctGenderInput(Parameter):
    if Parameter == '1' or Parameter == '2':
        return True
    print('Please choose the options.')
    return False

'''
Blood Alcohol Content:
    A is total alcohol consumed, in ounces (oz). 
    W is body weight in pounds.
    r is the alcohol distribution ratio:
        – 0.73 for men
        – 0.66 for women
    H is number of hours since the last drink.
'''
def BAC_fucntion(A,W,r,H):
    return(A*5.14/W*r - 0.015*H)


input_weight = rf.InputFunction('What is your weight? ', 1, IsPostiveNum)
input_gender = rf.InputFunction('What is your gender? (1)man (2)woman', 1, correctGenderInput)
input_numberOfDrink = rf.InputFunction('What is the number of drinks? ', 1, IsPostiveNum)
input_alcoholInDrink = rf.InputFunction('What is the amount of alcohol by volume of the drinks consumed? ', 1, IsPostiveNum)
input_timeAfterLastDrink = rf.InputFunction('What is the amount of time since your last drink? ', 1, IsPostiveNum)

totalAlcohol = float(input_numberOfDrink)*float(input_alcoholInDrink)
weight = float(input_weight)
if input_gender == '1':
    alcoholDistributionRatio = 0.73
else:
    alcoholDistributionRatio = 0.66
hour = float(input_timeAfterLastDrink)

bac = BAC_fucntion(totalAlcohol, weight, alcoholDistributionRatio, hour)

print(f'Your BAC is {bac}')
print('It is legal for you to drive.') if bac>legalBloodAlcoholContent else print('It is not legal for you to drive.')