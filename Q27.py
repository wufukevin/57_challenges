import RegulationFunction as rf
import math
import re

class Validator:
    def __init__(self, name, value, regex, failMessage):
        self.name = name
        self.value = value
        self.regex = regex
        self.failMessage = failMessage

    def validate(self):
        ans = True
        if self.value == '':
            print(f"The {self.name} must be filled in.")
            ans = False
        elif not re.fullmatch(self.regex, self.value):
            print(self.failMessage)
            ans = False
        return ans


class UserInfo:
    def __init__(self, firstName, lastName, zipCode, employeeID):
        self.inputList = [Validator('first name', firstName, r"[a-zA-Z]{2,}", f"{firstName} is not a valid first name. It is too short."),
                          Validator('last name', lastName, r"[a-zA-Z]{2,}", f"{lastName} is not a valid last name. It is too short."),
                          Validator('zipCode', zipCode, r"[0-9]+", f'The ZIP code must be numeric.'),
                          Validator('employeeID', employeeID, r"[a-zA-Z]{2}-[0-9]{4}", f'{employeeID} is not a valid ID.')]

    @classmethod
    def fromInput(cls):
        return cls(
            rf.InputFunction('Enter the first name: '),
            rf.InputFunction('Enter the last name: '),
            rf.InputFunction('Enter the ZIP code: '),
            rf.InputFunction('Enter an employee ID: ')
        )

    def validateInput(self):
        noError = True
        for i in self.inputList:
            if not i.validate():
                noError = False

        if noError:
            print('There were no errors found.')


userInfo = UserInfo.fromInput()
userInfo.validateInput()

