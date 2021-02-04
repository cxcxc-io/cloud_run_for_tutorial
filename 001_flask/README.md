

## 專案目標

透過Cloud Shell Editor  開發一個Web application，並部署在Cloud run 上

## 流程描述

為Cloud Shell Editor 的Python專案建置獨立虛擬環境，並安裝套件

設定IDE，使IDE可以偵測到該專案的套件

開發程式

透過Cloud Shell 環境執行，並預覽

確認無誤後，透過 Cloud Build 編譯成 image，並推入 Artifact Registry

設定Cloud Run，從Artifact Registry提取image，設定成服務

## 建置獨立虛擬環境

指定此資料夾為Workspace

```
# 安裝venv套件
sudo apt-get install -y python3-venv
# 建置虛擬環境
python3 -m venv venv_001_flask
# 指定虛擬環境
source venv_001_flask/bin/activate
# 安裝套件
pip3 install -r requirements.txt

```

## 設定IDE，使IDE可以偵測到該專案的套件

點擊左上角的File -> Settings -> Open Preferences

選擇Python -> Auto Complete -> Auto Complete Extra Paths -> Edit in settings.json

將python.autoComplete.extraPaths覆蓋為下方值，請注意此處寫的python3.7，須按照當時的cloud shell editor python版本而定。

```
"python.autoComplete.extraPaths": [
    "/home/USER_NAME/cloud_run_for_tutorial/001_flask/venv_001_flask/lib/python3.7/site-packages/"
]
```

## 開發

## 執行預覽

```
python3 main.py
```

## 透過 Cloud Build 編譯成 image，並推入 Artifact Registry

請將內容裡提及的PROJECT-ID 改為您的Project

構建Image，並推至 GCP的Artifact Registry
```
gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld
```

## 設定Cloud Run，從Artifact Registry提取image，設定成服務

將該Image推至 GCP的Cloud Run
```
gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
```

以Console方式清除資源
