from dataclasses import dataclass
from numbers import Integral
from sqlalchemy import Column, Integer, ForeignKey
from app.configs.database import db

@dataclass
class ProductCategory(db.Model):
    
    id: int
    product_id: int
    category_id: int

    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))