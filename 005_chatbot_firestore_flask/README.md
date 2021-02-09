## 專案目標

## 流程描述

## 虛擬環境與套件準備

```
sudo apt-get install -y python3-venv
python3 -m venv venv_005_chatbot_firestore_flask
source venv_005_chatbot_firestore_flask/bin/activate
pip3 install -r requirements.txt
```

## 建置firestore 模擬器

https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore

https://cloud.google.com/firestore/docs/security/test-rules-emulator

```
 firebase emulators:start --only firestore
```

## 開發用戶關注與取消關注

參照

### 關鍵在於環境變數的指定

```
export FIRESTORE_EMULATOR_HOST=localhost:8080
export FIRESTORE_EMULATOR_HOST_PATH=localhost:8080/firestore
export FIRESTORE_HOST=http://localhost:8080
export LINE_CHANNEL_ACCESS_TOKEN=""
export LINE_CHANNEL_SECRET=""
```

### 啟動ngrok，並將生成的連結貼回Line Console

```
ngrok http -ap 5000
```

###

