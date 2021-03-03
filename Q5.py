while True:
    notrepeat = 1
    input_01 = input('What is the first number?')
    if input_01.isdigit():
        num_01 = float(input_01)
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
    input_02 = input('What is the second number?')
    if input_02.isdigit():
        num_02 = float(input_02)
        if num_02<0:
            print('Please enter a postive number!')
            notrepeat = 0
    else:
        print('Please enter a number!')
        notrepeat = 0

    if notrepeat:
        break


ans_01 = str(num_01+num_02)
ans_02 = str(num_01-num_02)
ans_03 = str(num_01*num_02)
ans_04 = str(num_01/num_02)
num_01 = str(num_01)
num_02 = str(num_02)

print(num_01+' + '+num_02+' = '+ans_01+'\n'
+num_01+' - '+num_02+' = '+ans_02+'\n'
+num_01+' * '+num_02+' = '+ans_03+'\n'
+num_01+' / '+num_02+' = '+ans_04)