import requests
import RegulationFunction as rf
import math
import random
import operator


class WhoInSpace:
    def __init__(self):
        API = "http://api.open-notify.org/astros.json"
        r= requests.get(API)
        self.peopleInTheSpace = r.json()['people']


    def show(self):
        sortedByLengthOfName = sorted(self.peopleInTheSpace, key = lambda person:len(person['name']), reverse=True)
        sortedByLengthOfCraft = sorted(self.peopleInTheSpace, key = lambda person:len(person['craft']), reverse=True)
        nameMaxLength = len(sortedByLengthOfName[0]['name'])
        craftMadLength = len(sortedByLengthOfCraft[0]['craft'])
        formatTemplate = '%%-%ds | %%-%ds'
        formatter = formatTemplate % (nameMaxLength, craftMadLength)

        print(f'There are {len(self.peopleInTheSpace)} people in space right now:')
        print(formatter % ('Name', 'Craft'))
        print('-'*nameMaxLength + ' | ' + '-'*craftMadLength)
        for element in self.peopleInTheSpace:
            print(formatter % (element['name'], element['craft']))

mainFunction = WhoInSpace()
mainFunction.show()