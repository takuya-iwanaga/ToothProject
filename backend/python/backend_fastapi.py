from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

user_data={"user_name":"岩永　拓也",
"reserved_number":"4444",
"reserved_data":"２０２３/０９/２６（火） １３：３０〜",
"hospital_name":"すやま歯科医院"}


@app.get("/user/user_data")
def read_root():
    return user_data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}