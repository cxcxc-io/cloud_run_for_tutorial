## 專案目標

透過Cloud Shell Editor，嘗試串接firestore的程式碼

參考內容： https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py


## 流程描述

虛擬環境與套件準備

建置firestore，匯入資料

插入資料

讀取單筆資料

更新資料

讀取多筆資料

## 虛擬環境與套件準備

指定此資料夾為Workspace
```
# 安裝venv套件
sudo apt-get install -y python3-venv
# 建置虛擬環境
python3 -m venv venv_003_firestore
# 指定虛擬環境
source venv_003_firestore/bin/activate
# 安裝套件
pip3 install -r requirements.txt
```

## 建置firestore 模擬器

https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore

https://cloud.google.com/firestore/docs/security/test-rules-emulator

```
 firebase emulators:start --only firestore
```

## 匯入資料

參照import_data_to_firestore.py

### 關鍵在於環境變數的指定

```
FIRESTORE_EMULATOR_HOST="localhost:8080"
FIRESTORE_EMULATOR_HOST_PATH="localhost:8080/firestore"
os.environ["FIRESTORE_HOST"]="http://localhost:8080"
```

### 操作資料流程如下

建立客戶端
透過客戶端指定collection
並由該collection生成 Document 並進行set 
或直接由collection進行add的動作


## ORM的方式寫入與讀取資料

撰寫 Class的時候，找出能夠代表物件獨特性的欄位，未來考慮作為document的id欄位，並建議編寫三個方法

to_dict

__repr__

from_dict (static method)




