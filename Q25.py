import enum
import RegulationFunction as rf
import math

class passwordStrength(enum.Enum):
    very_weak = 0
    weak = 1
    strong = 2
    very_strong =3

def hasInput(inputString):
    return True if inputString else False

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
    if len(password) < 8:
        if digitNumber == len(password):
            return passwordStrength.very_weak
        elif alphaNumber == len(password):
            return passwordStrength.weak
    else:
        if digitNumber != 0 and alphaNumber != 0:
            if otherNumber != 0:
                return passwordStrength.very_strong
            return passwordStrength.strong


inputPassword = rf.InputFunction('Please enter a password: ',1,hasInput)

strengthTable = \
    {
        passwordStrength.very_weak : 'very weak',
        passwordStrength.weak : 'weak',
        passwordStrength.strong : 'strong',
        passwordStrength.very_strong : 'very strong',
    }
passwordStrengthNumber = passwordValidator(inputPassword)
strengthAdj = strengthTable[passwordStrengthNumber]

print(f'The password \'{inputPassword}\' is a {strengthAdj} password.')