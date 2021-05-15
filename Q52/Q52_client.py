# import flickrapi  #with python 2
import json
import urllib
import requests
import time

API = "http://127.0.0.1:5000/localTime"

data = requests.get(API).json()
servertime = data['localTime']
print(servertime)
# print(f'The current time is {time[3]}:{time[4]}:{time[5]} {time[1]}/{time[2]}/{time[0]}.')
