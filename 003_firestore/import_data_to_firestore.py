

from google.cloud import firestore 
import os

os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"
os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:8080/firestore"
os.environ["FIRESTORE_HOST"] = "http://localhost:8080"

import google
import mock
# credentials = mock.Mock(spec=google.auth.credentials.Credentials)
# db = firestore.Client(project='cxcxc-2021-01-30-lh', credentials=credentials)

# 需事前指定好project
db = firestore.Client()
# [START quickstart_add_data_one]
# [START firestore_setup_dataset_pt1]
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})

#讀取資料
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')