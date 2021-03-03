from datetime import datetime

now = datetime.now()

while True:
    notrepeat = 1
    input_01 = input('What is your current age?')
    if input_01.isdigit():
        num_01 = int(input_01)
        if num_01<0:
            print('Please enter a postive number!')
            notrepeat = 0
    else:
        print('Please enter a number!')
        notrepeat = 0

    if notrepeat:
        break
while True:
    notrepeat = 1
    input_02 = input('At what age would you like to retire?')
    if input_02.isdigit():
        num_02 = int(input_02)
        if num_02<0:
            print('Please enter a postive number!')
            notrepeat = 0
    else:
        print('Please enter a number!')
        notrepeat = 0

    if notrepeat:
        break

dif = num_02-num_01

if dif<0:
    print('You can already retire.')
else:
    print('You have '+str(dif)+' years left until you can retire.')
    print("It's "+str(now.year)+", so you can retire in "+str(now.year+dif)+'.')