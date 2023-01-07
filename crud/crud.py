# from sqlalchemy.orm import Session
# from models.order import Order
# from schemas.order import Order as OrderSchema


# def get_orders(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Order).offset(skip).limit(limit).all()

# def get_orders(db: Session):
#     return db.query(Order).all()