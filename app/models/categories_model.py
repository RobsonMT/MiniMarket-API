from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class CategoryModel(db.Model):

    id: int
    name: str
    url_img: str

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    url_img = Column(String)

    # products = relationship(
    #     "ProductModel",
    #     secondary="product_categories",
    #     back_populates="categories",
    #     lazy="joined",
    # )
