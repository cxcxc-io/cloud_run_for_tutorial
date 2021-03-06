import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from flask import Flask, request, abort
from src.controllers.user_controller import UserController
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/user',methods=['GET'])
def get_user():
    reuslt = UserController.get_user(request)
    return reuslt

@app.route('/user',methods=['POST'])
def save_user():
    result = UserController.add_user(request)
    return result

app.run()