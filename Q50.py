# import flickrapi  #with python 2
import GUI_caller as gui
import variable as v
import json
import urllib
import requests
import xml

def on_click_run_the_program(inputList):
    mainfunction = MovieRecommendations(*inputList)
    mainfunction.searchRequest()
    mainfunction.showSearchResult()

class MovieRecommendations:
    def __init__(self):
        API = 'https://imdb-api.com/en/API/'
        #   'https://imdb-api.com/Account/PublicApiKeys'  change IP
        ApiKey = 'pk_cff2qy6x5iuq1a4p7/'
        self.idSearchAPI = API+'SearchTitle/'+ApiKey
        self.rateSearchAPI = API+'Ratings/'+ApiKey


        # movieName = 'Guardians of the Galaxy'
    def searchRequest(self, *input):
        self.movieName = input[0]
        self.movieYear = None
        self.movieRate = None
        idSearch = requests.get(self.idSearchAPI+self.movieName).json()
        # print(requests.get(self.idSearchAPI+self.movieName).url)
        moveId = idSearch['results'][0]['id']

        rateSearch = requests.get(self.rateSearchAPI+moveId).json()
        self.movieYear = rateSearch['year']
        self.movieRate = float(rateSearch['imDb'])

    def showSearchResult(self):
        print(f'Title: {self.movieName}')
        print(f'Year: {self.movieYear}')
        print(f'Rating: {self.movieRate}')
        # print(f'Running Time: 121 minutes')
        # print(f'Description: From Marvel...')

        if self.movieRate > 8.0:
            print(f'You should watch this movie right now!')
        elif self.movieRate < 5.0:
            print(f'You should not watch this movie!')
        else:
            print(f'To watch or not to watch, this is a question!')


        # print(json.dumps(rateSearch, indent = 4))

if __name__ == '__main__':

    # mainFunction = MovieRecommendations(input('Enter the name of a movie: '))
    # mainFunction.searchRequest()
    # mainFunction.showSearchResult()

    v.mainClass = 'MovieRecommendations'
    gui.initial()
    gui.createInputWidget('Enter the name of a movie: ')
    mainFunction = MovieRecommendations()
    # mainFunction.searchRequest()
    # mainFunction.showSearchResult()
    gui.loop(movieRecommendation=mainFunction)