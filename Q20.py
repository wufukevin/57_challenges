import RegulationFunction as rf
import math
tax_WI = 5
tax_WI_EauClaire = tax_WI+0.5
tax_WI_Dunn = tax_WI+0.4
tax_Illinois = 8
tax = 0

# def IsInteger(Parameter):
#     if Parameter.isdigit() and float(Parameter)%1==0:
#         return True
#     print('Please enter an integer!')
#     return False
# def roundUp(num, dig):
#     digNum = 1
#     for i in range(dig):
#         digNum *= 10
#     return(math.ceil(num*digNum)/float(digNum))

def getTax(state = '', country = ''):
    tax = 0
    state = state.lower()
    country = country.lower()
    if state == 'wisconsin':
        if country == 'eau claire':
            tax = tax_WI_EauClaire
        elif country == 'dunn':
            tax = tax_WI_Dunn
        else:
            tax = tax_WI
    elif state == 'illinois':
        tax = tax_Illinois
    return tax

input_order = rf.InputFunction('What is the order amount? ', 1, rf.isInteger)
input_state = rf.InputFunction('What state do you live in? ')
input_country = ''
if input_state.lower() == 'wisconsin':
    input_country = rf.InputFunction('What country do you live in? ')
tax = getTax(input_state, input_country)


order = float(input_order)
tax_result = rf.roundUp(order*tax/100,2)
total = order+tax_result

hastax = tax != 0
if hastax:
    print(f'The tax is ${tax_result}.')
print(f'The total is ${total}.')
