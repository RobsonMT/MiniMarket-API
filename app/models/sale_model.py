from dataclasses import dataclass
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, DateTime, Numeric
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from datetime import datetime as dt
@dataclass
class SaleModel(db.Model):
    
    id : int
    date : dt
    paid_date: dt
    client_id: int
    payment_id: int
    sale_total: float
    remain_to_pay: float

    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)  
    date = Column(DateTime)
    paid_date = Column(DateTime)
    client_id = Column(Integer, ForeignKey("clients.id"), unique=True)
    payment_id = Column(Integer, ForeignKey("payments.id"), unique=True)
    sale_total = Column(Numeric(asdecimal=True))
    remain_to_pay = Column(Numeric(asdecimal=True))

    products = relationship(
        "ProductModel",
        secondary="sales_products",
        backref=backref("products", uselist=True)
        )
