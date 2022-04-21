from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from app.configs.database import db

@dataclass
class CategoryModel(db.Model):

    id = int
    name = str
    image = str

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    Image = Column(String)