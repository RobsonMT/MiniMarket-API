from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer
from sqlalchemy.orm import validates

 
@dataclass
class SaleProductModel(db.Model):

    id : int
    sale_id : int
    product_id : int

    __tablename__ = 'sales_products'

    id = Column(Integer, primary_key=True)
    sale_id = Column(Integer, ForeignKey=("sales.id"))
    product_id = Column(Integer, ForeignKey=("products.id"))