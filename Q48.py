import requests
import RegulationFunction as rf
import math
import random
import operator
import json
import time

API = "https://api.openweathermap.org/data/2.5/weather"

def degToCompass(deg):
    val=int((deg/22.5)+.5)
    compassArr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return(compassArr[(val % 16)])

class GrabbingWeather:
    def __init__(self):
        self.city = input('Where are you? ')
        parameters = {
            "q": self.city,
            'appid': '2dfc75f30ac9ccae831a0b6fdbd4124c'
        }
        self.data= requests.get(API, params=parameters).json()



    def showWeather(self):
        print(f'{self.city} weather:')
        temp = self.data['main']['temp']
        sunRiseTimeString = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.data['sys']['sunrise']))
        sunSetTimeString = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.data['sys']['sunset']))
        windCompass = degToCompass(self.data['wind']['deg'])
        print(f'{temp} degrees Fahrenheit')
        print(f'sun rise time: {sunRiseTimeString}')
        print(f'sun set time: {sunSetTimeString}')
        print(f'the wind is come from {windCompass}')

mainFunction = GrabbingWeather()
mainFunction.showWeather()