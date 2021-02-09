import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from flask import Flask, request, abort

from flask_cors import CORS


from linebot.exceptions import (
    InvalidSignatureError
)

from controllers.line_bot_handler import LineBotController

from controllers.user_controller import UserController

app = Flask(__name__)
CORS(app)

from linebot import (
    LineBotApi, WebhookHandler
)
import os
line_bot_api=LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])
handler=WebhookHandler(channel_secret=os.environ["LINE_CHANNEL_SECRET"])


# 載入Follow事件
from linebot.models.events import (
    FollowEvent,UnfollowEvent,MessageEvent,TextMessage
)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # print(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(FollowEvent)
def handle_line_follow(event):
    return LineBotController.follow_event(event)

@handler.add(UnfollowEvent)
def handle_line_unfollow(event):
    return LineBotController.unfollow_event(event)

@handler.add(MessageEvent,TextMessage)
def handle_line_text(event):
    return LineBotController.handle_text_message(event)

@app.route("/user",methods=['GET'])
def get_user():
    result = UserController.get_user(request)
    return result


if __name__ == "__main__":
    app.run()