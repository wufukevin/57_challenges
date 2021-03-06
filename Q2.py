import sys
'''
isNoInput = True
while isNoInput:
    inputString = input('What is the input string?')
    if inputString:
        isNoInput = False

print(f'{inputString} has {len(inputString)} characters.')
'''

inputLength = ''

def isNoInput(inputLength):
    return inputLength == 0

while isNoInput(inputLength): 
    inputString = input('What is the input string?')
    inputLength = len(inputString)

print(f'{inputString} has {inputLength} characters.')
    
