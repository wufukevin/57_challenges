from datetime import datetime
import hashlib
from flask import Flask, jsonify, request, redirect, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate('/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')
# firebase_admin.initialize_app(cred)
# db = firestore.client()
# doc_ref = db.collection('Q54')


serverIP = 'http://127.0.0.1:5000'
app = Flask(__name__)


def urlEncode(longUrl):
    md5 = hashlib.md5()
    md5.update(longUrl.encode())
    return(md5.hexdigest()[:20])

class FireBase:
    def __init__(self):
        cred = credentials.Certificate(
            '/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.docRef = self.db.collection('Q54')

    def searchData(self, id):
        data = self.docRef.document(id).get()
        return(data.to_dict())

    def addAccessedTime(self, id, accessedTime):
        doc = {
            'accessedTime':accessedTime+1
        }
        newDocRef = self.docRef.document(id)
        newDocRef.update(doc)


    def saveData(self, id, longUrl):
        doc = {
            'longURL': longUrl,
            'accessedTime': 0
        }
        newDocRef = self.docRef.document(id)
        newDocRef.set(doc)

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        longUrl = request.form['url']
        id = urlEncode(longUrl)
        db.saveData(id, longUrl)
        shortUrl = '{}/{}'.format(serverIP, id)
        return render_template('home.html', home = serverIP, shortURL = shortUrl)
    return render_template('home.html', home = serverIP, shortURL = '')

@app.route("/<id>")
def redirectToUrl(id):
    data = db.searchData(id)
    accessedTime = data['accessedTime']
    db.addAccessedTime(id, accessedTime)
    return redirect(data['longURL'])

@app.route("/<id>/stats")
def showUrlStats(id):
    data = db.searchData(id)
    shortURL = '{}/{}'.format(serverIP, id)
    longURL = data['longURL']
    accessedTime = data['accessedTime']
    return render_template('stats.html',home = serverIP, shortURL = shortURL,longURL = longURL,accessedTime = accessedTime)


if __name__ == '__main__':
    db = FireBase()
    app.run(debug=True)