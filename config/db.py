# mysqlclient設定
from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://asdf0359:zxcv0359@192.168.68.60:3306/node_sequelize_api_db")



# mysqlconn= MySQLdb.connect(
#         host='192.168.68.60',
#         port = 3306,
#         user='asdf0359',
#         passwd='zxcv0359',
#         db ='fastAPItest',
#         )

meta = MetaData()

conn = engine.connect()




# DB_URL = "mysql+pymysql://asdf0359:zxcv0359@192.168.68.60:3306/fastAPItest"

# Engine = create_engine(DB_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#         # yield: 產生器，每次執行到yield時，會暫停，並回傳yield後面的值，下次執行時，會從yield暫停的地方繼續執行
    
#     except Exception:
#         db.rollback()
#         raise

#     finally:
#         db.close()