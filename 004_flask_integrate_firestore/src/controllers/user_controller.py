from src.services.user_service import UserService
from src.models.user import User
from flask import Request,Response
import json
class UserController:

    @classmethod
    def add_user(cls,request:Request):
        print(json.loads(request.get_data()))
        user = User.from_dict(json.loads(request.get_data()))
        UserService.enroll_user(user)
        return 'OK'

    @classmethod
    def get_user(cls,request:Request):
        user_id= request.args.get('user_id')
        user = UserService.get_user(user_id)
        return user.to_dict()
