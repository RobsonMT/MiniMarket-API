from dataclasses import dataclass
from unicodedata import category

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

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
    establishment_id: int
    categories: list

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String)
    sale_price = Column(Numeric(asdecimal=True), nullable=False)
    cost_price = Column(Numeric(asdecimal=True), nullable=False)
    unit_type = Column(String(100), nullable=False)
    url_img = Column(String)
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)

    categories = relationship(
        "CategoryModel",
        secondary="product_categories",
        backref="categories",
        lazy="dynamic",
    )
