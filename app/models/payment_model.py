from dataclasses import dataclass
from datetime import datetime as dt

from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.orm import validates

from app.configs.database import db


@dataclass
class PaymentModel(db.Model):

    id: int
    form_of_payment: str

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    form_of_payment = Column(String(100))
