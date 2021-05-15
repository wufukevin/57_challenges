from datetime import datetime

from flask import Flask, jsonify
import time
app = Flask(__name__)

localTime = {
    'localTime': datetime.now()
}

@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route('/localTime')
def getLocalTime():
    json = jsonify(localTime)
    print(json)
    return json


if __name__ == '__main__':
    app.run(debug=True)