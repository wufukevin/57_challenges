import requests
import RegulationFunction as rf
import math
import random
import operator
import json
API = "https://api.openweathermap.org/data/2.5/weather"

class GrabbingWeather:
    def __init__(self):
        parameters = {
            "q": 'Chicago',
            'appid': '2dfc75f30ac9ccae831a0b6fdbd4124c'
        }
        r= requests.get(API, params=parameters)
        self.data = json.dumps(r.json(), sort_keys=True, indent=4)



    def showWeather(self):
        print(self.data)

mainFunction = GrabbingWeather()
mainFunction.showWeather()