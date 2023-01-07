from pydantic import BaseModel, Field


class Order(BaseModel):
    # id: int = Field(...)
    # ord_number: str = Field(...)
    # ord_total: int = Field(...)
    # ord_phone: str = Field(...)
    # ord_address: str = Field(...)
    # ord_payment: str = Field(...)
    # ord_byusername: str = Field(...)
    # ord_byid: int = Field(...)
    # ord_state: str = Field(...)
    # ord_logistics: str = Field(...)


    id: int
    ord_number: str
    ord_total: int
    ord_phone: str
    ord_address: str
    ord_payment: str
    ord_byusername: str
    ord_byid: int
    ord_state: str
    ord_logistics: str



