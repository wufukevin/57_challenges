import flickrapi  #with python 2
import urllib
from PIL import Image

# Flickr api access key
FLICKR_PUBLIC = '11a2de6a46b76c9c1d2243df5aec8079'
FLICKR_SECRET = '5a17b181310ed11b'
flickr = flickrapi.FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, cache=True)

keyword = 'nature'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,  # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    url = photo.get('url_c')
    urls.append(url)
    if i > 3:
        break

text = '''
        <html>
            <head>
            <title>Photo Search</title>
            </head>
            <body>
                <h1>Photos about "{}"</h1>
                <img src="{}" width="200" height="200">
                <img src="{}" width="200" height="200">
                <img src="{}" width="200" height="200">
            </body>
        </html>
        '''.format(keyword,urls[0],urls[1],urls[2])

with open("Q49.html", "w") as f:
    f.write(text)

