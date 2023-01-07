from fastapi import APIRouter
# from config.db import get_db
from config.db import conn
from models.order import orders
from schemas.order import Order as OrderSchema
# from crud.crud import get_orders
from calculate.order import orderTotal, orderTotalAndAverage
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

router = APIRouter()



# @router.get("/orders")
# def get_orders(db_session: Session = Depends(get_db)):
#     return get_orders(db_session)



@router.get("/orders")
async def read_data():
    
    s = orders.select()
    result = conn.execute(s).fetchall()

    # fetchall: 取得所有資料
    return result



# 統計訂單數量，total: 加總金額
# @router.get("/orders/total")
# async def read_data():
#     s = orders.select()
#     result = Engine.execute(s).fetchall()
#     resulttest = orderTotalAndAverage(result)
#     return resulttest