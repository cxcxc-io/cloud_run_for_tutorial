'''

當用戶關注時，必須取用照片，並存放至指定bucket位置，而後生成User物件，存回db

當用戶取消關注時，
    從資料庫提取用戶數據，修改用戶的封鎖狀態後，存回資料庫

'''

from linebot import (
    LineBotApi, WebhookHandler
)
import os

# 載入Follow事件
from linebot.models.events import (
    FollowEvent,UnfollowEvent
)

from services.user_service import UserService
from services.hakka_text_service import HakkaTextService

class LineBotController:


    # 將消息交給用戶服務處理
    @classmethod
    def follow_event(cls,event):
        print(event)
        UserService.line_user_follow(event)

    @classmethod
    def unfollow_event(cls,event):
        UserService.line_user_unfollow(event)
    

    # 未來可能會判斷用戶快取狀態
    # 現在暫時無
    @classmethod
    def handle_text_message(cls,event):
        return_to_line = HakkaTextService.text_to_voice_line(event)
        return return_to_line