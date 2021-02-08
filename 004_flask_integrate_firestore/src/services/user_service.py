from src.daos.user_dao import UserDAO
from src.models.user import User


class UserService:

    @classmethod
    def enroll_user(cls, user:User):
        result= UserDAO.save_user(user)
        return result

    @classmethod
    def get_user(cls,user_id:str)->User:
        result = UserDAO.get_user(user_id)
        return result