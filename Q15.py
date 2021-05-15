import RegulationFunction as rf

passwordMap = {
    'a':'111',
    'b':'222',
    'c':'333',
    'd':'444',
}

for username, password in passwordMap.items():
#    print(username,passwordMap[username])
    print(username, password)

def IsUserExist(username):
    findUser = username in passwordMap
    if not findUser:
        print('Find no body! Please enter again.')
    return findUser

def IsPasswordCorrect(inputPassword):
    if inputPassword==passwordMap[input_username]:
        print('Welcome!')
        return True
    else:
        print('I do not know you.')
        print('Please enter again.')
        return False


input_username = rf.InputFunction('What is the username? ',1,IsUserExist)
# passwordMap.get(input_username, 'nothing')
# for username, password in passwordMap:
#     if username==input_username:
#         correctPassword = password
input_password = rf.InputFunction('What is the password? ',1,IsPasswordCorrect)

# expectedPassword = passwordMap.get(input_username)
# if expectedPassword != input_password:
#     print('I do not know you.')
#     print('Please enter again.')