
# 定義 class，並設置方法
from __future__ import annotations
class Person(object):

    def __init__(self, name:str,age:int):
        self.name=name
        self.age=age

    @staticmethod
    def from_dict(source) -> Person:
        person = Person(source[u'name'], source[u'age'])
        return person
    
    def to_dict(self):
        return_data_dict= {
            u'name':self.name,
            u'age':self.age
        }
        return return_data_dict

    def __repr__(self):
        return ( f'Person( name={self.name} age={self.age} )'  )

# 建立模擬資料
small_ming= Person(name='ming',age=20)
small_mei = Person(name='mei',age= 99)

# 設定本地環境變數，未來可撤除
import os
os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"
os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:8080/firestore"
os.environ["FIRESTORE_HOST"] = "http://localhost:8080"

# 建立客戶端
from google.cloud import firestore 
db = firestore.Client()

# 建立表格
people_ref= db.collection(u'people')

# 將資料以物件方式，插入表格內
people_ref.document(small_mei.name).set(small_mei.to_dict())
people_ref.add(small_ming.to_dict(),document_id=small_ming.name)

# 讀取資料，並轉成物件
docs = people_ref.stream()
for doc in docs:
    person= Person.from_dict(doc.to_dict())
    print(person)
    print(f'{doc.id} => {doc.to_dict()}')



