
from linebot.models import (
    TextSendMessage,QuickReply,QuickReplyButton,MessageAction
)
    
    
from linebot import (
    LineBotApi
)

import os


class HakkaTextService:
    
    line_bot_api=LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    @classmethod
    def text_to_voice_line(cls, event):
        user_input = event.message.text

        text_qrb=QuickReplyButton(action=MessageAction(label="發送文字消息", text="text2")
)
        return_message=[TextSendMessage(user_input,quick_reply=QuickReply(items=[text_qrb]))]

        cls.line_bot_api.reply_message(
            event.reply_token,
            return_message
        )

        return return_message