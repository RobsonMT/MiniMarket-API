from dataclasses import dataclass
from enum import unique
from itertools import product

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class EstablishmentModel(db.Model):

    # id: int
    name: str
    cnpj: str
    contact: str
    url_logo: str
    user_id: int
    address_id: int
    address: object
    # clients: list
    # products: list

    __tablename__ = "establishments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    cnpj = Column(String(100), unique=True)
    contact = Column(String)
    url_logo = Column(String)
    address_id = Column(Integer, ForeignKey("adresses.id"), unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    address = relationship("AddressModel", backref="address", uselist=False)

    clients = relationship(
        "ClientModel", backref=backref("clients", uselist=True), uselist=False
    )

    # products = relationship(
    #     "ProductModel", backref=backref("products", uselist=True), uselist=False
    # )
