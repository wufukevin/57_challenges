import RegulationFunction as rf
import math
import re


class InputData:
    def __init__(self, firstName, lastName, zipCode, employeeID):
        self.inputList = [firstName, lastName, zipCode, employeeID]

    @classmethod
    def from_input(cls):
        return cls(
            rf.InputFunction('Enter the first name: '),
            rf.InputFunction('Enter the last name: '),
            rf.InputFunction('Enter the ZIP code: '),
            rf.InputFunction('Enter an employee ID: ')
        )

    def validateInput(self):
        noError = True
        namePattern = r"[a-zA-Z]{2,}"
        zipPattern = r"[0-9]+"
        idPattern = r"[a-zA-Z]{2}-[0-9]{4}"

        patternList = [namePattern,namePattern,zipPattern,idPattern]
        inputName = ['first name', 'last name', 'zipCode', 'employeeID']
        for i, inputString in enumerate(self.inputList):
            if inputString:
                if not re.fullmatch(patternList[i], inputString):
                    noError = False
                    if i < 2:
                        print(f"\"{inputString}\" is not a valid {inputName[i]}. It is too short.")
                    elif i == 2:
                        print(f'The ZIP code must be numeric.')
                    else:
                        print(f'{inputString} is not a valid ID.')
            else:
                noError = False
                print(f"The {inputName[i]} must be filled in.")

        if noError:
            print('There were no errors found.')


mainFunction = InputData.from_input()
mainFunction.validateInput()