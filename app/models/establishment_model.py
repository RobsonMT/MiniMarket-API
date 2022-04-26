from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, String
from app.configs.database import db
from sqlalchemy.orm import relationship, backref

@dataclass
class EstablishmentModel(db.Model):

    id: int
    name: str
    cnpj: str
    contact: str
    url_logo: str
    user_id: int
    address_id: int

    __tablename__ = "establishments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    cnpj = Column(String(100), unique=True)
    contact = Column(String)
    url_logo = Column(String)
    address_id = Column(Integer, ForeignKey("adresses.id"), unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    clients = relationship(
        "ClientModel", backref=backref("clients", uselist=True), uselist=False
    )

    products = relationship(
        "ProductModel", backref=backref("products", uselist=True), uselist=False
    )