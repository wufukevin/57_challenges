import requests
import RegulationFunction as rf
import math
import random
import operator
API = "http://api.open-notify.org/astros.json"

class WhoInSpace:
    def __init__(self):
        r= requests.get(API)
        self.inputData = r.json()['people']


    def show(self):
        sortedByLengthOfName = sorted(self.inputData, key = lambda person:len(person['name']),reverse=True)
        sortedByLengthOfCraft = sorted(self.inputData, key = lambda person:len(person['craft']),reverse=True)
        nameMaxLength = len(sortedByLengthOfName[0]['name'])
        craftMadLength = len(sortedByLengthOfCraft[0]['craft'])
        format_template = '%%-%ds | %%-%ds'
        formatter = format_template % (nameMaxLength, craftMadLength)

        print(f'There are {len(self.inputData)} people in space right now:')
        print(formatter % ('Name', 'Craft'))
        print('-'*nameMaxLength + ' | ' + '-'*craftMadLength)
        for element in self.inputData:
            print(formatter % (element['name'], element['craft']))

mainFunction = WhoInSpace()
mainFunction.show()