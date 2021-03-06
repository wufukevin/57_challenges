import RegulationFunction as rf

def IsPostiveNum(Parameter):
    if Parameter.isdigit():
        return True
    else:
        print('Please enter a postive number!')
        return False


input_01 = rf.InputFunction('What is the first number? ', 1, IsPostiveNum)
input_02 = rf.InputFunction('What is the second number? ', 2, IsPostiveNum)

num_01 = int(input_01)
num_02 = int(input_02)
ans_add = str(num_01+num_02)
ans_sub = str(num_01-num_02)
ans_mul = str(num_01*num_02)
ans_div = str(int(num_01/num_02))

print(f'{num_01} + {num_02} = {ans_add} \n{num_01} - {num_02} = {ans_sub} \n{num_01} * {num_02} = {ans_mul} \n{num_01} / {num_02} = {ans_div}')