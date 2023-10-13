#fastapiのモジュール
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

#postgreの接続のモジュール

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

<<<<<<< HEAD

=======
>>>>>>> 12d683373c0a30c6606c8602aae055cfb450b20a
class User(BaseModel):
    user_name:str
    reserved_number:int
    reserved_data:str
    hospital_name:str


user_data={"user_name":"岩永　拓也",
"reserved_number":"4444",
"reserved_data":"２０２３/０９/２６（火） １３：３０〜",
"hospital_name":"すやま歯科医院"}


@app.get("/user/user_data")
def read_root():
    return user_data


@app.post("/reserved_data_receive")
def reserved_data_receive(user:User):

    return{"res":"受付が完了しました！"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
