from sqlalchemy import Column, ForeignKey, Integer

from app.configs.database import db


class ProductCategory(db.Model):

    id: int
    product_id: int
    category_id: int

    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
