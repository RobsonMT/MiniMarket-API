from dataclasses import dataclass
from app.configs.database import db
from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import validates


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
    category_id = Column(Integer, ForeignKey=("categories.id"))
    establieshment_id = Column(Integer,ForeignKey=("establishments.id"))

 