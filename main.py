from fastapi import FastAPI

app = FastAPI()

# 追加: 動作確認用のルート
@app.get("/")
async def read_root():
    return {"message": "FastAPI is working"}