from models.user import User

import os
os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"
os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:8080/firestore"
os.environ["FIRESTORE_HOST"] = "http://localhost:8080"

from google.cloud import firestore

class UserDAO:
    
    db = firestore.Client()
    users_ref= db.collection(u'users')

    @classmethod
    def save_user(user:User) -> None:
        users_ref.add(document_data=user.to_dict, document_id=user.user_id)
        return user.to_dict()

    @classmethod
    def get_user(user_id:str) -> User:
        user_ref = users_ref.document(user_id)
        user_doc =  user_ref.get()
        user = User.from_dict(user_doc.to_dict())
        return user




    