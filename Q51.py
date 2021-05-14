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

def showData():
  for doc in doc_ref.stream():
    data = doc.to_dict()
    print(timeToStr(data['saveTime']) + ' - ' + data['noteContent'])

def saveData():
  savedNote = ''
  for word in sys.argv[2:]:
    savedNote  = savedNote + word + ' '

  doc = {
    'noteContent': savedNote,
    'saveTime': time.time()
  }
  doc_ref.add(doc)
  print('Your note was saved.')



# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('/Users/kshskevin/57_challenges/challenge-q51-firebase-adminsdk-f34xu-0a07380a60.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

doc_path = "/notes/note_01"
# 透過路徑，產生參考
doc_ref = db.collection('notes')



if sys.argv[1] == 'new':
  saveData()
elif sys.argv[1] == 'show':
  showData()


