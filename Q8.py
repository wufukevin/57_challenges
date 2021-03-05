while True:
    notrepeat = 1
    people_input = input('How many people? ')
    if people_input.isdigit():
        people = float(people_input)
        if people%1 == 0:
            people = int(people)
        else:
            print('Please enter an integer.')
            notrepeat = 0
    else:
        print('Please enter a number.')
        notrepeat = 0
    if notrepeat:
        break

while True:
    notrepeat = 1
    pizza_input = input('How many pizzas do you have? ')
    if pizza_input.isdigit():
        pizza = float(pizza_input)
        if pizza%1 == 0:
            pizza = int(pizza)
        else:
            print('Please enter an integer.')
            notrepeat = 0
    else:
        print('Please enter a number.')
        notrepeat = 0
    if notrepeat:
        break

def plural(x):
    if x==0 or x==1:
        return('')
    else:
        return('s')


piece_of_pizza = pizza*8
piece_of_eachPerson = int(piece_of_pizza/people)
rest_pizza = int(piece_of_pizza%people)

print()
print(people_input+' people with '+pizza_input+' pizza'+plural(pizza_input))
print('Each person gets '+str(piece_of_eachPerson)+' piece'+plural(piece_of_eachPerson)+' of pizza.')
print('There are '+str(rest_pizza)+' leftover piece'+plural(rest_pizza)+'.')
