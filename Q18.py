import RegulationFunction as rf

def isFloat(numStr):
    flag = False
    numStr = str(numStr).strip().lstrip('-').lstrip('+')
    try:
        numFloat = float(numStr)
        flag = True
    except Exception as ex:
        print("isFloat() - error: " + str(ex))
    return flag

def correctUnitInput(unitString):
    unit = unitString.lower()
    correctunit = unit == 'c' or unit == 'f'
    if not correctunit:
        print('Please choose the options.')
    return correctunit

def CF_conversion(From, temperature):
    if From == 'Celsius':
        return temperature*9/5+32
    else:
        return (temperature-32)*5/9

print('Press C to convert from Fahrenheit to Celsius.')
print('Press F to convert from Celsius to Fahrenheit.')
input_unit = rf.InputFunction('Your choice: ', 1, correctUnitInput)
print('')
isToCelsius = input_unit.lower() == 'c' 
if isToCelsius:
    From = 'Fahrenheit'
    To =  'Celsius'
else:
    From = 'Celsius'
    To = 'Fahrenheit'

input_temperature = rf.InputFunction(f'Please enter the temperature in {From}: ', 1, rf.isFloat)

conversedTemperature = CF_conversion(From, float(input_temperature))

print(f'The temperature in {To} is {conversedTemperature} .')