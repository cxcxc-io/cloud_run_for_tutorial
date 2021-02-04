sudo apt-get install -y python3-venv

建立新虛擬環境
python3 -m venv 002_chatbot_env

激活虛擬環境
source 002_chatbot_env/bin/activate

建置requirements.txt
pip3 install -r requirements.txt


```
gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld
```

部署環境變數
LINE_CHANNEL_ACCESS_TOKEN
LINE_CHANNEL_SECRET

```
gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
```