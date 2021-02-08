

from __future__ import annotations
class User(object):
    def __init__(self, name, age, user_id):
        self.name=name
        self.age=age
        self.user_id=user_id
    
    @staticmethod
    def from_dict(source) -> User :
        user=User(name=source[u'name'],age=source[u'age'],user_id=source[u'user_id'])
        return user

    def to_dict(self):
        data_dict={
            u'name':self.name,
            u'age':self.age,
            u'user_id':self.user_id
        }

        return data_dict

    def __repr__(self):
        return ( f'User( name={self.name}, age={self.age}, user_id={self.user_id} )'  )

    