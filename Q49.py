# import flickrapi  #with python 2
import json
import urllib
import requests
import xml
from PIL import Image

# Flickr api access key
FLICKR_PUBLIC = '11a2de6a46b76c9c1d2243df5aec8079'
FLICKR_SECRET = '5a17b181310ed11b'
# flickr = flickrapi.FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, cache=True)

API = "https://www.flickr.com/services/rest/"
keyword = 'nature'

parameters = {
    "method": 'flickr.photos.search',
    'api_key': '11a2de6a46b76c9c1d2243df5aec8079',
    'text': keyword,
    'extras': 'url_c',
    'format': 'json',
    'nojsoncallback':1
}
photos = requests.get(API, params=parameters).json()
# print(json.loads())

# photos = flickr.walk(text=keyword,
#                      tag_mode='all',
#                      tags=keyword,
#                      extras='url_c',
#                      per_page=100,  # may be you can try different numbers..
#                      sort='relevance')

urls = []
for i, photo in enumerate(photos['photos']['photo']):
    url = photo.get('url_c')
    urls.append(url)
    if i > 3:
        break
#
text = f'''
        <html>
            <head>
            <title>Photo Search</title>
            </head>
            <body>
                <h1>Photos about "{keyword}"</h1>
                <img src="{urls[0]}" width="200" height="200">
                <img src="{urls[1]}" width="200" height="200">
                <img src="{urls[2]}" width="200" height="200">
            </body>
        </html>
        '''

with open("Q49.html", "w") as f:
    f.write(text)
