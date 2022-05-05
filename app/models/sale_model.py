from dataclasses import dataclass
from datetime import datetime as dt
from enum import unique

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class SaleModel(db.Model):
    id: int
    date: dt
    paid_date: dt
    client_id: int
    payment_id: int
    sale_total: float
    remain_to_pay: float
    payment_method: object

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=dt.now())
    paid_date = Column(DateTime, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id"), nullable=False)
    sale_total = Column(Numeric(asdecimal=True), nullable=False)
    remain_to_pay = Column(Numeric(asdecimal=True), nullable=False)

    payment_method = relationship(
        "PaymentModel", backref="payment_method", uselist=False
    )

    products = relationship(
        "ProductModel",
        secondary="sales_products",
        backref=backref("sales_products", uselist=True),
    )
