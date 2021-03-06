import RegulationFunction as rf

def IsInteger(Parameter):
    if Parameter.isdigit():
        num = float(Parameter)
        if num%1==0:
            return True
        else:
            print('Please enter an integer!')
            return False
    else:
        print('Please enter a number!')
        return False

def plural(num):
    if num==0 or num==1:
        return('')
    else:
        return('s')

input_01 = rf.InputFunction('How many people? ', 1, IsInteger)
input_02 = rf.InputFunction('How many pizzas do you have? ', 2, IsInteger)

people = int(input_01)
pizza = int(input_02)

piece_of_pizza = pizza*8
piece_of_eachPerson = int(piece_of_pizza/people)
rest_pizza = int(piece_of_pizza%people)

print()
print(f'{people} people with {pizza} pizza{plural(pizza)}')
print(f'Each person gets {piece_of_eachPerson} piece{plural(piece_of_eachPerson)} of pizza.')
print(f'There are {rest_pizza} leftover piece{plural(rest_pizza)}.')
