from sqlalchemy import Table, Column, Integer, String, Numeric, ForeignKey
from config.db import meta
# from config.db import Base

# class Order(Base):
#     __tablename__ = "orders"
    
#     id = Column(Integer, primary_key=True)
#     ord_number = Column(String)
#     ord_total = Column(Integer)
#     ord_phone = Column(String)
#     ord_address = Column(String)
#     ord_payment = Column(String)
#     ord_byusername = Column(String)
#     ord_byid = Column(Integer)
#     ord_state = Column(String)
#     ord_logistics = Column(String)


orders = Table(
    'orders', meta,
    Column('id', Integer, primary_key=True),
    Column('ord_number', String(255)),
    Column('ord_total', Numeric(10)),
    # Column('ord_total', Integer),
    Column('ord_phone', String(255)),
    Column('ord_address', String(255)),
    Column('ord_payment', String(255)),
    Column('ord_byusername', String(255)),
    Column('ord_byid', Integer),
    Column('ord_state', String(255)),
    Column('ord_logistics', String(255)),

)

