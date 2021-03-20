import RegulationFunction as rf
import math

print('Enter two strings and I\'ll tell you if they are anagrams: ')
print('')

def IsAnagram(FirstString, SecondString):
    stringLen = len(FirstString)
    if stringLen != len(SecondString):
        return False
    for indexFromHead in range(stringLen):
        indexFromTail = stringLen - indexFromHead - 1
        if FirstString[indexFromHead] != SecondString[indexFromTail]:
            return False
    return True


InputFirstString = rf.InputFunction('Enter the first string: ')
InputSecondString = rf.InputFunction('Enter the second string: ')

if IsAnagram(InputFirstString, InputSecondString):
    ans = ''
else:
    ans = 'not'

print(f'\"{InputFirstString}\" and \"{InputSecondString}\" are {ans} anagrams.')