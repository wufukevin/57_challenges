import RegulationFunction as rf
import math


def passwordValidator(password):
    digitNumber = 0
    alphaNumber = 0
    otherNumber = 0
    for char in password:
        if char.isdigit():
            digitNumber += 1
        elif char.isalpha():
            alphaNumber += 1
        else:
            otherNumber += 1
    len = digitNumber+alphaNumber+otherNumber
    if len<8:
        if alphaNumber == 0 and otherNumber == 0:
            return(0)
        elif digitNumber == 0 and otherNumber == 0:
            return(1)
    else:
        if digitNumber != 0 and alphaNumber != 0:
            if otherNumber != 0 :
                return(3)
            return(2)


inputPassword = rf.InputFunction('Please enter a password: ')

strengthTable = ['very weak','weak','strong','very strong']
passwordStrengthNumber = passwordValidator(inputPassword)
strengthAdj = strengthTable[passwordStrengthNumber]

print(f'The password \'{inputPassword}\' is a {strengthAdj} password.')