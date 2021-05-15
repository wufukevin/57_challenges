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

class FireBase:
    def __init__(self):
        cred = credentials.Certificate(
            '/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.docRef = self.db.collection('Q57')

    def getData(self):
        return(self.docRef.get())


    def addData(self, question, correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
        doc = {
            'Question' : question,
            'CorrectAnswer' : correctAnswer,
            'WrongAnswer1' : wrongAnswer1,
            'WrongAnswer2': wrongAnswer2,
            'WrongAnswer3': wrongAnswer3
        }
        self.docRef.add(doc)


@app.route('/', methods=('GET', 'POST'))
def home():
    global ans
    result = ''
    if request.method == 'POST':
        userChoice = request.form['choice']
        if int(userChoice) == int(ans):
            result = 'You are correct!!'
        else:
            result = 'Yout are wronge~~'

    question = db.getData()
    questionList = []
    for doc in question:
        questionList.append(doc.to_dict())
    currentQuestion = choice(questionList)
    questionString = currentQuestion['Question']
    optionList = []
    optionList.append(currentQuestion['CorrectAnswer'])
    optionList.append(currentQuestion['WrongAnswer1'])
    optionList.append(currentQuestion['WrongAnswer2'])
    optionList.append(currentQuestion['WrongAnswer3'])
    optionList = sample(optionList, 4)
    for idx, option in enumerate(optionList):
        if option == currentQuestion['CorrectAnswer']:
            ans = idx

    return render_template('home.html', result = result, question = questionString, opt1 = optionList[0], opt2 = optionList[1], opt3 = optionList[2], opt4 = optionList[3])

@app.route('/addNewQuestion', methods=('GET', 'POST'))
def addQuestion():
    if request.method == 'POST':
        db.addData(request.form['question'],request.form['correctAnswer'],request.form['wrongAnswer1'],request.form['wrongAnswer2'],request.form['wrongAnswer3'])
    return render_template('addQuestion.html')

if __name__ == '__main__':
    db = FireBase()
    app.run(debug=True)