以Flask集成MVC的方式，製作一隻Restful API 

# 資料夾結構

```
src/
    models
        user.py
    daos
        user_dao.py
    services
        user_service.py
    controllers
        user_controller.py
test/
application.conf

```

# 環境建立

## 虛擬環境建立
```
sudo apt-get install -y python3-venv
python3 -m venv venv_004_flask_mvc
source venv_004_flask_mvc/bin/activate
pip3 install -r requirements.txt
```
## 增加套件提示與自動補全

的File -> Settings -> Open Preferences

選擇Python -> Auto Complete -> Auto Complete Extra Paths -> Edit in settings.json

將python.autoComplete.extraPaths覆蓋為下方值，請注意此處寫的python3.7，須按照當時的cloud shell editor python版本而定。

```
"python.autoComplete.extraPaths": [
    "/home/USER_NAME/cloud_run_for_tutorial/002_chatbot_flask/venv_002_chatbot_flask/lib/python3.7/site-packages/"
]
```

## 程式開發環境建立

### 建立firestore 虛擬器

```
firebase emulators:start --only firestore
```

### 編輯models資料夾

### 編輯daos資料夾

### 編輯services資料夾

### 編輯controllers資料夾

### 啟用flask