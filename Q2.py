import sys

while True:
    notRepeat = 1
    inputString = input('What is the input string?')
    if not inputString:
        notRepeat = 0
    if  notRepeat:
        break

print(inputString + ' has ' + str(len(inputString)) + ' characters.')