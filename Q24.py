import RegulationFunction as rf
import math

print('Enter two strings and I\'ll tell you if they are anagrams: ')
print('')

def IsAnagram(FirstString, SecondString):
    if len(FirstString) != len(SecondString):
        return False
    for char_1 , char_2 in zip(FirstString, reversed(SecondString)):
        if char_1 != char_2:
            return False
    return True


InputFirstString = rf.InputFunction('Enter the first string: ')
InputSecondString = rf.InputFunction('Enter the second string: ')

if IsAnagram(InputFirstString, InputSecondString):
    ans = ''
else:
    ans = 'not'

print(f'\"{InputFirstString}\" and \"{InputSecondString}\" are {ans} anagrams.')