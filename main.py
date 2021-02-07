from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    email:str

@app.get("/")
def index():
    return {"message":"Hello world"}

@app.post("/signin")
def signin(item:Item):
    if item.email == 'tee_api@hotmail.com':
        return {"username":"apisit amornchanchaigul","position":"develop"}
    else:
        return {"username":"อภิสิทธิ์ อมรชาญชัยกุล","position":"develop"}

if __name__ == '__main__':
    uvicorn.run('main:app',host="0.0.0.0",port=8888)