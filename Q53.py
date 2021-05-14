import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys
import time

def timeToStr(timestamp):
  nowTime = int(timestamp)  # 取得現在時間
  structTime = time.localtime(nowTime)  # 轉換成時間元組
  timeString = time.strftime("%Y-%m-%d", structTime)  # 將時間元組轉換成想要的字串
  return(timeString)


class ToDoList:
    def __init__(self):
        cred = credentials.Certificate(
            '/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.doc_ref = self.db.collection('Q53')

    def showData(self):
        for doc in self.doc_ref.stream():
            data = doc.to_dict()
            print(data['noteContent'] + f'           (docID : {doc.id}')

    def saveData(self, savedNote):
        doc = {
            'noteContent': savedNote,
            'saveTime': time.time()
        }
        self.doc_ref.add(doc)
        print('Your note was saved.')

    def deleteData(self, docID):
        self.doc_ref.document(docID).delete()
        print('Your note was deleted.')

    def whatToDo(self, instruction):
        if instruction == '1':
            while True:
                savedNote = input('Please enter your task: ')
                if savedNote == '':
                    break
                self.saveData(savedNote)

        elif instruction == '2':
            self.showData()

        elif instruction == '3':
            self.deleteData(input('Which task you want to delete? '))



if __name__ == '__main__':
    mainFunction = ToDoList()
    while True:
        mainFunction.whatToDo(input('What do you wanna do? 1)Enter new task 2)Display all task 3)Delete a task'))
