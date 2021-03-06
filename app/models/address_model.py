from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from app.configs.database import db


@dataclass
class AddressModel(db.Model):

    # id: int
    street: str
    number: int
    zip_code: str
    district: str

    __tablename__ = "adresses"

    id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    zip_code = Column(String, nullable=False)
    district = Column(String, nullable=False)
