import hashlib
import csv
import pandas as pd
from random import choice, sample
from flask import Flask, jsonify, request, redirect, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

serverIP = 'http://127.0.0.1:5000'
app = Flask(__name__)
ans = 0

def encodeID(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    return(md5.hexdigest()[:20])

class FireBase:
    def __init__(self):
        cred = credentials.Certificate(
            '/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.docRef = self.db.collection('Q55')

    def searchData(self, id):
        data = self.docRef.document(id).get()
        return (data.to_dict())


    def saveData(self, id, content):
        doc = {
            'text' : content
        }
        newDocRef = self.docRef.document(id)
        newDocRef.set(doc)


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        content = request.form['content']
        id = encodeID(content)
        db.saveData(id, content)
        url = '{}/{}'.format(serverIP, id)
        return render_template('home.html', url=url)
    return render_template('home.html')

@app.route('/<id>', methods=('GET', 'POST'))
def shareText(id):
    content = db.searchData(id)['text']
    if request.method == 'POST':
        content = request.form['content']
        id = encodeID(content)
        db.saveData(id, content)
        url = '{}/{}'.format(serverIP, id)
        return render_template('home.html', url=url)
    return render_template('home.html',content = content)

if __name__ == '__main__':
    db = FireBase()
    app.run(debug=True)