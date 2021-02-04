## 專案目標

透過Cloud Shell Editor，嘗試串接firestore的程式碼

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

## 建置firestore，匯入資料