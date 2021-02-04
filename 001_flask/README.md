請將內容裡提及的PROJECT-ID 改為您的Project

構建Image，並推至 GCP的Artifact Registry
```
gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld
```

將該Image推至 GCP的Cloud Run
```
gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
```

以Console方式清除資源
