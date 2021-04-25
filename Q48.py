import requests
import RegulationFunction as rf
import math
import random
import operator
import json
import time
import enum


# class windDegEnum(enum):
#
#     0 = "N"

def degToCompass(deg):
    val = int((deg / 22.5) + .5)
    compassArr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return (compassArr[(val % 16)])


class CityWeather(object):
    def __init__(self, weather_data):
        self.temp = weather_data['main']['temp']
        self.sunrise = weather_data['sys']['sunrise']
        self.sunset = weather_data['sys']['sunset']
        self.wind = weather_data['wind']['deg']

    def _convert_time(self, time):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time))

    def get_sunrise_time(self):
        return self._convert_time(self.sunrise)

    def get_sunset_time(self):
        return self._convert_time(self.sunset)

    def get_wind_in_compass(self):
        return degToCompass(self.wind)


class GrabbingWeather:
    def __init__(self):
        API = "https://api.openweathermap.org/data/2.5/weather"
        self.city = input('Where are you? ')
        if self.city.split()[1] == 'IL':
            self.city = self.city.split()[0] + ',US-IL'
        parameters = {
            "q": self.city,
            'appid': '2dfc75f30ac9ccae831a0b6fdbd4124c'
        }
        self.weather_data = CityWeather(requests.get(API, params=parameters).json())

    def showWeather(self):
        print(f'{self.city} weather:')

        print(f'{self.weather_data.temp} degrees Fahrenheit')
        print(f'sun rise time: {self.weather_data.get_sunrise_time()}')
        print(f'sun set time: {self.weather_data.get_sunset_time()}')
        print(f'the wind is come from {self.weather_data.get_wind_in_compass()}')


mainFunction = GrabbingWeather()
mainFunction.showWeather()
