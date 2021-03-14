import RegulationFunction as rf
import math
tax_WI = 5
tax_WI_EauClaire = 5.5
tax_WI_Dunn = 5.4
tax_Illinois = 8
tax = 0

def IsInteger(Parameter):
    if Parameter.isdigit() and float(Parameter)%1==0:
        return True
    print('Please enter an integer!')
    return False
def roundUp(num, dig):
    digNum = 1
    for i in range(dig):
        digNum *= 10
    return(math.ceil(num*digNum)/float(digNum))

input_order = rf.InputFunction('What is the order amount? ', 1, IsInteger)
input_state = rf.InputFunction('What state do you live in? ')
if input_state.lower() == 'wisconsin':
    input_country = rf.InputFunction('What country do you live in? ')
    if input_country.lower() == 'eau claire':
        tax = tax_WI_EauClaire
    elif input_country.lower() == 'dunn':
        tax = tax_WI_Dunn
    else:
        tax = tax_WI
elif input_state.lower() == 'illinois':
    tax = tax_Illinois

order = float(input_order)
tax_result = roundUp(order*tax/100,2)
total = order+tax_result

if tax:
    print(f'The tax is ${tax_result}.')
print(f'The total is ${total}.')