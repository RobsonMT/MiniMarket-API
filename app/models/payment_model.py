from dataclasses import dataclass
from app.configs.database import db
from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship, backref, validates


@dataclass
class PaymentModel(db.Model):
    
    id: int
    form_of_payment: str

    __tablename__ = "payments"
 
    id = Column(Integer, primary_key=True) 
    form_of_payment = Column(String(100))
    
    sales = relationship(
        "SaleModel",
        backref=backref("sales", uselist=True)
    )

 