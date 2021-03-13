import RegulationFunction as rf

passwordMap = [['a','111'],['b','222'],['c','333'],['d','444']]

for username, password in passwordMap:
    print(username, password)

def IsPasswordCorrect(inputPassword):
    if inputPassword==correctPassword:
        print('Welcome!')
        return True
    else:
        print('I do not know you.')
        print('Please enter again.')
        return False


input_username = rf.InputFunction('What is the username? ')
for username, password in passwordMap:
    if username==input_username:
        correctPassword = password
input_password = rf.InputFunction('What is the password? ',1,IsPasswordCorrect)