'''

line版儲存line用戶個資時，取照片，更換連結，放回原object，

取出用戶個資時，傳入用戶id，作為檢索條件

'''


from models.user import User
from flask import Request
from linebot import (
    LineBotApi
)
import os

from daos.user_dao import UserDAO

class UserService:

    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    # 取得line event，將line event拿去取個資，轉換成User，並將其照片取出
    @classmethod
    def line_user_follow(cls, event):

        print(event)
        # 取個資
        line_user_profile= cls.line_bot_api.get_profile(event.source.user_id)
        # line_user_profile= cls.line_bot_api.get_profile(event)
        print(line_user_profile)
        print(type(line_user_profile))
        print(line_user_profile.user_id)
        print(line_user_profile.picture_url)
        print(line_user_profile.display_name)
        print(line_user_profile.status_message)
        print(line_user_profile.language)
        # event轉換成user
        user = User(
            line_user_id=line_user_profile.user_id,
            line_user_pic_url=line_user_profile.picture_url,
            line_user_nickname=line_user_profile.display_name,
            line_user_status=line_user_profile.status_message,
            line_user_system_language=line_user_profile.language,
            blocked=False
        )

        # 取得用戶照片，存放回cloud storage，並將連結存回user的連結


        # 存入資料庫
        UserDAO.save_user(user)
        
        # 打印結果
        print(user)

        # 回傳結果給handler
        # 關注的部分，不回傳，交由控制台回傳
        pass

    # 從資料庫內取出用戶資料，並將其blocked狀態，更改為True
    @classmethod
    def line_user_unfollow(cls, event):

        user = UserDAO.get_user(event.source.user_id)
        user.blocked=True
        UserDAO.save_user(user)
        print(user)
        print('用戶已封鎖')
        
        pass

    @classmethod
    def get_user(cls,user_id:str):
        user=UserDAO.get_user(user_id)
        return user
        

        
