from dataclasses import dataclass
from datetime import datetime as dt

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import validates

from app.configs.database import db


@dataclass
class ProductModel(db.Model):

    id: int
    name: str
    description: str
    sale_price: float
    cost_price: float
    unit_type: str
    url_img: str
    category_id: int
    establieshment_id: int

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)
    sale_price = Column(Numeric(asdecimal=True))
    cost_price = Column(Numeric(asdecimal=True))
    unit_type = Column(String(100))
    url_img = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    establieshment_id = Column(Integer, ForeignKey("establishments.id"))
