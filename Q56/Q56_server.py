import hashlib
import csv
import pandas as pd
from flask import Flask, jsonify, request, redirect, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

serverIP = 'http://127.0.0.1:5000'
app = Flask(__name__)

class FireBase:
    def __init__(self):
        cred = credentials.Certificate(
            '/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.docRef = self.db.collection('Q56')

    def getData(self):
        return(self.docRef.get())


    def addData(self, name, number, value):
        doc = {
            'Name' : name,
            'Serial Number' : number,
            'Value' : value
        }
        self.docRef.add(doc)


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        value = request.form['value']
        db.addData(name, number, value)
        return render_template('home.html', success = 'Data save success!')
    elif request.method == 'GET':
        data = db.getData()
        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            # writer.writerow(['Name', 'Serial Number', 'Value'])
            for doc in data:
                dataInDict = doc.to_dict()
                dataList = []
                dataList.append(dataInDict['Name'])
                dataList.append(dataInDict['Serial Number'])
                dataList.append(dataInDict['Value'])
                writer.writerow(dataList)
        columns = ['Name', 'Serial Number', 'Value']
        dataInCsv = pd.read_csv('output.csv', names=columns)
        return(dataInCsv.to_html())
    return render_template('home.html')

if __name__ == '__main__':
    db = FireBase()
    app.run(debug=True)