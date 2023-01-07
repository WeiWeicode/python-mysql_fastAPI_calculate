from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.order import router

from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from datetime import datetime
# from typing import Union



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(router)


# 測試get_all_orders
# @app.get("/orders")
# def get_orders():
#     return get_all_orders()



# 以下是測試json寫入

# fake_db = {}


# class Item(BaseModel):
#     title: str
#     timestamp: datetime
#     description: Union[str, None] = None


# app = FastAPI()


# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatible_item_data
#     return fake_db[id]

# @app.get("/items/{id}")
# def read_item(id: str):
#     return fake_db[id]






# uvicorn main:app --reload
# 只能用localhost方式進入

# uvicorn main:app  --reload --host 0.0.0.0 --port 8080
# 用IP方式架設