from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.configs.database import db
from sqlalchemy.orm import relationship, backref
@dataclass
class CategoryModel(db.Model):

    id = int
    name = str
    image = str

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    Image = Column(String)

    products = relationship(
        "ProductModel",
        secondary="product_categories", 
        backref=backref("categories", uselist=True)
    )